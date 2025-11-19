# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

Person: dict = {"First_Name": "Gabriele",
                "Last_name": "Cutolo",
                "Age": 21,
                "City": "Roma"}

for key, values in Person.items():
    print(f"{key}: {values}")

# 6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, print everything you know about each person.

Person_1: dict = {"First_Name": "Gabriele",
                "Last_name": "Cutolo",
                "Age": 21,
                "City": "Roma"}

Person_2: dict = {"First_Name": "Dioni",
                "Last_name": "UnFake",
                "Age": 53,
                "City": "Roma"}

Person_3: dict = {"First_Name": "Davide",
                "Last_name": "Raponi",
                "Age": 20,
                "City": "Roma"}

people: list = [Person_1, Person_2, Person_3]

print("")

for i in people:
    print(i)