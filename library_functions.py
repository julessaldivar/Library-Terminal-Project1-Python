# Here are all the functions required to run the library
from prettytable import PrettyTable
from Library_class_Book import Book
from Library_class_Book import book_list

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

# Display the entire list of books. Format it nicely.
def display_books(list):
    display= PrettyTable(['Number' ,'Title', "Author", 'Status'])
    for book in list:
       display.add_row([book.number, book.title, book.author, book.status])
    print(display)

# Search for a book by author.
def search_by_author(list):
    print(f'We would be happy to help you search for a book!')
    desired_author= input("Please enter the author's name: ")
    book_options = PrettyTable(['Number','Title', "Author",'Status'])
    found_media = 0

    for book in list:
        author=book.author
        if author.find(desired_author) >= 0:
            book_options.add_row([book.number, book.title, book.author, book.status])
            found_media += 1
        else:
            continue

    if found_media == 0:
        print(f"I'm sorry we didn't find any media from your search.")
    else:
        print(f'We have the following books that may interest you:')
        print(book_options)
        checkout(book_list)




# Search for a book by title keyword.
def search_title(list):
    keyword=str(input('Please enter the keyword you would like to search: '))
    keyword_results = PrettyTable(['Number','Title','Author', "Status"])
    found_media = 0

    for book in list:
        title = book.title
        if title.find(keyword) >= 0:
            keyword_results.add_row([book.number, title ,book.author, book.status])
            found_media += 1
        else:
            continue

    if found_media == 0:
        print(f"I'm sorry we didn't find any media from your search.")
    else:
        print(f'We have the following books that may interest you:')
        print(keyword_results)
        checkout(book_list)


def add_book(list):
    print(f'Excellent, you would like to add a book to the library!')

    index = str(len(list) + 1)
    new_book_title =  input('What is the title of the new book? ')
    new_book_author = input('What is the author of the new book? ')
    new_book = Book(index, new_book_title, new_book_author)
    list.append(new_book)
    print(f"Great! You've added {new_book.title} by {new_book.author} to the library. We appreciate your donation.")
