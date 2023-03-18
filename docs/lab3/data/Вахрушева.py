import os.path
if os.path.isfile("data/app.conf"):
    with open("data/app.conf","r") as myjob:
        for line in myjob:
            a,b,c = line.split()
else:
    with open("data/app.conf", "w+") as h:
        h.write(input())
    with open("data/app.conf","r") as y:
        for line in y:
            a,b,c = line.split()
s=[]
for i in range(0, int(a)):
    g=int(b)*i+int(c)
    s.insert(i, g)
with open("data/result.dat","w+") as myjob2:
    myjob2.write(' '.join(map(str, s)))
    


    

