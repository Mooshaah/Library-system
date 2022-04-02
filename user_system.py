## the class created for the users
# this class is used to create an account for the user and determine the type of the user
#then after gatting the credentials from the user class strores it in a list "users[user.i]

class User:
    i = 1

# initializing a method which contains the object type


 #this function (set_users) contains the dictionary (users[user.i]) and methods required for the user in order to store the user credentials
  # type, name, id, books,email, are the keys of the dictionary which stores a certian variable

    def __init__(self):
        self.users = dict()

    def set_users(self, type, name, id, email ):
        self.users[User.i] = {
            "type": type,
            "name": name,
            "id": id,
            "books": [],
            "Email": email
        }
        User.i += 1


# get users is a method used to get the user's input stored in the method set users which contains the dictionary users that stores all theusers info
#  and then it would return the input that before was stored in the dictionary.
# to show user input
    def get_users(self):
        return self.users

