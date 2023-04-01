import matplotlib.pyplot as plt
from numpy import arange, sin, pi
 
import os.path
if os.path.isfile("graf.txt"):
    with open("graf.txt","r") as myjob:
        for line in myjob:
            a,b,c = line.split()
else:
    with open("graf.txt", "w+") as h:
        h.write(input())
    with open("graf.txt","r") as y:
        for line in y:
            a,b,c = line.split()
            
t = arange(float(a), float(b), float(c)) 
fig = plt.figure(1)  
w = 2*pi 
plt.plot(t, sin(w * t), 'm--')  
plt.axis([float(a), float(b), -1,1])  
plt.title('sin(x)')
plt.savefig('sin.svg')
plt.show()

