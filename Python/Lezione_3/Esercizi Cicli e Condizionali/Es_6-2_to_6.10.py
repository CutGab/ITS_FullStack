# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.

Favorite_numbers: dict = {"Dioni": 7,
                          "Gabriele": 4,
                          "Davide": 10,
                          "Lorenzo": 2,
                          "Erald": 15}

for key, values in Favorite_numbers.items():
    print(f"{key}: {values}")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

Favorite_numbers: dict = {"Dioni": [7, 10, 6],
                          "Gabriele": [4, 22, 2],
                          "Davide": [10, 66, 25],
                          "Lorenzo": [2, 89, 5],
                          "Erald": [15, 3, 87]}

for key, values in Favorite_numbers.items():
    print(f"{key}: {values}")