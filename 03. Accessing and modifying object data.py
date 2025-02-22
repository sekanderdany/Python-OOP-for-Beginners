from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        self._email = self._email.strip().lower()
        print(f"Email accessed at {datetime.now()}")
        return self._email

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email.strip().lower()
            print(f"Email changed at {datetime.now()}")


user1 = User("Alice", " Dan@gmail.com", "123456")

print(user1.get_email())  #
user1.set_email("baad@YAHOO.com")
print(user1.get_email())  #

# '''
# In the above code, we have a class User with an __init__ method that initializes the username, email, and password of the user. We have defined a get_email method that returns the email of the user after stripping and converting it to lowercase. We have also defined a set_email method that changes the email of the user after stripping and converting it to lowercase.
# We have created an instance of the User class, user1, with the username Alice, email
