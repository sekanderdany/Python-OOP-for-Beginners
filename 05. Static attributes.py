

class User:
    # Static attribute
    user_count = 0

    def __init__(self, username, email):
        # Instance attributes
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user_count(self):
        print(f"Username: {self.username}, Email: {self.email}")
# Create instances of the User class
        print(f"Total users: {User.user_count}")


user1 = User("john_doe", "dan@gmail.com")
user2 = User("Alice", "alice@gmail.com")

print(User.user_count)  # Output: 2
user1.display_user_count()  # Output: Username: john_doe, Email:
print(user1.user_count)  # Output: 2
print(user2.user_count)  # Output: 2

# static attributes are shared across all instances of the class and can be accessed with class name and attribute name

# In the above code, we have a class User with a static attribute user_count that keeps track of the number of users created. We have an __init__ method that initializes the username and email of the user and increments the user_count by 1 each time a new user is created. We have created two instances of the User class, user1 and user2, and printed the total number of users created.
