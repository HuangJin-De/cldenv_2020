import csv
import numpy as np
import numpy.matlib
from netCDF4 import Dataset
import pickle
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy
import sys
sys.path.append('/data/cloud/Goldtimes5/code/')
from PYfunctions.data_load.load_SPCAM import SPCAM

data_path= '/data/cloud/Goldtimes5/data/SPCAM/CPL64/'

#var_names= np.array(['MSE_sur','TS','CAPE','RHmid','CCW_gridmean','CCW_gridvar','CCW_aggrgate'])
#var_names= np.array(['CCW_gridmean','CCW_gridvar','CCW_aggrgate'])
var_names= np.array(['CCW_gridvar'])

# var_name= 'TS'
# var_name= 'OMEGA500'

CRM_temp= '/data/dadm1/model_output/SPCAM/CPL64/CPL64.cam.h1.0001-01-01-00000.nc'
with Dataset(CRM_temp,'r') as D:
    lat=D.variables['LAT_15s_to_30n'][:]
    lon=D.variables['LON_60e_to_180e'][:]
    maxGY= lat.size
    maxGX= lon.size

#=== load data and plot
for vv in np.arange(0,var_names.shape[0]):
  var_name= var_names[vv]
  data_file= data_path+var_name+'.pk'
  data_DJF= SPCAM(var_name, 'DJF')
  data_JJA= SPCAM(var_name, 'JJA')
  data_ann= SPCAM(var_name, 'ann')
  data_DJF= np.nanmean(np.nanmean(data_DJF,0),0)
  data_JJA= np.nanmean(np.nanmean(data_JJA,0),0)
  data_ann= np.nanmean(np.nanmean(data_ann,0),0)
  for season in ['DJF', 'JJA', 'ann']:
    if season == 'DJF':
      data=data_DJF
    elif season == 'JJA':
      data=data_JJA
    elif season == 'ann':
      data=data_ann
    if var_name== 'TS' :
      data=data-273.15
      level= np.arange(14,38,4)
      data[(data<14)]=14
    elif  var_name== 'PS':
      data=data/100
      level= np.arange(980,1035,5)
      data[(data>1030)]=1030
      data[(data<980)]=980
    elif  var_name== 'MSE_sur':
      data=data/1000
      level= np.arange(320,360,4)
      data[(data<320)]=320
    elif  var_name== 'CAPE':
      level= np.arange(0,4400,400)
      data[(data<0)]=0
      data[(data>4000)]=4000
    elif var_name== 'CCW_gridmean':
      level= np.arange(0,2.2e-5,2e-6)
      data[(data>2e-5)]=2e-5
    elif var_name== 'CCW_gridvar':
      level= np.arange(0,5.5e-11,5e-12)
      data[(data>4.9e-11)]=4.9e-11
    elif var_name== 'CCW_aggrgate':
      level= np.arange(10,70,6)
      data[(data>64)]=64
    elif var_name== 'RHmid':
      level= np.arange(0,110,10)
      data=data*100
      data[(data>100)]=100
    plt.figure(figsize=(7,3))
#    cmap = plt.cm.jet  # define the colormap
#    cmaplist = [cmap(i) for i in range(cmap.N)]
 #   cmap = mpl.colors.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, cmap.N)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    cs1= plt.contourf(lon,lat,data,levels=level,cmap='RdYlBu_r')
#     plt.clim((-1,1))
    plt.colorbar().set_ticks(level)
    ax.set_xlim(60, 180)
    ax.set_ylim(-15, 30)
    picsave= '/data/cloud/Goldtimes5/pic/SPCAM/Mean/'+var_name+'_'+season+'.png'
    plt.savefig(picsave)
    plt.show()
    plt.close()
