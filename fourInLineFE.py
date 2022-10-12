from fourInLineBE import FourInLineBE
from fourInLineBEException import Winner
from fourInLineBEException import OutOfRange


class FourInLineFE():

    def __init__(self):
        self.BE = FourInLineBE()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                print("  " + str(self.BE.board[i][j]) + "  ", end="")
            print("\n")

    def run(self):

        while not self.BE.winCondition:
            self.draw_board()
            self.play()

    def play(self):
        try:
            column = int(input('Introduzca una columna: '))
            self.BE.placeToken(column - 1)
        except ValueError:
            print("Ingrese un valor válido")
        except OutOfRange:
            print("Ingrese un nùmero entre 1 y 8")
        except Winner:
            self.BE.winCondition = True
            self.draw_board()
            print("¡Gano el jugador: " + str(self.BE.token.colour) + "!")


if __name__ == '__main__':
    FourInLineFE().run()
