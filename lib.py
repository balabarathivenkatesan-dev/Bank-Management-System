class Book:
    def __init__(self,book_id,title,author,available=True):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.available=True
    
    def display_books(self):
        print("Book ID: ",self.book_id)
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Available: ",self.available)

class Member:
    def __init__(self,member_id,name,borrowed_books=[]):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]
        
    def display_member(self):
        print("Member ID: ",self.member_id)
        print("name: ",self.name)
        print("Borrowed books: ",self.borrowed_books)
            
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
        
    def add_books(self,book):
        self.books.append(book)
        print("Book added successfully")
    
    def add_member(self,member):
        self.members.append(member)
        print("Member added successfully")
        
    def show_available_books(self):
        print("Available Books")
        for book in self.books:
            if book.available:
                book.display_books
                print("-----------")
                
    def borrow_book(self,member_id,book_id):
        member=None
        book=None
        
        for m in self.members:
            if m.member_id==member_id:
                member=m
                break
            
        for b in self.books:
            if b.book_id==book_id:
                book=b
                break
        
        if member and book:
            if book.available:
                book.available=False
                member.borrowed_books.append(book)
                print("Book borrowed successfully")
            else:
                print("Book is not available")
        else:
            print("Invalid member or book ID")
            
    def return_book(self,member_id,book_id):
        for member in self.members:
            if member.member_id==member_id:
                for book in member.borrowed_books:
                    if book.book_id==book_id:
                        member.borrowed_books.remove(book)
                        book.available=True
                        print("Book returned successfully")
                        return
                    
        print("Book not found in member borrowed list")
                        
library = Library()

book1 = Book(1, "Python Basics", "Guido")
book2=Book(2,"Java","bala")
member1 = Member(101, "Arun")

library.add_books(book1)
library.add_member(member1)

# library.borrow_book(101,1)

library.show_available_books()

# library.return_book(101,1)