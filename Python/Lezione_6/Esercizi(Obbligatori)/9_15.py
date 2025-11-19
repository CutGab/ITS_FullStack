# 9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

# 1. Add a method called simulate_until_win(self, my_ticket) that:

# Accepts a ticket (a list of 4 items).
# Repeatedly draws random tickets using the draw_ticket() method.
# Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
# Returns the number of attempts and the winning ticket.
# 2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

# 3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

# 4. Print a message showing:

# Your ticket
# The winning ticket
# How many attempts it took to win


import random

class LotteryMachine:

    def __init__(self, prizes: list[int, str]):

        self.prizes = prizes
        self.winning_ticket = []

    def random_pick(self):
        for _ in range(4):
            pick = random.choice(self.prizes)
            self.winning_ticket.append(pick)

    def winner(self):
        print(f"The winner will be anyone who is able to match the following ticket!: {self.winning_ticket}")

    def simulate_until_win(self, my_ticket: list):

        attempts = 0

        while self.winning_ticket != my_ticket:

            self.random_pick()

            if my_ticket != self.winning_ticket:
                print(f"Sorry, the ticket extracted was {self.winning_ticket}")
                self.winning_ticket.clear()
                attempts += 1

            else:
                print(f"Number of attempts: {attempts}")
                print(f"Ticket Extracted: {self.winning_ticket}")
                print(f"Your ticket: {my_ticket}")
                break


l1 = LotteryMachine ([1, "a", 6, "c", 9, "f", 2, "b", 4, "z", 7, 3, 5, 10, 8])

l1.simulate_until_win(["a", 4, "f", "b"])

            

