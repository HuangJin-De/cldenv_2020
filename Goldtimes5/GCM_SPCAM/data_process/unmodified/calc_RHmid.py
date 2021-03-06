import csv
from datetime import datetime
import numpy as np
from netCDF4 import Dataset
import pickle
from scipy import interpolate
import matplotlib.pyplot as plt
import sys
sys.path.append('/data/cloud/Goldtimes5/code/')
from PYfunctions.physics.calc_q_sat import q_sat

# Timer
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start  =", current_time)

years= np.arange(6,7)
year_num= years[-1]- years[0] +1

SPCAM_path= '/data/dadm1/model_output/SPCAM/CPL64/'
# CPL64.cam.h0.0009-02-20-00000.nc , lat lon 96 144
# CPL64.cam.h1.0007-04-18-00000.nc
# LAT_15s_to_30n: 24, -14.21 : 1.89: 29.37
# LON_60e_to_180e: 49, 60:2.5:180

#=== load data
GCM_temp= SPCAM_path + 'CPL64.cam.h0.0001-01-01-00000.nc'
with Dataset(GCM_temp,'r') as D:
    lat=D.variables['lat'][:]
    lon=D.variables['lon'][:]
    lev=D.variables['lev'][:]
    ilev=D.variables['ilev'][:]

latr= lat[40:64]
lonr= lon[24:73]
maxGY= latr.size
maxGX= lonr.size
maxZ= lev.size
dp= np.diff(ilev)
# 300-700 hPa
dp[(lev>700)|(lev<300)]=0
dp_sum= np.sum(dp)
dp2 = np.reshape(dp,[dp.size,1,1])
dp2= np.tile(dp2, [1, maxGY, maxGX])

data_all= np.zeros((year_num, 365, maxGY, maxGX)) #all data(year, Julian_day, Z, Y, X)
RH_all= np.zeros((year_num, 365, maxZ, maxGY, maxGX)) #all data(year, Julian_day, Z, Y, X)
for year in years:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Year ',str(year),", Current Time =", current_time)
    # numbers of days in each months
    day_num= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for mon in np.arange(0,12,1):
        Nday= day_num[mon]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print('    Month ',str(mon+1),", Current Time =", current_time)
        for day in np.arange(0,Nday,1):
            cur_date= str(year).zfill(4)+'-'+str(mon+1).zfill(2)+'-'+str(day+1).zfill(2)
            cur_day= np.sum(day_num[0:mon])+day # Julian day, 0:364
            CRM_file= SPCAM_path+'CPL64.cam.h0.'+cur_date+'-00000.nc'
            with Dataset(CRM_file,'r') as D:
                Q= D.variables['Q'][:, :, 40:64, 24:73]
                Q= np.squeeze(np.mean(Q,0))
                T= D.variables['T'][:, :, 40:64, 24:73]
                T= np.squeeze(np.mean(T,0))
                P= D.variables['PRES'][:, :, 40:64, 24:73]
                P= np.squeeze(np.mean(P,0))
                P=P/100 # hPa => Pa
                ws= q_sat(T,P)
                RH= Q / ws
                # weighted mean
                RH_vm= np.sum(RH*dp2,0)/dp_sum
            RH_all[year-years[0], int(cur_day), :, : ,:]= RH
            data_all[year-years[0], int(cur_day), : ,:]= RH_vm

filesave= '/data/cloud/Goldtimes5/data/SPCAM/CPL64/RHmid.pk'
with open(filesave, 'wb') as fs:
     pickle.dump(data_all, fs, protocol = 4)

filesave= '/data/cloud/Goldtimes5/data/SPCAM/CPL64/RH.pk'
with open(filesave, 'wb') as fs:
     pickle.dump(RH_all, fs, protocol = 4)
