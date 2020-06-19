"reinit"
"set display color white"
"c"

"set lwid 13 5.5"
"set lwid 14 8.0"
"set annot 1 14"
"set strsiz 0.19"
"set xlopts 1 14 0.19"
"set ylopts 1 14 0.19"
"set clopts 1 14 0.19"
"set rgb 200 100 100 100 220"
"set grid on 3 200 6"

run="interim"
"open joint.ctl"

"set mproj off"

* pdf and cs
"set grads off"
"set parea 1.5 9.5 1.2 7.5"
"color -7 -2 0.5  -kind white->p31->p32->p33->p34->p35->p36->p37->p38->p39->p310->p311"
"set gxout grfill"
"d log10(f)"
"xcbar 9.6 9.7 2.2 6.5 -fs 2 -fw 0.14 -fh 0.14 -ft 14"
"set gxout contour"
"set ccolor 1"
"set cthick 13"
"set clevs 0.0001 0.0005 0.001 0.0015 0.002"
"set clab masked"
"d cs"
"draw xlab column relative humidity (%)"
"draw ylab OLR (W m`a-2`n)"
"draw title LOG10(PDF) and convective system"
"printim "run"_joint_cs.png x2048 y1536"
"c"

* pdf and ncs
"set grads off"
"set parea 1.5 9.5 1.2 7.5"
"color -7 -2 0.5  -kind white->p31->p32->p33->p34->p35->p36->p37->p38->p39->p310->p311"
"set gxout grfill"
"d log10(f)"
"xcbar 9.6 9.7 2.2 6.5 -fs 2 -fw 0.14 -fh 0.14 -ft 14"
"set gxout contour"
"set ccolor 1"
"set cthick 13"
"set clevs 0.0001 0.0005 0.001 0.0015 0.002"
"set clab masked"
"d ncs"
"draw xlab column relative humidity (%)"
"draw ylab OLR (W m`a-2`n)"
"draw title LOG10(PDF) and non-convective system"
"printim "run"_joint_ncs.png x2048 y1536"
"c"

* pdf and cs
"set grads off"
"set parea 1.5 9.5 1.2 7.5"
"color 100 2000 100 -kind white->p31->p32->p33->p34->p35->p36->p38->p39->p310->p311"
"set gxout grfill"
"d hs"
"xcbar 9.6 9.7 2.2 6.5 -fs 2 -fw 0.14 -fh 0.14 -ft 14"
"set gxout contour"
"set ccolor 1"
"set cthick 13"
"set clevs 0.0001 0.0005 0.001 0.0015 0.002"
"set clab masked"
"d cs"
"draw xlab column relative humidity (%)"
"draw ylab OLR (W m`a-2`n)"
"draw title LOG10(PDF) and CS scale"
"printim "run"_joint_hs.png x2048 y1536"
"c"

* pdf and cs
"set grads off"
"set parea 1.5 9.5 1.2 7.5"
"color 6000 18000 500 -kind white->p31->p32->p33->p34->p35->p36->p38->p39->p310->p311"
"set gxout grfill"
"d ct"
"xcbar 9.6 9.7 2.2 6.5 -fs 4 -fw 0.14 -fh 0.14 -ft 14"
"set gxout contour"
"set ccolor 1"
"set cthick 13"
"set clevs 0.0001 0.0005 0.001 0.0015 0.002"
"set clab masked"
"d cs"
"draw xlab column relative humidity (%)"
"draw ylab OLR (W m`a-2`n)"
"draw title LOG10(PDF) and CS top height"
"printim "run"_joint_ct.png x2048 y1536"
*"c"

*"quit"