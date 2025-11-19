# 9-11. Imported Admin: Create a module users.py containing three classes:

# User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
# Privileges: holds a list of privileges and a method show_privileges() to display them.
# Admin: stores a User instance and a Privileges instance as attributes.

# In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.

class User:

    def __init__(self, first_name: str, last_name: str, username: str, email: str):
    
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):

        print(f"Username: {self.username}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}")

    def greet_user(self):

        print(f"Hello {self.username}, have a nice day!")


class Privileges:

    def __init__(self, privileges: list):

        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin:

    def __init__(self, user: User, user_privileges: Privileges):

        self.user = user
        self.user_privileges = user_privileges