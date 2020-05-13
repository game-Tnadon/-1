import math
class Circcle2D:
    def _init_(sel,r)
        self.rad = r
    @property
    def rad (self):
        return self.__rad
    @rad.setter
    def rad(self,x)

    def computArea(self)
        return  math.pi *self.__rad**2

#print (Start)
c1 =Circcle2D(4)
print (c1.rad)
c1.rad = 5
print (c1.rad)
print(c1.computArea)