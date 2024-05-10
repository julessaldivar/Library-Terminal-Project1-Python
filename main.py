import datetime
from Library_class_Book import book_list
2

from library_functions import display_books
from library_functions import search_by_author
from library_functions import search_title

print("""Hi, Welcome to GC Library!
Please choose an option from the below list to begin:""")

valid_action=0
while valid_action == 0:
    print("""    1. Display all books
    2. Search for a book by author
    3. Search for a book by title keyword
    4. Return a book """)
    action= int(input(f'> '))

    if action == 1:  # Display all the books ###################################

        display_books(book_list)

        # Check out a book


        # Staying in the library loop or not.
        another = input(f'Would you like to complete another action (y/n)? ')
        if another == 'y':
            valid_action = 0
        else:
            break

    elif action == 2:  # Search for a book by author #############################
        search_by_author(book_list)



        # Staying in the library loop or not.
        another = input(f'Would you like to complete another action (y/n)? ')
        if another == 'y':
            valid_action = 0
        else:
            break

    elif action == 3:   # Search for a book by title keyword #######################
        search_title(book_list)


        # Staying in the library loop or not.
        another = input(f'Would you like to complete another action (y/n)? ')
        if another == 'y':
            valid_action = 0
        else:
            break

    elif action == 4:   # Return a book ##############################################
        print('Return a book')




        # Staying in the library loop or not.
        another = input(f'Would you like to complete another action (y/n)? ')
        if another == 'y':
            valid_action = 0
        else:
            break

    else:
        valid_action = 0
        print(f"I don't understand your prompt, please enter a number 1-4.")

print("""
Thanks for visiting GC Library! We look foward to seeing you again.""")