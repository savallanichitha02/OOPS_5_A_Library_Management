


class Book:
    def __init__(self, book_id, title, author):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

        pass

    def mark_borrowed(self):

        self.available = False

        pass

    def mark_returned(self):

        self.available = True

        pass

    def __str__(self):

        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} (ID: {self.book_id}, Status: {status})"
     
    def __repr__(self):
        return self.__str__()