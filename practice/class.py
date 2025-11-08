class Rectangle:
    length=0
    breadth=0
    def setrec(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length * self.breadth
    
r1=Rectangle()
r1.setrec(2,4)
print("Area of a rectangle :",r1.area())