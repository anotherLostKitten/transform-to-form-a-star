#for parsing .obj files into graphics script
f = open("untitled.obj","r")
d = f.read().split("\n")
f.close()
v = [[f for f in l.split(" ")[1:]]for l in d if l[:2]=="v "]
fcs = [[int(f.split("/")[0])for f in l.split(" ")[1:]]for l in d if l[:2]=="f "]
txt=""
for k in fcs:
    for j in range(len(k)):
        for i in range(j):
            txt+="line\n"+" ".join([*v[k[i]-1],*v[k[j]-1]])+"\n"
f=open("boot.txt","w")
f.write(txt)
f.close()
