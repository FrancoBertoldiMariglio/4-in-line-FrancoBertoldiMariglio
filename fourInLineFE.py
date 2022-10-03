from ast import Break
from fourInLineBE import FourInLineBE
from fourInLineBEException import Winner
from fourInLineBEException import OutOfRange


class FourInLineFE():

    def __init__(self):
        self.game = FourInLineBE()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                print("  " + str(self.game.board[i][j]) + "  ", end="")
            print("\n")

    def run(self):
        try:
            while self.game.winCondition == False:
                self.draw_board()
                self.play()
        except Winner:
            Break

    def play(self):
        try:
            column = int(input('Introduzca una columna: '))
            self.game.placeToken(column - 1)
        except ValueError:
            print("Ingrese un valor válido")
        except OutOfRange:
            print("Ingrese un nùmero entre 1 y 8")
        except Winner:
            self.game.winCondition = True
            self.draw_board()
            print("¡Ganaste!")


if __name__ == '__main__':
    FourInLineFE().run()