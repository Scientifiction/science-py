from pylib import *
listm=["I","Fraction","Det","Matrix"]
def add(a,b):
    if a==None:
        return b
    elif b==None:
        return a
    elif indexOf(listm,a.typem)!=-1:
        if sattrin(b,"typem") and indexOf(listm,b.typem)>indexOf(listm,a.typem):
            return b.add(a)
        else:
            return a.add(b)
    elif indexOf(listm,b.typem)!=-1:
        return b.add(a)
    else:
        return a+b
def reduce(a,b):
    if indexOf(listm,a.typem)!=-1:
        if sattrin(b,"typem") and indexOf(listm,b.typem)>indexOf(listm,a.typem):
            return b.bereduced(a)
        else:
            return a.reduce(b)
    elif indexOf(listm,b.typem)!=-1:
        return b.bereduced(a)
    else:
        return a-b

def mult(a,b):
    if indexOf(listm,a.typem)!=-1:
        if sattrin(b,"typem") and indexOf(listm,b.typem)>indexOf(listm,a.typem):
            return b.mult(a)
        else:
            return a.mult(b)
    elif indexOf(listm,b.typem)!=-1:
        return b.mult(a)
    else:
        return a*b


def divide(a,b,k=0):
    if indexOf(listm,a.typem)!=-1:
        if sattrin(b,"typem") and indexOf(listm,b.typem)>indexOf(listm,a.typem):
            return b.bedivided(a)
        else:
            return a.divide(b)
    elif indexOf(listm,b.typem)!=-1:
        return b.bedivided(a)
    elif k:
        return a/b
    else:
        return a/b#new Fraction(a,b)

# const Fraction=require("./Fraction")