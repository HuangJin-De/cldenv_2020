PROGRAM retemp
IMPLICIT NONE

REAL, DIMENSION(144,72) :: temp

temp=1.

OPEN(10,FILE="grid_2p5d.dat",ACCESS="direct",RECL=144*72)
WRITE(10,REC=1) temp
CLOSE(10)

END PROGRAM retemp
