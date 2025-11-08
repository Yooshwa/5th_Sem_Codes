class Library:
    total_books=0
    def __init__(self,b_id,b_name):
        self.b_id=b_id
        self.b_name=b_name
        Library.total_books+=1
    
    def display(self):
        print("Book_id:",self.b_id)
        print("Book_name:",self.b_name)
    
    @classmethod
    def display_total_books(cls):
        print("The total numbers of books are:",cls.total_books)

b1=Library(101,"C++")
b2=Library(102,"Python")
b3=Library(103,"Java")

b1.display()
Library.display_total_books()