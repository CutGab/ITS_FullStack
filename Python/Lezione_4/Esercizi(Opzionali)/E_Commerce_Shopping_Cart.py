# 3. E-commerce Shopping Cart:

# Create a function that defines a product with a name, price, and quantity.
# Create functions that manage the shopping cart, allowing the user to add, remove, and view products in the cart.
# Create a function that calculates the cart total and apply any discounts or taxes.
# Create a funciton to print a detailed summary of the cart including products and totals.
# Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

shopping_cart: list = []
available_products: list = []

def create_product(name: str, price: float, quantity: int):

    product: dict = {"Name": name,
                     "Price": price,
                     "Quantity": quantity}
    
    available_products.append(product)

def add_product(product_name):

    for i in available_products:

        if i["Name"] == product_name:

            if i["Quantity"] <= 0:
                print("Spiacenti, prodotto esaurito.")
                
            else:
                shopping_cart.append((i["Name"], i["Price"]))
                i["Quantity"] -= 1

def remove_product(product_name):
    
    for i in shopping_cart:
        
        if i[0] == product_name:
            shopping_cart.remove(i)
            
            for i in available_products:
                
                if product_name == i["Name"]:
                    i["Quantity"] += 1

def view_shopping_cart():

    print("Shopping Cart")

    print("")

    for i in shopping_cart:
        print(f"(Name: {i[0]} Price: {i[1]})")

def show_total():

    somma = 0

    for i in shopping_cart:
        somma += i[1]

    print(f"Total: {somma}")

#Definisco Due Prodotti
create_product("Mozzarelle", 10, 1)
create_product("Pomodori", 15.66, 10)

#Aggiungo prodotto al mio carrello

add_product("Pomodori")
add_product("Pomodori")
add_product("Mozzarelle")

#Rimuovo prodotto dal mio carrello

remove_product("Pomodori")

#Mostro i contenuti del carrello

view_shopping_cart()

#Mostro il totale

show_total()



