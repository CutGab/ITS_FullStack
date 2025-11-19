# 1. School Grading System:

# Create a function that takes a student's name and their scores in different subjects as input.
# The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
# Create a for loop to iterate over a list of students and scores, calling the function for each student.

def grade_student(name: str, scores: list):
    
    average = sum(scores)/len(scores)

    print(f"Name: {name}")
    print(f"Average: {average}")

    if average >= 60:
        print(f"The student {name} has passed the exam!")

    else:
        print(f"The student {name} has failed the exam.")

students: list = [("Federico", [18, 24, 30, 19, 20]),
                  ("Davide", [40, 110, 35, 84, 73]),
                  ("Andrea", [12, 34, 67, 2, 19]),
                  ("Daniele", [59, 76, 60, 54, 87])
                  ]

for names, scores in students:
    
    print("")
    grade_student(names, scores)