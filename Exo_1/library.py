#Exo1
class Person:
#1
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"



        
class Book:
#2
    def __init__(self, title: str, author: Person):
        self.title = title
        self.author = author
    def __str__(self): 
        return f"{self.title} {self.author}"


    


class LibraryError(Exception):
    #return a string with the error message
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
    def __str__(self):
        return f"LibraryError: {self.message}"
    





class Library:
#3
    _books: list[Book] = []
    _membres: set[Person] = []
    _borrowed_books: dict[Book, Person] = []

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name} {self._books} {self._membres} {self._borrowed_books}"
 #4   
    def is_book_available(self, book) -> bool:
        """Check if the book is available in the library."""
        if book not in self._books:
            # if the book is not in the library, raise an error
            raise LibraryError("Book not found in the library.")
        # return True if the book is not borrowed, else False
        return book in self._books 
#5    
    def borrow_book(self, book: Book, person: Person) -> None:
        """Borrow a book from the library."""
        if not self.is_book_available(book):
            # if the book is not available, raise an error
            raise LibraryError("Book not available for borrowing.")
        # if the book is already borrowed, raise an error
        if book in self._borrowed_books:
            raise LibraryError("Book is already borrowed.")
        #if the book is available, check if the person is a member of the library
        if person not in self._membres:
            # if the person is not a member, raise an error
            raise LibraryError("Person is not a member of the library.")
        # add the book to the borrowed books dictionary with the person as the value
        self._borrowed_books[book] = person
#6
    def return_book(self, book: Book):
        """Return a book to the library."""
        if book not in self._borrowed_books:
            # if the book is not borrowed, raise an error
            raise LibraryError("Book not borrowed")
        # remove the book from the borrowed books dictionary
        del self._borrowed_books[book]
        # add the book to the library's books list
        self._books.append(book)
#7
    def add_new_member(self, person: Person):
        """Add a new member to the library."""
        self._membres.append(person)
    def add_new_book(self, book: Book):
        """Add a new book to the library."""
        self._books.append(book)
#8
    def print_status(self):
        
        """Print the status of the library."""
        print("\n")


        print(f"Public library status:")
        print(f"Books catalogue:")
        for book in self._books: 
            print(f"- {book.title} by ({book.author.first_name} {book.author.last_name})")
            # returns the book title and author name

        print("Members:")
        for member in self._membres:
            print(f"- {member.first_name} {member.last_name}")
            # returns the member name

        print("Available books:")
        for book in self._books:
            print(f"- {book.title} by ({book.author.first_name} {book.author.last_name})")
            #returns the available book title and author name

        print("Borrowed books:")
        for book, person in self._borrowed_books:   
            print(f"- {book.title} by {book.author.first_name} {book.author.last_name} by {person.first_name} {person.last_name}")
            # returns the borrowed book title and author name with the member name
      






        



def main():
    """Test your code here"""


#9
    
antoine = Person("Antoine", "Dupont")
print(antoine)

julia = Person("Julia", "Roberts")
print(julia)

rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
print(rugby_book)

novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
print(novel_book)

library = Library("Public library")
library.print_status()

library.add_new_book(rugby_book)
library.add_new_book(novel_book)
library.add_new_member(antoine)
library.add_new_member(julia)
library.print_status()

print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
library.borrow_book(rugby_book, antoine)
library.print_status()

try:
    library.borrow_book(rugby_book, julia)
except LibraryError as error:
    print(error)

try:
    library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
except LibraryError as error:
    print(error)

try:
    library.borrow_book(novel_book, Person("Simone", "Veil"))
except LibraryError as error:
    print(error)

try:
    library.return_book(novel_book)
except LibraryError as error:
    print(error)

library.return_book(rugby_book)
library.borrow_book(novel_book, julia)
library.print_status()

library.borrow_book(rugby_book, julia)
library.print_status()




if __name__ == "__main__":
    main()






























