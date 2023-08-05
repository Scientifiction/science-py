from pylib import *
class I:
    a = None
    b = None
    typem=None
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.typem="I"
    def conjugate(self):
        return I(self.a,-self.b)
    def add(self,n):
        if sattrin(n,"typem"):
            if n.typem=="I":
                return I(self.a+n.a,self.b+n.b)
        return I(self.a+n,self.b)
    def reduce(self,n):
        if sattrin(n,"typem"):
            if n.typem=="I":
                return I(self.a-n.a,self.b-n.b)
        return I(self.a-n,self.b)
    def mult(self,n):
        if sattrin(n,"typem"):
                if n.typem=="I":
                    return I(self.a*n.a-self.b*n.b,self.b*n.a+self.a*n.b)
        else:
            return I(self.a*n,self.b*n)
    def divide(self,n):
        if sattrin(n,"typem") and n.b!=0 and n.typem=="I":
            return self.mult(n.conjugate()).divide(n.mult(n.conjugate()))
        else:
            return I(self.a/n,self.b/n)
    def tostr(self):
        if(self.b>0):
            return str(self.a)+"+"+str(self.b)+"i"
        else:
            return str(self.a)+""+str(self.b)+"i"
