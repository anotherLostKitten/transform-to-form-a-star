from math import cos,sin,pi
from os import remove
from subprocess import Popen,PIPE
class Img:
    def __init__(self,r,c,p=[]):
        self.c=c
        self.r=r
        self.img=[0]*r*c
        for i in range(0,len(p),8):
            self.ln(round(p[i]/p[i+3])+250,round(p[i+1]/p[i+3])+250,round(p[i+4]/p[i+7])+250,round(p[i+5]/p[i+7])+250,16741235)
    def s(self,r,c,v):
        if-1<r<self.r and-1<c<self.c:
            self.img[c+r*self.c]=v
    def ln(self,rs,cs,rf,cf,v):
        dr=abs(rf-rs)
        dc=abs(cf-cs)
        if rs>rf if dr<dc else cs>cf:
            self.ln(rf,cf,rs,cs,v)
        elif dr<dc:
            rr=2*dr-dc
            for c in range(cs,cf-1 if cs>cf else cf+1,-1 if cs>cf else 1):
                self.s(rs,c,v)
                rs+=1 if rr>0 else 0
                rr+=2*dr-2*dc if rr>0 else 2*dr
        else:
            rr=2*dc-dr
            for r in range(rs,rf-1 if rs>rf else rf+1,-1 if rs>rf else 1):
                self.s(r,cs,v)
                cs+=1 if rr>0 else 0
                rr+=2*dc-2*dr if rr>0 else 2*dc
    def __str__(self):
        return"P3 "+str(self.c)+" "+str(self.r)+" 255\n"+" ".join(str(round(i/65536))+" "+str(round(i/256)%256)+" "+str(i%256) for i in self.img)
class Etrx:
    def __init__(self,m=[]):
        self.m=m[:]
    def e(self,s,f):
        self.m+=(*s,1,*f,1)
    def __str__(self):
        return"\n".join(" ".join(("  "if i<10 else" "if i<100 else"")+str(i) for i in self.m[j::4]) for j in range(4))+"\n"
    def x(self,m):
        self.m=[sum(float(m[i%4+k*4])*self.m[i-(i%4)+k]for k in range(4))for i in range(len(self.m))]
    def idm(self,e=None):
        self.m=tuple(1.0 if i==j else 0.0 for j in range(4)for i in range(4))
def cmd(m,edgm,filename):
    [{"ident":(lambda:m.idm()),"line":(lambda:edgm.e([float(i)for i in b[1][:3]],[float(i)for i in b[1][3:]])),"scale":(lambda:m.x((float(b[1][0]),0,0,0,0,float(b[1][1]),0,0,0,0,float(b[1][2]),0,0,0,0,1))),"move":(lambda:m.x((1,0,0,0,0,1,0,0,0,0,1,0,float(b[1][0]),float(b[1][1]),float(b[1][2]),1))),"rotate":(lambda:m.x({"x":(1,0,0,0,0,cos(float(b[1][1])/180*pi),sin(float(b[1][1])/-180*pi),0,0,sin(float(b[1][1])/180*pi),cos(float(b[1][1])/180*pi),0,0,0,0,1),"y":(cos(float(b[1][1])/180*pi),0,sin(float(b[1][1])/180*pi),0,0,1,0,0,sin(float(b[1][1])/-180*pi),0,cos(float(b[1][1])/180*pi),0,0,0,0,1),"z":(cos(float(b[1][1])/180*pi),sin(float(b[1][1])/-180*pi),0,0,sin(float(b[1][1])/180*pi),cos(float(b[1][1])/180*pi),0,0,0,0,1,0,0,0,0,1)}[b[1][0]])),"project":(lambda:m.x((1,0,0,0,0,1,0,0,0,0,0,0,0,0,1/float(b[1][0]),1))),"apply":(lambda:[edgm.x(m.m),m.idm()]),"display":(lambda:[open("temp.ppm","w+").write(str(Img(500,500,edgm.m))),Popen(("display","temp.ppm"),stdin=PIPE,stdout=PIPE,stderr=PIPE).communicate(),remove("temp.ppm")]),"save":(lambda:open(b[1][0],"w+").write(str(Img(500,500,edgm.m))))}[b[0]]()for b in[(e[0],(*tuple(k.split(" ")for k in open(filename,"r").read().split("\n")if k and k[0]!="#"),[])[i+1])for(i,e)in enumerate(k.split(" ")for k in open(filename,"r").read().split("\n")if k and k[0]!="#")if e and e[0]in("ident","line","scale","move","rotate","project","apply","display","save")]]
if __name__ == "__main__":
    cmd(Etrx(),Etrx(),"boot.txt")
