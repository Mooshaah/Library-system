# importing the classes created in external files to uss in the main file
import sys
from user_system import User
from Library_system import Books
# user is the object's name used to store the class , so the class can be used later on
user = User()
books = Books()
# a deafult user that is stored in the system by default
user.set_users("admin","mohamed","1254","mohamedmedhatsh@hotmail.com")
all_user = user.get_users()

#  a book which is stored in the library by default
books.set_data("Hamlet", "William_shakespeare", "9781586638443", "3", "1", "4", "4","out_of_stock","")
all_books = books.get_data()

# The system is designed to function during runtime , so we need a while loop to keep looping the program till it ends
while True:
    name = input("Enter the Name") # prompts the user to enter his name
    type = input("Enter the Type") # prompts the user to enter his account type in order to gain access to the system

    if type == "admin" and name == "mohamed": # the system checks and authintcates the user by his type and then logs him into the category of his user type
        n = int(input("Please enter the number of users you want to add or remove")) # the user sets n users his going to add or remove
        for i in range (n): # loop to irritate inside the admin user privileges
            print("Welcome to the system, you currently are using the root account")
        system_users = int(input("===== Admin_user_menu =====" #admin user menu
                                 " \n1 ) Add a user "
                                 " \n2) Remove a user"))
        if system_users == 1: # option 1 Add a user
            # prompts the Admin user to enter the new user details
            name = input("Enter new user username")
            id = input("Enter new user ID")
            books_borrow = input("Enter the books you want to borrow")
            Email = input("Enter new user email")
            type = input("Enter new user type")
            user.set_users(type, name, id, Email)
            all_users = user.get_users() # returns the new user details
            print(all_users)
            system_users = int(input("===== Admin_user_menu ====="
                                 " \n2) Remove a user"
                                 " \n3) Exit the admin user menu"))
            if system_users == 2: #option 2 remove a user
                n = int(input("Enter the number of users you want to delete")) # enter the index number of the user you want to delete
                all_users.pop(n)
                print(all_users)

            if system_users == 3: # exits the admin user menu
                print("You have exited the Admin user menu successfully")

        else:
            print("Wrong Data") # the program display this message when the user enter invalid user type

    elif type == "librarian": # checks the type if it's librarian
        print("Welcome to the system, you're now logged in as a librarian")
        choice = int(input("===== Librarian_user_menu =====" #librarian user menu
                           " \n1) Add a book to the library"
                           " \n2) Remove a book from the library"
                           " \n3) Search for a book"
                           " \n4) Exit"))
        if choice == 1: # option 1 Add a book to the dict Books.i
            n = int(input("Enter the total number of books you're going to add to the shelve ")) # the user sets n users his going to add
            for i in range(n): # based upon the user input the program is going to iretate n times and take the new books details and store them inside the dictionary
                name = input("Enter the new book name")
                author = input("Enter the author/'s name ")
                isbn = input("Enter the book ISBN number")
                num_of_copies_at_school = input(("Enter the num of copies at school"))
                num_of_copies_borrowed = input("Enter the number of copies borrowed")
                num_of_copies = input("Enter the total number of copies ")
                av_online_or_physical = input("Enter Whether the new book available or not ")
                borrowers_info_with_the_date_borrowed = input("Enter the borrowers information, if available")
                # after the librarian user enter the new books details the system is going to store them inside the function set_data which stores the inputs inside the dictionary
                books.set_data(name, author, isbn, num_of_copies_at_school, num_of_copies_borrowed, num_of_copies, av_online_or_physical, borrowers_info_with_the_date_borrowed)
                # the following 2 lines of code returns the new books stored in the dictionary and then displays it
                all_books = books.get_data()
                print(all_books)
                choice = int(input("===== Librarian_user_menu ====="
                                   " \n2) Remove a book from the library"
                                   " \n3) Search for a book"
                                   " \n4) Exit the Librarian menu"))

                if choice ==2: #remove a book from the dictionary
                    n = int(input("Enter the number of books you want to delete")) # takes an input from the user and based upon the user
                                                                                   # input the program is going to irritate inside the loop to remove a certian number of books
                    for i in range(n):
                        books.data.pop(Books.i)
                        all_data = books.get_data()
                        print(all_data)



                if choice ==3: # the library search engine which search for books by its name
                    for x in all_books:
                        name = input("Enter the name of the book your searching for")
                        if all_books[x]["name"] == name:
                            print("Book found")
                        else:
                            print("Book not found")

                if choice == 4:
                    break

    elif type == "normal": #normal user and its functuality
        print("Welcome to the system you're now logged in as a normal user")
        normal_user_choice = int(input(print("========== Normal user menu ==========" #normal user menu
                                         "\n 1 . Borrow a book"
                                         "\n 2 . Return a book"
                                         "\n 3 . search for a book"
                                         "\n 4 . Extend your loan period"
                                         "\n 5 . Press key num 5 to exit the system")))

        if normal_user_choice == 1: # option 1 for normal user to borrow a book
            for x in all_books:
                name = input("Enter the name of the book you want to borrow")
                if all_books[x]["name"] == name:
                    print("Book borrowed")
                else:
                    print("Book isn't available, try again in a bit")
            normal_user_choice = int(input(print("========== Normal user menu =========="
                                                 "\n 2 . Return a book"
                                                 "\n 3 . search for a book"
                                                 "\n 4 . Extend your loan period"
                                                 "\n 5 . Press any key to quit")))
            if normal_user_choice == 2: # the normal user returns the book borrowed
                for x in all_books:
                    name = input("Enter the name of the book you want to return")
                    if all_books[x]["name"] == name:
                        print("Book returned")
                    else:
                        print("An error occurred, try again in a bit")
            normal_user_choice = int(input(print("========== Normal user menu =========="
                                                             "\n 3 . search for a book"
                                                             "\n 4 . Extend your loan period"
                                                             "\n 5 . Press any key to quit")))
            if normal_user_choice ==3: # the normal user search engine which search for books by its name
                print("search for the book by its Name")
                for x in all_books:
                    name = input("Enter the name of the book your searching for")
                    if all_books[x]["name"] == name:
                        print("Book found")
                    else:
                        print("Book not found")
            normal_user_choice = int(input(print("========== Normal user menu =========="
                                                 "\n 4 . Extend your loan period"
                                                 "\n 5 . Press any key to quit")))
            if normal_user_choice == 4: # loan period extension
                print("Extend the loan period in int format")
                for x in all_books:
                    period= input("Enter the duration desired")
                    if all_books[x]["period"] == period:
                        print("Loan period extended")
                    else:
                        print("Error occurred while requesting a loan period extension, please try again in a bit ")


            if normal_user_choice == 5: # exits the whole program
                print("you have exited the program")
                break

    else:
        print("\nWrong type entered")
        sys.exit("The program has closed due to an usage error, please restart the program and be careful while using it to prevent crashing")

