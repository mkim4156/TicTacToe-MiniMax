from random import choice
from math import inf


class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell, sign)
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        while True:
            cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
            if cell in valid_choices:
                if board.isempty(cell):
                    board.set(cell, self.sign)
                    break
                else:
                    print("You did not choose correctly.")
            else:
                print("You did not choose correctly.")


class AI(Player):
    def __init__(self, name, sign, board):
        super().__init__(name, sign)
        self.board = board

    def choose(self, board):
        used_words = []
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
        while True:
            cell = choice(valid_choices)
            if cell not in used_words:
                used_words.append(cell)
                if cell in valid_choices:
                    if board.isempty(cell):
                        board.set(cell, self.sign)
                        break


class MiniMax(AI):
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)

    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.get_sign():
                return 1
            # is a tie
            elif board.get_winner() == "":
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1

        min_score = inf
        max_score = -inf
        bestMove = None
        cells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        for cell in cells:
            if board.isempty(cell):
                if self_player:
                    self.board.set(cell, self.get_sign())
                    score = self.minimax(board, False, False)
                    if score > max_score:
                        max_score = score
                        bestMove = cell
                    board.set(cell, " ")
                else:
                    opponent_sign = ""
                    if self.get_sign() == "O":
                        opponent_sign = "X"
                    else:
                        opponent_sign = "O"

                    self.board.set(cell, opponent_sign)
                    score = self.minimax(board, True, False)
                    if score < min_score:
                        min_score = score
                        bestMove = cell
                    board.set(cell, " ")

        if start:
            return bestMove
        elif self_player:
            return max_score
        else:
            return min_score
