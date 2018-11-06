import math
class circle:
    def __init__(self,x):
        self.r=x 
    def getr(self):
        return self.r 
    def area(self):
        return math.pi*self.r*self.r 
    def __add__(self,othercircle):
        return circle(self.r+othercircle.r)
    
c1=circle(10)
c2=circle(20)
c3=c1+c2
print("Circle 1 radius : ",c1.r)
print("Circle 2 radius : ",c2.r)
print("Circle 3 radius : ",c3.r)
