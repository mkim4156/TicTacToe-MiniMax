class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        # the winner's sign O or X
        self.winner = ""

    def get_size(self):
        # optional, return the board size (an instance size)
        return self.size

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        return self.winner

    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        index = valid_choices.index(cell)
        self.board[index] = sign

    def isempty(self, cell):
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        index = valid_choices.index(cell)

        # return True if the cell is empty (not marked with X or O)
        if self.board[index] == " ":
            return True
        else:
            return False

    def row_checker(self, sign):
        for i in range(3):
            count = 0
            for j in range(3):
                if self.board[i] == sign:
                    count = count + 1
                i = i + 3
                if count == 3:
                    self.winner = sign

    def column_checker(self, sign):
        for i in range(0, 7, 3):
            count = 0
            for j in range(3):
                if self.board[i] == sign:
                    count = count + 1
                i = i + 1
                if count == 3:
                    self.winner = sign

    def cross_checker(self, sign):
        count1 = 0
        index1 = 0
        count2 = 0
        index2 = 2
        for i in range(3):
            if self.board[index1] == sign:
                count1 = count1 + 1
            index1 = index1 + 4
            if count1 == 3:
                self.winner = sign

            if self.board[index2] == sign:
                count2 = count2 + 1
            index2 = index2 + 2
            if count2 == 3:
                self.winner = sign

    def isdone(self):
        self.winner = ""
        done = False
        sign_O = "O"
        sign_X = "X"
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        self.row_checker(sign_O)
        self.row_checker(sign_X)
        self.column_checker(sign_O)
        self.column_checker(sign_X)
        self.cross_checker(sign_O)
        self.cross_checker(sign_X)

        if self.winner != "":
            done = True
        if " " not in self.board:
            done = True

        return done

    def show(self):
        # draw the board
        # need to complete the code
        print('   A   B   C')
        print(' +---+---+---+')
        print('1| {} | {} | {} |'.format(self.board[0], self.board[3], self.board[6]))
        print(' +---+---+---+')
        print('2| {} | {} | {} |'.format(self.board[1], self.board[4], self.board[7]))
        print(' +---+---+---+')
        print('3| {} | {} | {} |'.format(self.board[2], self.board[5], self.board[8]))
        print(' +---+---+---+')
