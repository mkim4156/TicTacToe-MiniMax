from board import Board
from player import Player, AI, MiniMax

# fraom player import Player, AI, SmartAI

# main program
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    #player1 = Player("Bob", "X")
    #player1 = AI("Bob", "X", board)
    player1 = Player("Bob", "X")

    #player2 = Player("Alice", "O")
    player2 = MiniMax("Alice", "O", board)
    #player2 = AI("Alice", "O", board)

    # player2 = SmartAI("Alice", "O", board)

    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N]\n").upper()
    if ans != "Y":
        break
print("Goodbye!")