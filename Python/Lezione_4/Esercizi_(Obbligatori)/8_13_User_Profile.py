# 8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
# All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def build_profile(name: str, last_name: str, age: int, hair: str, weight: int):

    print(f"Name: {name}\nLast Name: {last_name}\nAge: {age}\nHair: {hair}\nWeight: {weight}")

build_profile("Gabriele", "Cutolo", 21, "Brown", 65)
