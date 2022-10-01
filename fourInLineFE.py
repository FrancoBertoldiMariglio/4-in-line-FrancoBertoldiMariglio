from ast import Break
from fourInLineBE import FourInLineBE
from fourInLineBE import Token
from fourInLineBEException import Winner
from fourInLineBEException import NotWinner
from fourInLineBEException import OutOfRange

class FourInLineFE():

    def __init__(self):
        self.game = FourInLineBE()

    def run(self):
        try:
            while self.game.winCondition == False:
                for i in range(8):
                    for j in range(8):
                        print(self.game.board[i][j], end="")
                    print("\n")
                self.play()
        except Winner:
            Break

    def play(self):
        try:
            column = int(input('Introduzca una columna: '))
            self.game.placeToken(column)
        except ValueError:
            print("Ingrese un valor válido")
        except OutOfRange:
            print("Ingrese un nùmero entre 0 y 7")
        except Winner:
            self.game.winCondition = True
            print("¡Ganaste!")
            """ for i in range(8):
                for j in range(8):
                    print(self.game.board[i][j], end="")
                print("\n") """

if __name__ == '__main__':
    FourInLineFE().run()