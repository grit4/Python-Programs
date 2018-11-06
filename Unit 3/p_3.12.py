class quadratic:
    def __init__(self,p,q,r):
        self.a=p 
        self.b=q 
        self.c=r 
    def geta(self):
        return self.a 
    def getb(self):
        return self.b 
    def getc(self):
        return self.c 
    def getDiscriminant(self):
        return (self.b**2)-(4*self.a*self.c)
    def getRoot1(self):
        return (-self.b+(self.getDiscriminant()**0.5))/(2*self.a) 
    def getRoot2(self):
        return (-self.b-(self.getDiscriminant()**0.5))/(2*self.a)


q=quadratic(1,-4,4)
if(q.getDiscriminant()>0):
    print("Root 1 : ",q.getRoot1())
    print("Root 2 : ",q.getRoot2())
elif(q.getDiscriminant()==0):
    print("Roots are equal")
    print("Root : ",q.getRoot1())
else:
    print("The equation has no roots")    
    