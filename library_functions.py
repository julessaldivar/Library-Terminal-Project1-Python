# Here are all the functions required to run the library
from prettytable import PrettyTable
from Library_class_Media import Book
from Library_class_Media import Media
from Library_class_Media import Movie
from Library_class_Media import media_list


def checkout(list):
    checkout_y_or_n = input('Would you like to checkout one of these items (y/n)? ')
    if checkout_y_or_n == 'y':
        num = input('Which number would you like? ')
        for item in list:
            if item.number == num:
                this_one = list[int(num)-1]
                this_one.check_out()
        if int(num) > len(list) or int(num) < 0:
            print(f"I'm sorry that item isn't in our library.")


def return_an_item(list, num):
    for item in list:
        if item.number == num:
            item.return_media()
            return
    else:
        print("Item was not found in the library.")


# Display the entire list of books. Format it nicely.
def display_books(list):
    display = PrettyTable(['Number', 'Title', "Book Author", "Movie Director", 'Status'])
    for item in list:
        if isinstance(item, Book):
            display.add_row([item.number, item.title, item.author, ' ', item.status])
        elif isinstance(item, Movie):
            display.add_row([item.number, item.title, ' ', item.director, item.status])
    print(display)


# Search for a book by author. #############################################
def search_by_author(list):
    print(f'We would be happy to help you search!')
    desired_author_director = input("Please enter the author/director name: ").lower()

    media_options = PrettyTable(['Number', 'Title', "Book Author", "Movie Director", 'Status'])
    found_media = 0

    for item in list:
        if isinstance(item, Book):
            author = item.author.lower()
            if author.find(desired_author_director) >= 0:
                media_options.add_row([item.number, item.title, item.author, ' ', item.status])
                found_media += 1
        elif isinstance(item, Movie):
            director = item.director.lower()
            if director.find(desired_author_director) >= 0:
                media_options.add_row([item.number, item.title, ' ', item.director, item.status])
                found_media += 1
            else:
                continue

    if found_media == 0:
        print(f"I'm sorry we didn't find any media from your search.")
    else:
        print(f'We have the following items that may interest you:')
        print(media_options)
        checkout(media_list)


# Search for a book by title keyword. ###################################
def search_title(list):
    keyword = str(input('Please enter the keyword you would like to search: ')).lower()
    keyword_results = PrettyTable(['Number', 'Title', 'Book Author', 'Movie Director', "Status"])
    found_media = 0

    for item in list:
        title = item.title.lower()
        if title.find(keyword) >= 0:
            if isinstance(item, Book):
                keyword_results.add_row([item.number, item.title, item.author, ' ', item.status])
            elif isinstance(item, Movie):
                keyword_results.add_row([item.number, item.title, ' ', item.director, item.status])
            found_media += 1
        else:
            continue

    if found_media == 0:
        print(f"I'm sorry we didn't find any media from your search.")
    else:
        print(f'We have the following media that may interest you:')
        print(keyword_results)
        checkout(media_list)


def add_book(list):
    print(f'Excellent, you would like to add a book to the library!')

    index = str(len(list) + 1)
    new_book_title = input('What is the title of the new book? ')
    new_book_author = input('Who is the author of the new book? ')
    new_book = Book(index, new_book_title, new_book_author)
    list.append(new_book)
    print(f"Great! You've added {new_book.title} by {new_book.author} to the library. We appreciate your donation.")


def add_movie(list):
    print(f'Excellent, you would like to add a movie to the library!')

    index = str(len(list) + 1)
    new_movie_title = input('What is the title of the new movie? ')
    new_movie_director = input('Who is the director of the new movie? ')
    new_movie = Movie(index, new_movie_title, new_movie_director)
    list.append(new_movie)
    print(f"Great! You've added {new_movie.title} directed by {new_movie.director} to the library."
          f" We appreciate your donation.")