class Player:

    def __init__(self, initial_score):
        self.score = initial_score
        self.guess = None
        self.is_playing = True

    def earn_points(self, points):
        self.score += points

    def lose_points(self, points):
        self.score -= points

        self.is_playing = self.score > 0
