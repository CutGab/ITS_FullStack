# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size: str, text: str):
    print(f"T-Shirt size: {size}\nT-Shirt text: {text}")


make_shirt("XL", "When I'm sad I stop being sad and be awesome instead.")

print("")

make_shirt(text = "When I'm sad I stop being sad and be awesome instead.", size= "XL")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt_2(size: str = "XL", text: str = "I love Python"):
    print(f"T-Shirt size: {size}\nT-Shirt text: {text}")

print("")

make_shirt_2()

print("")

make_shirt_2("M")

print("")

make_shirt_2("S", "FUCK YOU")



