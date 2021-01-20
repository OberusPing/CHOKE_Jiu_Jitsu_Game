from data import *
import random


class Npc:
    def __init__(self, name):
        self.name = name
        self.current_position = 'Bottom Closed Guard'
        self.turn = False
        self.last_roll = 0
        self.current_move = ''

    def npc_mechanic(self, player):
        self.last_roll = random.randint(1, 20)
        self.current_move = random.choice(globalPositions[self.current_position][MOVES])

        if self.last_roll >= globalMoves[self.current_move][DC]:
            self.current_position = globalMoves[self.current_move][NEWPOSITION]
            player.current_position = globalMoves[self.current_move][ENEMYPOS]
            self.turn = False
        else:
            self.turn = False

    def check_submission(self):
        if self.current_position == 'Submission':
            return True
