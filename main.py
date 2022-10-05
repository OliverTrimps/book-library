class Library:
    def __init__(self):
        self.shelf = {}

    def add_book(self, book_name, book_rating):
        book_shelf = {}
        if book_name not in self.shelf:
            book_shelf[book_name] = book_rating
            self.shelf[book_name] = book_shelf
            return "Added!"
        else:
            return f"{book_name} already exist"

    def change_book_rating(self, book_name, book_rating):
        if book_name not in self.shelf:
            return "Book not found"
        else:
            self.shelf[book_name][book_name] = book_rating
            return "Updated!"

    def get_all_books(self):
        return self.shelf.values()

    def delete_book(self, book_name):
        if book_name in self.shelf:
            del self.shelf[book_name]
            return "Deleted!"
        else:
            return "Book not found!"

    def get_book_by_name(self, book_name):
        if book_name in self.shelf:
            return self.shelf[book_name]
        else:
            return "Book not found!"

    def get_books_by_rating(self, book_rating):
        books_by_rating = {}
        book_rating_to_show = {}
        for book in self.shelf.values():
            books_by_rating.update(book)
            if book_rating in book.values():
                book_rating_to_show.update(book)
        if book_rating not in books_by_rating.values():
            return "No book has this rating!"
        else:
            return book_rating_to_show


library = Library()
is_running = True

while is_running:
    option = input("A(Add Book), B(Change Book Rating), C(Get All Books), D(Delete), "
                   "E(Get Book By Name), F(Get Books By Rating), END(Stop!): ").upper()
    if option == "A":
        name = input("Name: ").title()
        rating = float(input("Rating: "))
        print(library.add_book(name, rating))
    elif option == "B":
        name = input("Name: ").title()
        rating = float(input("Rating: "))
        print(library.change_book_rating(name, rating))
    elif option == "C":
        print(library.get_all_books())
    elif option == "D":
        name = input("Name: ").title()
        print(library.delete_book(name))
    elif option == "E":
        name = input("Name: ").title()
        print(library.get_book_by_name(name))
    elif option == "F":
        rating = float(input("Rating: "))
        print(library.get_books_by_rating(rating))
    elif option == "END":
        is_running = False
