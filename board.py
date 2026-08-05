class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\n")
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:
                print("-" * 9)

    def make_move(self, row, col, player):
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def is_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def check_winner(self):
        # Rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Columns
        for col in range(3):
            if (
                self.board[0][col]
                == self.board[1][col]
                == self.board[2][col]
                != " "
            ):
                return self.board[0][col]

        # Diagonals
        if (
            self.board[0][0]
            == self.board[1][1]
            == self.board[2][2]
            != " "
        ):
            return self.board[0][0]

        if (
            self.board[0][2]
            == self.board[1][1]
            == self.board[2][0]
            != " "
        ):
            return self.board[0][2]

        return None