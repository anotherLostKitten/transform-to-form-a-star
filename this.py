from math import cos,sin,pi
class Img:
    def __init__(self,r,c):
        self.c=c
        self.r=r
        self.img=[0 for i in range(r*c)]
    def s(self,r,c,v):
        self.img[c+r*self.c]=v
    def ln(self,rs,cs,rf,cf,v):
        dr=abs(rf-rs)
        dc=abs(cf-cs)
        if rs==rf and cs==cf:
            self.s(rs,cs,v)
        elif rs>rf if dr<dc else cs>cf:
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
        return"P3 "+str(self.c)+" "+str(self.r)+" 255\n"+" ".join(str(i/65536)+" "+str(i/256%256)+" "+str(i/256) for i in self.img)
class Etrx:
    def __init__(self,m=[]):
        self.m=m[:]
    def e(self,s,f):
        self.m+=(*s,1,*f,1)
    def __str__(self):
        return"\n".join(" ".join(("  "if i<10 else" "if i<100 else"")+str(i) for i in self.m[j::4]) for j in range(4))+"\n"
    def x(self,m):
        self.m=[sum(self.m[i-(i%4)+k]*m[i%4*4+k] for k in range(4)) for i in range(len(self.m))]
def idm(n):
    return tuple(1.0 if i==j else 0.0 for j in range(n)for i in range(n))
if __name__ == "__main__":
    a=Etrx()
    l=10.0
    for i in range(0,int(l)):
        for j in range(0,int(l*2)):
            a.e((sin(i/l*pi)*cos(j/l*pi),cos(i/l*pi),sin(i/l*pi)*sin(j/l*pi)),(sin(i/l*pi)*cos((j+1)/l*pi),cos(i/l*pi),sin(i/l*pi)*sin((j+1)/l*pi)))
            a.e((sin(i/l*pi)*cos(j/l*pi),cos(i/l*pi),sin(i/l*pi)*sin(j/l*pi)),(sin((i+1)/l*pi)*cos(j/l*pi),cos((i+1)/l*pi),sin((i+1)/l*pi)*sin(j/l*pi)))
    a.x((180.0,0.0,0.0,0.0,0.0,180.0,0.0,0.0,0.0,0.0,180.0,0.0,0.0,0.0,0.0,1.0))
    a.x((1.0,0.0,0.0,0.0,0.0,cos(pi/6),sin(pi/6),0.0,0.0,sin(pi/-6),cos(pi/6),0.0,0.0,0.0,0.0,1.0))
    a.x((cos(pi/15),0.0,sin(pi/-15),0.0,0.0,1.0,0.0,0.0,sin(pi/15),0.0,cos(pi/15),0.0,0.0,0.0,0.0,1.0))
    a.x((1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,1.0/250.0,0.0,0.0,0.0,1.0))
    img=Img(500,500)
    for i in range(0,len(a.m),8):
        img.ln(round(a.m[i]/a.m[i+3])+250,round(a.m[i+1]/a.m[i+3])+250,round(a.m[i+4]/a.m[i+7])+250,round(a.m[i+5]/a.m[i+7])+250,16741368)
    f=open("things.ppm","w")
    f.write(str(img))
    f.close()
    print("identiy matrix & matrix printing demo:",Etrx(idm(4)),"i only want this demo code to be 1 line, see image for adding edges & multiplication.",sep="\n")
