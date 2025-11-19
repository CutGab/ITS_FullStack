# 9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. 
# Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. 
# Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.

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


l1 = LotteryMachine ([1, "a", 6, "c", 9, "f", 2, "b", 4, "z", 7, 3, 5, 10, 8])

l1.random_pick()

l1.winner()
