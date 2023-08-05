import Mathm
from pylib import *
print(vars(Mathm.I(2,3).reduce(Mathm.I(4,5))))
print(Mathm.I(100,200).mult(6).tostr())
print(indexOf([0,1,2],1))
print(sattrin(Mathm.I(2,3),"typem"))
print(Mathm.O.add(Mathm.I(2,3),5).tostr())
print(Mathm.O.mult(Mathm.I(2,3),Mathm.I(1,2)).tostr())