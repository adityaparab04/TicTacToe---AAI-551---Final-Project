import random
import time


class TicTacToe:
    def __init__(self) -> None:
        self.board = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]
        self.player = random.choice(['X', 'O'])
# extra features of time and scores
        self.scores = {'X': 0, 'O': 0}
        self.timeLimit = 20  # 20 seconds to make a move


# check board is empty or not

    def checkNotEmpty(self):
        for rowEle in range(len(self.board)):
            for colEle in range(len(self.board[rowEle])):
                if self.board[rowEle][colEle] == '_':
                    return False
        return True

# check for win, lose or draw

    def checkResult(self, player):
        # check Rows
        for row in self.board:
            if all([element == player for element in row]):
                return True

        # check Columns
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        # check Diagonals
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2-i] == player for i in range(3)]):
            return True
# show board

    def showBoard(self):
        print("  1   2   3   ")
        print("1 " + self.board[0][0] + " | " + self.board[0]
              [1] + " | " + self.board[0][2])
        print("  --+---+---")
        print("2 " + self.board[1][0] + " | " + self.board[1]
              [1] + " | " + self.board[1][2])
        print("  --+---+---")
        print("3 " + self.board[2][0] + " | " + self.board[2]
              [1] + " | " + self.board[2][2])


# start game

    def startGame(self):
        while True:
            self.board = [["_", "_", "_"],
                          ["_", "_", "_"],
                          ["_", "_", "_"]]
            while True:

                self.showBoard()
                start_time = time.time()
                move = input(
                    "Please play your move Player {} in 20 secs (row, col): ".format(self.player))
                end_time = time.time()

                if end_time - start_time > self.timeLimit:
                    print("Time's up! Player {} loses.".format(self.player))
                    self.scores["O" if self.player == "X" else "X"] += 1
                    break

                moveArr = move.split(',')

                if len(moveArr) > 2:
                    print("Invalid Move")
                    continue

                row, col = map(int, moveArr)

                if row > 3 or col > 3:
                    print("Invalid move, please try again!")
                    continue

                if row < 1 or col < 1:
                    print("Invalid move, please try again!")
                    continue

                if self.board[row-1][col-1] != '_':
                    print("Move is already taken, please try again!")
                    continue
                else:
                    self.board[row-1][col-1] = self.player

                if self.checkResult(self.player):
                    self.showBoard()
                    print("Player {} wins!!".format(self.player))
                    self.scores[self.player] += 1
                    break

                if self.checkNotEmpty():
                    self.showBoard()
                    print("It's a Draw!!")
                    break

                # switch player

                if self.player == 'X':
                    self.player = 'O'
                else:
                    self.player = 'X'

            print("Current Scores: X = {}, O = {}".format(
                self.scores['X'], self.scores['O']))

            playAgain = input(
                "Do you want to Play again? Press (y) or any other key to exit: ")

            if playAgain.lower() == 'y':
                continue
            else:
                break


# restart game
g = TicTacToe()
g.startGame()
