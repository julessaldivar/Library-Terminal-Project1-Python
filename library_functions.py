# Here are all the functions required to run the library
from prettytable import PrettyTable


def checkout(list):
    checkout_y_or_n = input('Would you like to checkout one of these books (y/n)? ')
    if checkout_y_or_n == 'y':
        num = input('Which number would you like? ')
        for book in list:
            if book.number == num:
                this_one = list[int(num)-1]
                this_one.check_out()
        if int(num) > len(list) or int(num) < 0:
            print(f"I'm sorry that book isn't in our library.")

def return_a_book(list, num):
    for book in list:
        if book.number == num:
            book.return_book()
            return
    else:
        print("Book was not found in the library.")

#Display the entire list of books. Format it nicely.
def display_books(list):
    display= PrettyTable(['Number' ,'Title', "Author", 'Status'])
    for book in list:
       display.add_row([book.number, book.title, book.author, book.status])
    print(display)

# Search for a book by author.
def search_by_author(list):
    print(f'We would be happy to help you search for a book!')
    desired_author= str(input("Please enter the author's name: "))
    print(f'We have the following books that may interest you:')
    book_options = PrettyTable(['Number','Title', "Author",'Status'])
    for book in list:
        author=book.author
        if author.find(desired_author) >= 0:
            book_options.add_row([book.number, book.title, book.author, book.status])
        else:
            continue
    print(book_options)



# Search for a book by title keyword.
def search_title(list):
    keyword=str(input('Please enter the keyword you would like to search: '))
    print('Results are as follows:')
    keyword_results = PrettyTable(['Number','Title','Author', "Status"])
    for book in list:
        title=book.title
        if title.find(keyword) >= 0:
            keyword_results.add_row([book.number, title ,book.author, book.status])
            # Try to print out something if no keywords are found
        else:
            continue
    print(keyword_results)