#62055008
import math 

class Circle2D:
    def __init__(self,r):
        self.__rad = r
    @property
    def rad(self): 
        return self.__rad 
    @rad.setter 
    def rad(self, r): self.__rad = r
   

    def computerArea(self):
        return math.pi*self.__rad**2
    def computerCircumferrence(self):
        return 2* math.pi*self.__rad

class Circle3D(Circle2D):
    def __init__(self,r,col): 
        super().__init__(r)
        self.__color = col 
    @property 
    def color(self): 
            return self.__color 
    @color.setter 
    def color(self, col):
            self.__color = col
    def spehereVolume(self):
        return 4/3 * math.pi* b2.rad**3


c1 = Circle2D(4)
print('1','=',c1.rad)
c1.rad = 5
print('2','=',c1.rad)
print('3','=',c1.computerArea())
print('4','=',c1.computerCircumferrence())
b2 = Circle3D(2,'red')
print('5','=',b2.color)
b2.color = 'Black'
print('6','=',b2.color)
print('7','=',b2.spehereVolume())