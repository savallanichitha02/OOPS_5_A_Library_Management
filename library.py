from book import Book
from member import Member
from exceptions import BookNotFoundError, BookNotAvailableError, MemberNotFoundError

class Library:
    def __init__(self):
        self.books = {}    
        self.members = {}
        pass

    def add_book(self, book):

        self.books[book.book_id] = book
        print(f"Book added: {book.title} (ID: {book.book_id})")

        pass

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member added: {member.name} (ID: {member.member_id})")

        pass

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member ID '{member_id}' not found.")
        
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID '{book_id}' not found.")

        member = self.members[member_id]
        book = self.books[book_id]

        if not book.available:
            raise BookNotAvailableError(f"Book '{book.title}' is already borrowed.")
        
        book.mark_borrowed()      
        member.borrow_book(book)  

        print(f"\nSUCCESS: {member.name} borrowed '{book.title}'")

        pass

    def return_book(self, member_id, book_id):

        if member_id not in self.members:
            raise MemberNotFoundError(f"Member ID '{member_id}' not found.")
        
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID '{book_id}' not found.")

        member = self.members[member_id]
        book = self.books[book_id]

        returned_book = member.return_book(book_id)
        
        if returned_book:
            book.mark_returned() 
            print(f"\nSUCCESS: {member.name} returned '{book.title}'")
        else:
            print(f"\nWARNING: Book '{book.title}' not found in {member.name}'s borrowed list.")
            
        pass
