# import datatime so we can set 2 week due date
import datetime


# add media as the parent class
class Media:
    def __init__(self, number, title, status="On Shelf", condition=100, due_date=None):
        self.number = number
        self.title = title
        self.status = status
        self.condition = condition
        self.due_date = due_date

    def check_out(self):
        if self.status == "On Shelf":
            self.status = "Checked Out"
            self.due_date = datetime.date.today() + datetime.timedelta(weeks=2)
            self.condition -= 20
            print(f"'{self.title}' has been successfully checked out, and is due back {self.due_date}")
        else:
            print(f"Sorry, '{self.title}' is already checked out.")

    def return_media(self):
        if self.status == "Checked Out":
            if self.condition <= 0:
                print(f"The condition of '{self.title}' is too damaged. It will be recycled.")
                self.status = "Recycled"
            else:
                self.status = "On Shelf"
                self.due_date = None
                print(f"'{self.title}' was successfully returned.")
        else:
            print("This item is not currently checked out.")


# Book class is now a child class of Media
class Book(Media):  # add author as new parameter
    def __init__(self, number, title, author, status="On Shelf", condition=100, due_date=None):
        super().__init__(number, title, status, condition, due_date)
        self.author = author

    # override the checkout for books to add author
    def check_out(self):
        if self.status == "On Shelf":
            self.status = "Checked Out"
            self.due_date = datetime.date.today() + datetime.timedelta(weeks=2)
            self.condition -= 20
            print(
                f"Book '{self.title}' by {self.author} has been successfully checked out, and is due back {self.due_date}")
        else:
            print(f"Sorry, '{self.title}' is already checked out.")

    # override return for books to add author
    def return_media(self):
        if self.status == "Checked Out":
            if self.condition <= 0:
                print(f"The condition of the book '{self.title}' by {self.author} is too damaged. It will be recycled.")
                self.status = "Recycled"
            else:
                self.status = "On Shelf"
                self.due_date = None
                print(f"Book '{self.title}' by {self.author}' was successfully returned.")
        else:
            print("This book is not currently checked out.")


# Adding Movie as a child class of Media
class Movie(Media):  # add director as new parameter
    def __init__(self, number, title, director, status="On Shelf", condition=100, due_date=None):
        super().__init__(number, title, status, condition, due_date)
        self.director = director

    # override the checkout for Movie to add director
    def check_out(self):
        if self.status == "On Shelf":
            self.status = "Checked Out"
            self.due_date = datetime.date.today() + datetime.timedelta(weeks=2)
            self.condition -= 20
            print(
                f"Movie '{self.title}' by {self.director} has been successfully checked out, and is due back {self.due_date}")
        else:
            print(f"Sorry, '{self.title}' is already checked out.")

    # override return for Movie to add director
    def return_media(self):
        if self.status == "Checked Out":
            if self.condition <= 0:
                print(
                    f"The condition of the movie '{self.title}' by {self.director} is too damaged. It will be recycled.")
                self.status = "Recycled"
            else:
                self.status = "On Shelf"
                self.due_date = None
                print(f"Movie '{self.title}' by {self.director}' was successfully returned.")
        else:
            print("This movie is not currently checked out.")


media_list = [
    Book("1", "The Great Gatsby", "F. Scott Fitzgerald"),
    Book("2", "Animal Farm", "George Orwell"),
    Book("3", "The Fellowship of the Ring", "J.R.R. Tolkien"),
    Book("4", "Pride and Prejudice", "Jane Austen"),
    Book("5", "Don Quixote", "Miguel de Cervantes"),
    Book("6", "Treasure Island", "Robert Louis Stevenson"),
    Book("7", "The Scarlet Letter", "Nathaniel Hawthorne"),
    Book("8", "Little Women", "Louisa May Alcott"),
    Book("9", "A Tale of Two Cities", "Charles Dickens"),
    Book("10", "Crime and Punishment", "Fyodor Dostoyevsky"),
    Book("11", "Frankenstein", "Mary Shelley"),
    Book("12", "The Return of the King", "J.R.R. Tolkien"),
    Book("13", "The Two Towers", "J.R.R. Tolkien"),
    Book("14", "The Shining", "Stephen King"),
    Movie("15", "Maximum Overdrive", "Stephen King"),
    Movie("16", "Love Lies Bleeding", "Rose Glass"),
    Movie("17", "Edward Scissorhands", "Tim Burton"),
    Movie("18", "Fight Club", "David Fincher"),
    Movie("19", "The Lord of the Rings: The Fellowship of the Ring", "Peter Jackson"),
    Movie("20", "The Great Gatsby", "Baz Luhrmann")
]
