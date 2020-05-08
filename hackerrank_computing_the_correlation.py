import math
n=int(input())
x=0
y=0
xx=0
yy=0
z=0
zz=0
xy=0
yz=0
xz=0

for i in range(n):
    row=list(map(int,input().split()))
    x+=row[0]
    y+=row[1]
    z+=row[2]
    xx+=(row[0]**2)
    yy+=(row[1]**2)
    zz+=(row[2]**2)
    xy+=(row[0]*row[1])
    yz+=(row[1]*row[2])
    xz+=(row[0]*row[2])
MpUp=(n*xy)-(x*y)
MpDown=math.sqrt((n*xx)-(x*x))*(math.sqrt((n*yy)-(y*y)))
MpUp=MpUp/MpDown
PCUp=(n*yz)-(y*z)
PcDown=math.sqrt((n*yy)-(y*y))*(math.sqrt((n*zz)-(z*z)))
PCUp=PCUp/PcDown
McUp=(n*xz)-(x*z)
McDown=math.sqrt((n*xx)-(x*x))*(math.sqrt((n*zz)-(z*z)))
McUp=McUp/McDown
print(round(MpUp,2))
print(round(PCUp,2))
print(round(McUp,2))
