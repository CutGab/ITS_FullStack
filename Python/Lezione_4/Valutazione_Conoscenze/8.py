# Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
# For example:

# Test	Result
# print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
# 2
# print(count_isolated([1, 2, 3, 4, 5]))
# 5

def count_isolated(numbers: list):

    isolated = 0

    for i in range(len(numbers)):

        if i == 0:
            if numbers[i] != numbers[1]:
                isolated += 1

        elif i == len(numbers) - 1:
            if numbers[i] != numbers[i - 1]:
                isolated += 1

        else:

            if numbers[i] != numbers [i + 1] and numbers[i] != numbers [i - 1]:
                isolated += 1


    return isolated

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 2, 3, 4, 5]))
