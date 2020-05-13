import math

class Circle2D:

    def __init__(self, x):
        self.__rad = x
        
    @property
    def x(self):
        return self.__rad
    
    @x.setter
    def x(self, x):
        self.__rad = x
    
    def computeArea(self):
        return math.pi*self.__rad**2

    def computeCircumference(self):
        return 2*math.pi*self.__rad

class Circle3D(Circle2D):
    def __init__(self,r,col):
        Circle2D.__init__(self,r)
        self.__color = col

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,col):
        self.__color = col

    def sphereVolume(self): 
        return 4/3*(math.pi*self._Circle2D__rad)**3

print('start')
b1 = Circle2D(4)
print('1 ', b1.computeCircumference())
b1.rad = 3
print('2 ', b1.computeCircumference())
print('3 ', b1.computeArea())
b2 = Circle3D(2,'Yellow')
print(b2.color)
print('4 ',b2.sphereVolume())