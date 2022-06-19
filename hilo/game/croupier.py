import random


class Croupier:

    def __init__(self):
        self.current_card = random.randint(1, 13)
        self.next_card = None

    def new_card(self):
        self.next_card = random.randint(1, 13)
        return self.next_card

    def prepare_next_round(self):
        self.current_card = self.next_card
        self.next_card = None
