# Here are all the functions required to run the library 

from prettytable import PrettyTable

#Display the entire list of books. Format it nicely.
def display_books(list):
    table.field_names=['Title', "Author"]
    for book in list:
       table.add_row([book.title, book.author])

# Search for a book by author.
def search_by_author(list):
    author_search='y'
    print(f'We would be happy to help you search for a book!')
    while author_search=='y':
        desired_author= input("Please enter the author's name: ")
        for book in list:
            if book.author == desired_author:
                print(f'We have a book by {desired_author} titled {Book}')
            # else:
            #     print(f"I'm sorry we don't have a book by that author.")
            #     author_search=input(f'Would you like to search again (y/n)?')


# Search for a book by title keyword.
def search_title(list):
    keyword=str(input('Please enter the keyword you would like to search: '))
    print('Results are as follows:')
    for book in list:
        title=book.title
        if title.find(keyword) > 0:
            print(f'{book.title}')
            # Try to print out something if no keywords are found