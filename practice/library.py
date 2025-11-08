class Library:
    total_books=0
    def add_books(self,bid,bn):
        self.book_id=bid
        self.book_name=bn
        Library.total_books+=1

    def display_books(self):
        print("Book_id: ",self.book_id)
        print("Book_name: ",self.book_name,"\n")
    
    @classmethod
    def display_total_books(cls):
        print("The total number of books are: ",cls.total_books)
    
l1=Library()
l1.add_books(1,"C++")
l1.display_books()

l2=Library()
l2.add_books(2,"Pyhton")
l2.display_books()

l3=Library()
l3.add_books(3,"Javascript")
l3.display_books()

Library.display_total_books()