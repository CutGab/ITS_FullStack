# 5. Inventory Management System:

# Create a list to store the items in inventory.
# Create a function that defines an item with a code, name, quantity, and price.
# Implement functions to add, remove, search, and update items in the inventory.
# Use for loops to manage the various inventory operations.

inventory: list = []

created_items: list = []

def create_item(code: int, name: str, quantity: int, price: float):

    item: dict = {"Codice": code,
                  "Nome": name,
                  "Quantità": quantity,
                  "Prezzo": price
                  }
    
    created_items.append(item)

def add_item(name):

    for item in created_items:

        if name == item["Nome"]:

            if item["Quantità"] > 0:
                inventory.append((item["Codice"], item["Nome"], item["Prezzo"]))
                item["Quantità"] -= 1

            else:
                print(f"Spiacenti, l'oggetto {item["Nome"].lower()} non è disponibile.")

def remove_item(name):

    for item in inventory:

        if item[1] == name:
            inventory.remove(item)

        else:
            print("Prodotto non trovato.")

def search_item(name):

    for item in inventory:

        if item[1] == name:

            print(f"Nome: {item[1]}\nPrezzo: {item[2]}")

        else:
            print("Oggetto non trovato.")
            break

def update(name, new_name, new_price):
        for i, item in enumerate(inventory):
            if item[1] == name:
                inventory[i] = (item[0], new_name, new_price)

create_item(1, "Palla", 20, 10.99)
create_item(2, "Sarcofago", 4, 120.99)

add_item("Palla")
add_item("Sarcofago")

print(inventory)

print("-" * 10)

search_item("ADAW")

print("-" * 10)

update("Palla", "Salmone", 9.99)

print(inventory)