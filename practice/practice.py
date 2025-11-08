class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        a=self.length*self.breadth
        return a
    def perimiter(self):
        p=2*(self.length+self.breadth)
        return p
    def display(self):
        print("The area of a Reactangle is : ",self.area())
        print("The perimeter of a rectangle is :",self.perimiter())

value=Rectangle(10,5)
value.display()

        