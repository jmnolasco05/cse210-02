from game.croupier import Croupier
from game.player import Player


class GameTable:

    def __init__(self):
        self.croupier = None
        self.player = None

    def start_game(self):
        self.player = Player(300)
        self.croupier = Croupier()

        while self.player.is_playing:

            print()
            print(f"The card is {self.croupier.current_card}")
            guess = input("Higher or lower? [h/l] ")

            if self.valid_guess(guess):
                self.player.guess = guess

                print(f"Next card was: {self.croupier.new_card()}")

                self.check_guess()
                print(f"Your score: {self.player.score}")

                if self.player.score > 0:
                    self.keep_playing_choice()
            else:
                print("Invalid option!")

    def check_guess(self):
        cards_diff = self.croupier.next_card - self.croupier.current_card

        win_lower = cards_diff < 0 and self.player.guess.lower() == "l"
        win_higher = cards_diff > 0 and self.player.guess.lower() == "h"

        if cards_diff == 0:
            print("It is a tie!")
        elif win_lower or win_higher:
            self.player.earn_points(100)
        else:
            self.player.lose_points(75)

    def keep_playing_choice(self):
        print()

        choice = self.ask_user()
        if choice == "y":
            self.croupier.prepare_next_round()
        else:
            self.player.is_playing = False

    def ask_user(self):
        choice = None

        while choice is None:
            user_input = input("Play again? [y/n] ")
            if user_input in ["y", "Y", "n", "N"]:
                choice = user_input
            else:
                print("Invalid option")

        return choice.lower()

    def valid_guess(self, guess):
        valid_options = ["h", "l", "H", "L"]

        return guess in valid_options
