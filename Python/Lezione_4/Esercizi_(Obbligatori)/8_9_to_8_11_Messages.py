# 8-9. Messages
# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

messages: list = [
    "You’ve got this!",
    "I’m here for you.",
    "Sending good vibes your way.",
    "One step at a time.",
    "Proud of you!"
]

def show_messages(lista: list):
    for message in lista:
        print(message)

show_messages(messages)

print("")

# 8-10. Sending Messages
# Write a function called send_messages() that prints each text message
# and moves each message to a new list called sent_messages as it’s printed.

def send_messages(lista: list):
    sent_messages: list = []
    messages_copy = lista[:]

    for message in messages_copy:
        print(message)
        sent_messages.append(message)
        lista.remove(message)

    print(f"Sent Messages: {sent_messages}")
    print(f"Messages: {lista}")

send_messages(messages)

print("")

# 8-11. Archived Messages
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.

messages: list = [
    "You’ve got this!",
    "I’m here for you.",
    "Sending good vibes your way.",
    "One step at a time.",
    "Proud of you!"
]

send_messages(messages[:])

print("")

print(f"Original Messages after send_messages: {messages}")
