# 7. Roman Numeral Conversion:

# Create a function that converts a given integer to its Roman numeral representation.
# Handle numbers from 1 to 3999.
# Use a combination of string manipulation and conditional statements to build the Roman numeral.

def conversion(n: int):

    if n < 1 or n > 3999:
        print("Spiacenti inserire un numero da 1 a 3999.")

    valori = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    roman = ""

    for valore, simbolo in valori:
        while n >= valore:
            roman += simbolo
            n -= valore

    print(roman)

conversion(80)
