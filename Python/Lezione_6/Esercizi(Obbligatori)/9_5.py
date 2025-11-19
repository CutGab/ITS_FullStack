# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.

class User:

    def __init__(self, first_name: str, last_name: str, email: str, username: str, login_attempts: int):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.login_attempts = login_attempts

    def describe_user(self):

        print(f"Username: {self.username}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nLogin Attempts: {self.login_attempts}")


    def greet_user(self):

        print(f"Hello {self.username}, have a nice day!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


u1 = User ("Gabriele", "Cutolo", "gabbro@gmail.com", "GabbyGab", 0)

u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()

u1.describe_user()

u1.reset_login_attempts()

print("*" * 10)

u1.describe_user()


    
