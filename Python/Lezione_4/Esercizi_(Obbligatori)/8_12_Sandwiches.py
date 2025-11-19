# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

def sandwich(*args):

    lista_ingredienti: list = []

    for i in args:
        lista_ingredienti.append(i)

    print(f"Your Sandwhich: {lista_ingredienti}")


sandwich("Pomodoro", "Mozzarella", "Tonno")
sandwich("Insalata", "Tonno")
sandwich("Acciughe", "Bresaola", "Olive", "Olio")


