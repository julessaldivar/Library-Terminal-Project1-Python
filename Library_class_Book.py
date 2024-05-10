# import datatime so we can set 2 week due date
import datetime


# create book class with title, author, status , condition and due date if checked out
class Book:
    def __init__(self, title, author, status="On Shelf", condition=100, due_date=None):
        self.title = title
        self.author = author
        self.status = status
        self.condition = condition
        self.due_date = due_date

    # methods
    def check_out(self):
        if self.status == "On Shelf":
            self.status = "Checked out"
            self.due_date = datetime.date.today() + (datetime.timedelta(days=14))
            # self.condition()
            print(
                f"Book '{self.title}' by {self.author} has been successfully checked out, and is due back {self.due_date}")
        else:
            print(f"Sorry, {self.title} is already checked out.")

    def return_book(self):
        # update status from checked out to on shelf
        if self.status == "Checked out":
            self.status = "On Shelf"
            # reverts return date to none
            self.due_date = None
            if self.condition > 0:
                self.condition -= 50
                print(
                    f"The condition of the book '{self.title}' by {self.author} has been damaged to {self.condition}%.")
                if self.condition <= 0:
                    print(
                        f"The condition of the book '{self.title}' by {self.author} is too damaged.\n"
                        f" It will be recycled <3.")
                    self.status = "Recycled"
            else:
                print(
                    f"The condition of the book '{self.title}' by {self.author} is too damaged. It will be recycled <3.")
                self.status = "Recycled"

            print(f"Book '{self.title}' by {self.author} was successfully returned.")

        else:
            print("This book is not currently checked out. Maybe you are at the wrong library?")


# create list of books
book_list = [
    Book("The Great Gatsby", "F. Scott Fitzgerald"),
    Book("Animal Farm", "George Orwell"),
    Book("The Fellowship of the Ring", "J.R.R. Tolkien"),
    Book("Pride and Prejudice", "Jane Austen"),
    Book("Don Quixote", "Miguel de Cervantes"),
    Book("Treasure Island", "Robert Louis Stevenson"),
    Book("The Scarlet Letter", "Nathaniel Hawthorne"),
    Book("Little Women", "Louisa May Alcott"),
    Book("A Tale of Two Cities", "Charles Dickens"),
    Book("Crime and Punishment", "Fyodor Dostoyevsky"),
    Book("Frankenstein, or, the Modern Prometheus", "Mary Shelley"),
    Book("The Return of the King", "J.R.R. Tolkien"),
    Book("The Two Towers", "J.R.R. Tolkien")

]
