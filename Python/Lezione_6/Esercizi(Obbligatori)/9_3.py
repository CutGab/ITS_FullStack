# 9-3. Users: Make a class called User. 
# Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.


class User:

    def __init__(self, first_name: str, last_name: str, email: str, username: str):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username

    def describe_user(self):

        print(f"Username: {self.username}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}")


    def greet_user(self):

        print(f"Hello {self.username}, have a nice day!")


u1 = User ("Gabriele", "Cutolo", "gabbro@gmail.com", "GabbyGab")
u2 = User ("Davide", "Raponi", "davidin@gmail.com", "Danger")
u3 = User ("Erald", "Kanka", "Errald@gmail.com", "E_R")


u1.describe_user()
u1.greet_user()

print("*" * 10)

u2.describe_user()
u2.greet_user()

print("*" * 10)

u3.describe_user()
u3.greet_user()