# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement, such as You really like Apples!

fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("I really love apples!")

if "banana" in fruits:
    print("I really love bananas!")

if "oranges" not in fruits:
    print("I don't really like oranges")

if "mango" in fruits:
    print("I ADORE MANGOS")

if "grape" not in fruits:
    print("Grapes are whatever")