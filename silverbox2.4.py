#silver box

from turtle import *
import random
from math import *
import time

particles=200
size=400 #boundary box size
seconds=10000 #time
d=.05 #time step
gravityc=1000 #gravitational constant
friction=10 #percent loss in speed during collisions
dd=1/(10**200)

print("making turtles")
for i in range(particles):
    string="t"+str(i)+"=Turtle()"
    exec(string)
    string="t"+str(i)+".pu()"
    exec(string)

x=[]
y=[]
vx=[]
vy=[]
ax=[]
ay=[]
m=[]
#initiate positions and velocities
for i in range(particles):
    x.append(random.randint(-size+1,size-1))
    y.append(random.randint(-size+1,size-1))
    #string="t"+str(i)+".goto(x[i],y[i])"
    #exec(string)
    m.append(random.uniform(1,10))
    string="t"+str(i)+".shape(\"circle\")"
    exec(string)
    string="t"+str(i)+".turtlesize(.1*m[i])"
    exec(string)
    vx.append(random.uniform(-10,10))
    vy.append(random.uniform(-10,10))
    ax.append(0)
    ay.append(0)


t0.color("green")
t1.color("blue")
t2.color("magenta")
t3.color("cyan")

v=(gravityc*m[1]/200**.5)

dax=0
day=0

#Uncomment to move particles to starting positions if needed
"""for i in range(particles):
        string="t"+str(i)+".goto(x[i],y[i])"
        exec(string)"""

counter=0
count=0
for t in range(seconds):
    counter+=1
    if count==0: 
        ti2=time.time()
        percenti=round(t*100/seconds,2)
    if count==100:
        percentf=t*100/seconds
        pleft=100-percentf
        deltap=percentf-percenti
        deltat=time.time()-ti2
        ti2=time.time()
        tleft=(deltat/deltap)*pleft
        mins=floor(tleft/60)
        if mins==1:
            secs=tleft%60
            print(mins," minute and ",round(secs)," seconds left")
        if mins>1:
            secs=tleft%60
            print(mins," minutes and ",round(secs)," seconds left")
        if mins==0:
            secs=tleft%60
            print(round(secs), " seconds left")
        count=0
        tf2=time.time()
        percenti=percentf
    count+=1
    for i in range (particles): #focus particle
        ax[i]=0
        ay[i]=0
        dax=0
        day=0
        for j in range(particles): #effecting particle
            if j!=i:
                v=(vx[i]**2+vy[i]**2)**.5
                #if v>=(2*gravityc*m[j])**.5:
                    #print("escape velocity reached")
                rx=(x[j]-x[i])
                ry=(y[j]-y[i])
                r=((rx)**2+(ry)**2)**.5
                dax+=(gravityc*m[j]*rx)/(r**3+dd)
                day+=(gravityc*m[j]*ry)/(r**3+dd)
                
        ax[i]+=dax
        ay[i]+=day
        vx[i]+=ax[i]*d
        vy[i]+=ay[i]*d
        x[i]+=vx[i]*d
        y[i]+=vy[i]*d
        for j in range(particles):
            if j!=i:
                rx=(x[j]-x[i])
                ry=(y[j]-y[i])
                r=((rx)**2+(ry)**2)**.5
                #print("i:",i,"j:",j,"r:",round(r,2),"dist:",round(r-m[i],2))
                if r<=(m[j]+m[i]):
                    #collisions
                    vx[i]=((100-friction)/100)*m[j]/m[i]*vx[j]*d
                    vy[i]=((100-friction)/100)*m[j]/m[i]*vy[j]*d
                    vx[j]=.9*m[i]/m[j]*vx[i]*d
                    vy[j]=.9*m[i]/m[j]*vy[i]*d
                    rcx=1*(r-m[i]-m[j])*rx/(r+dd)
                    rcy=1*(r-m[i]-m[j])*ry/(r+dd)
                    x[i]+=rcx
                    y[i]+=rcy
                    #print("collision","rcx:",round(rcx,2),"rcy:",round(rcy,2))
        
        if x[i]>size:
            x[i]=size
            vx[i]=-vx[i]
        if x[i]<-size:
            x[i]=-size
            vx[i]=-vx[i]
        if y[i]>size:
            y[i]=size
            vy[i]=-vy[i]
        if y[i]<-size:
            y[i]=-size
            vy[i]=-vy[i]

#indent this section to move the turtles every second
for i in range(particles):
        string="t"+str(i)+".goto(x[i],y[i])"
        exec(string)    









