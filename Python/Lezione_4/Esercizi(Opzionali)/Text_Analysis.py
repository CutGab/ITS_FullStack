# 4. Text Analysis:

# Create a function that takes a paragraph and counts the number of occurrences of each word.
# The function should print a report showing the most frequent words and their number of occurrences.
# You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.

def text_analysis(text):

    occurrences: dict = {}

    new_text = text.lower()

    for i in new_text.split():

        i = i.strip(".,!?()")

        if i in occurrences:
            occurrences[i] += 1

        else:
            occurrences[i] = 1

    max_value = max(occurrences.values())

    for key, values in occurrences.items():

        if values == max_value:

            print(f"{key}: {values}")

text_analysis("ciao a tutti amici e amiche, ciao anche a te! (Ciao)")