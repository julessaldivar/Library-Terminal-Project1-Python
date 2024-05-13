import datetime
from Library_class_Media import media_list

from library_functions import display_books
from library_functions import search_by_author
from library_functions import search_title
from library_functions import checkout
from library_functions import return_an_item
from library_functions import add_book
from library_functions import add_movie

print("""Hi, Welcome to the Grand Circus Library!
Please choose an option from the below list to begin:""")

valid_action = 0
while valid_action == 0:            # Create a loop to stay in while the user wants to interact with the library.

    print("""    1. Display all media
    2. Search for a book by author or a movie by director
    3. Search by title keyword
    4. Return an item 
    5. Add a book to the library
    6. Add a movie to the library """)

    action = int(input(f'> '))

    if action == 1:  # Display all the books ###################################

        display_books(media_list)

        checkout(media_list)

        # Staying in the library loop or not.
        while True:
            another = input(f'Would you like to complete another action (y/n)? ')
            if another == 'y':
                valid_action = 0
                break
            elif another == 'n':
                valid_action = 1
                break
            else:
                print(f"I don't understand your prompt. Please enter 'y' or 'n'.")

    elif action == 2:  # Search for a book by author #############################

        search_by_author(media_list)

        # Staying in the library loop or not.
        while True:
            another = input(f'Would you like to complete another action (y/n)? ')
            if another == 'y':
                valid_action = 0
                break
            elif another == 'n':
                valid_action = 1
                break
            else:
                print(f"I don't understand your prompt. Please enter 'y' or 'n'.")

    elif action == 3:   # Search for a book by title keyword #######################

        search_title(media_list)

        # Staying in the library loop or not.
        while True:
            another = input(f'Would you like to complete another action (y/n)? ')
            if another == 'y':
                valid_action = 0
                break
            elif another == 'n':
                valid_action = 1
                break
            else:
                print(f"I don't understand your prompt. Please enter 'y' or 'n'.")

    elif action == 4:   # Return a book ##############################################

        num_return = input(f'What is the number of the item you would like to return? ')

        return_an_item(media_list, num_return)

        # Staying in the library loop or not.
        while True:
            another = input(f'Would you like to complete another action (y/n)? ')
            if another == 'y':
                valid_action = 0
                break
            elif another == 'n':
                valid_action = 1
                break
            else:
                print(f"I don't understand your prompt. Please enter 'y' or 'n'.")

    elif action == 5:  # Adding a book to the library ################################

        add_book(media_list)

        # Staying in the library loop or not.
        while True:
            another = input(f'Would you like to complete another action (y/n)? ')
            if another == 'y':
                valid_action = 0
                break
            elif another == 'n':
                valid_action = 1
                break
            else:
                print(f"I don't understand your prompt. Please enter 'y' or 'n'.")

    elif action == 6:  # Adding a movie to the library ################################

        add_movie(media_list)

        # Staying in the library loop or not.
        while True:
            another = input(f'Would you like to complete another action (y/n)? ')
            if another == 'y':
                valid_action = 0
                break
            elif another == 'n':
                valid_action = 1
                break
            else:
                print(f"I don't understand your prompt. Please enter 'y' or 'n'.")

    else:                   #
        valid_action = 0
        print(f"I don't understand your prompt, please enter a number 1-6.")

print("""
Thanks for visiting Grand Circus Library! We look forward to seeing you again.""")
