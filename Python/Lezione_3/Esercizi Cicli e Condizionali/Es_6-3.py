# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

Python_words: dict = {"Variable": "A name used to store data that can change during program execution.",
                      "Function": "A reusable block of code that performs a specific task. Defined using def.",
                      "Loop": "A control structure that repeats code multiple times. Python has for and while loops.",
                      "List": "A collection of ordered items that can be changed (mutable).",
                      "Class": "A blueprint for creating objects (OOP concept). Defined using class."
                      }

for key, values in Python_words.items():
    print(f"{key}:\n {values}")
    print("")