from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def play(self):
        while True:

            self.board.display()

            print(f"\nPlayer {self.current_player}'s Turn")

            try:
                row = int(input("Row (0-2): "))
                col = int(input("Column (0-2): "))
            except ValueError:
                print("Enter numbers only!")
                continue

            if row not in range(3) or col not in range(3):
                print("Invalid position.")
                continue

            if not self.board.make_move(row, col, self.current_player):
                print("Cell already occupied.")
                continue

            winner = self.board.check_winner()

            if winner:
                self.board.display()
                print(f"\nWinner: {winner}")
                break

            if self.board.is_full():
                self.board.display()
                print("\nDraw!")
                break

            self.switch_player()