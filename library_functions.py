# Here are all the functions required to run the library
from prettytable import PrettyTable


def checkout():
    checkout_y_or_n = input('Would you like to checkout one of these books (y/n)? ')
    if checkout_y_or_n == 'y':
        num = input('Which number would you like? ')

        if book.status ==
        check_out()


#Display the entire list of books. Format it nicely.
def display_books(list):
    display= PrettyTable(['Title', "Author"])
    for book in list:
       display.add_row([book.title, book.author])
    print(display)

# Search for a book by author.
def search_by_author(list):
    print(f'We would be happy to help you search for a book!')
    desired_author= str(input("Please enter the author's name: "))
    print(f'We have the following books that may interest you:')
    book_options = PrettyTable(['Number','Title', "Author"])
    for book in list:
        author=book.author
        if author.find(desired_author) >= 0:
            book_options.add_row([book.number, book.title, book.author])
        else:
            continue
    print(book_options)



# Search for a book by title keyword.
def search_title(list):
    keyword=str(input('Please enter the keyword you would like to search: '))
    print('Results are as follows:')
    keyword_results = PrettyTable(['Number','Title','Author'])
    for book in list:
        title=book.title
        if title.find(keyword) >= 0:
            keyword_results.add_row([book.number, title ,book.author])
            # Try to print out something if no keywords are found
        else:
            continue
    print(keyword_results)