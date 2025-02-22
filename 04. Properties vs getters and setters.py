from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
            print("Email changed")
        else:
            print("Invalid email")


user1 = User("Alice", " Dan@gmail.com", "123456")

user1.email = "this is not an email"
print(user1.email)  # this is not an email

# In the above code, we have a class User with an __init__ method that initializes the username, email, and password of the user. We have defined a property email that returns the email of the user. We have also defined a setter for the email property that changes the email of the user if it is valid.
