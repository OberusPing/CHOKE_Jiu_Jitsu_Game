from data import *
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.current_position = 'Top Closed Guard'
        self.current_move = ''
        self.last_roll = 0

    def check_success(self, move, opponent):
        self.last_roll = random.randint(1, 20)
        if self.last_roll >= move[DC]:
            self.current_position = move[NEWPOSITION]
            opponent.current_position = move[ENEMYPOS]
            return True
        else:
            return False

    def check_submission(self):
        if self.current_position == 'Submission':
            return True


