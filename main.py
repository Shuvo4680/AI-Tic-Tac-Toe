from utils import welcome
from game import Game


def main():
    welcome()

    game = Game()
    game.play()


if __name__ == "__main__":
    main()