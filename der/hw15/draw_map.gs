"reinit"
"set display color white"
"c"

"set lwid 13 8.5"
"set lwid 14 14.0"
"set annot 1 13"
"set strsiz 0.19"
"set xlopts 1 13 0.19"
"set ylopts 1 13 0.19"
"set clopts 1 13 0.19"
"set rgb 200 100 100 100 220"
"set grid on 3 200 6"
"set map 1 1 12"

"open map.ctl"

"set lon 0 360"
"set lat -30 30"

"set grads off"
"set parea 1 10 4.3 7.3"
"set ylint 30"
"color 0 1 0.1 -kind cyan->yellow->red"
"set gxout grfill"
"d f(t=2)"
"xcbar 10.1 10.2 2 6.5 -fs 2 -ft 13 -fw 0.15 -fh 0.15 -line on"
"set string 1 l 13 0"
"set strsiz 0.18"
"draw string 10.3 2 yr`a-1`n"
"draw title El nino"

"set grads off"
"set parea 1 10 1.2 4.2"
"color 0 1 0.1 -kind cyan->yellow->red"
"set gxout grfill"
"d f(t=3)"
"draw title La nina"

"printim tc_oni.png x2048 y1536"
"c"

"set grads off"
"set parea 1 10 1 7.5"
"set ylint 30"
"color 0 1 0.1 -kind cyan->yellow->red"
"set gxout grfill"
"d f(t=1)"
"xcbar 10.1 10.2 2 6.5 -fs 2 -ft 13 -fw 0.15 -fh 0.15 -line on"
"set string 1 l 13 0"
"set strsiz 0.18"
"draw string 10.3 2 yr`a-1`n"
"printim tc_cli.png x2048 y1536"
"c"

"quit"


