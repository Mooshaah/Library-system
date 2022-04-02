# class used to store the library books and their information
class Books:
    # i is set to "-1" in order to properly index the dictionary
    i = -1

    def __init__(self):
        # initializing a method which contains the object type
        self.data = dict()

    # this function (set_data) contains the dictionary (data[Books.i]) and methods required for the user in order to store the user credentials
    # name, author, isbn, num_of_copies_at_school, num_of_copies_borrowed, num_of_copies,av_online_or_physical, borrowers_info_with_the_date_borrowed are the keys of the dictionary which stores a certain variable
    def set_data(self,name, author, isbn, num_of_copies_at_school, num_of_copies_borrowed, num_of_copies,av_online_or_physical, borrowers_info_with_the_date_borrowed,period):
        Books.i += 1
        self.data[Books.i] = {
            "name": name,
            "Author":author,
            "ISBN":isbn,
            "Num_of_copies_at_school":num_of_copies_at_school,
            "Num_of_copies_borrowed":num_of_copies_borrowed,
            "Num_of_copies":num_of_copies,
            "Available_online_or_physical": av_online_or_physical,
            "Borrowers_info_with_the_date_of_borrowed":borrowers_info_with_the_date_borrowed,
            "period":period

        }
# to show user input
    def get_data(self):
        return self.data

    def search(self, all_books, name):
            n = int(input("Enter how intended number of searches you're going to make"))
            for y in range (n):
                for x in all_books:
                    if all_books[x]["name"] == name:
                        print(all_books)

    def extend_loan_period(self, all_books, Book_name, period):
        for x in books:
            if books[x]["name"] == Book_name:
                all_books[x]["loan period"]+= int(period)
                print(all_books)
