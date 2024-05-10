# Here are all the functions required to run the library
from prettytable import PrettyTable


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
    book_options = PrettyTable(['Title', "Author"])
    for book in list:
        author=book.author
        if author.find(desired_author) >= 0:
            book_options.add_row([book.title, book.author])
        else:
            continue
    print(book_options)




# Search for a book by title keyword.
def search_title(list):
    keyword=str(input('Please enter the keyword you would like to search: '))
    print('Results are as follows:')
    keyword_results = PrettyTable(['Title','Author'])
    for book in list:
        title=book.title
        if title.find(keyword) >= 0:
            keyword_results.add_row([title,book.author])
            # Try to print out something if no keywords are found
        else:
            continue
    print(keyword_results)