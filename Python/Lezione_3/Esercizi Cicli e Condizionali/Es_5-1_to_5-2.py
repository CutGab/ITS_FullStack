# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("")
print("Is car != 'audi'? I predict True.")
print(car != 'audi')
print("")
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
print("")
print("Is car != 'subaru'? I predict False.")
print(car != 'subaru')

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
# ate to 10. If you want to try more comparisons, write more tests and add them

# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

print('subaru' != 'subaru')
print('subaru' == 'subaru')
print("")
print(10 > 11)
print(10 < 11)
print(10 == 11)
print(10 == 10)
print('Subaru'.lower == 'subaru')
print(10 and 11 == 10 and 11)
print(10 == 10 or 10 == 11)

names: list = ["Gabriele"]

print("Gabriele" in names)
print("Luca" in names)