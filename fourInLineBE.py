from calendar import c
from fourInLineBEException import Overflow
from fourInLineBEException import Winner
from fourInLineBEException import NotWinner
from fourInLineBEException import OutOfRange


class Token():

    def __init__(self):
        self.colour = 0

    def changeColour(self):
        if self.colour == 0:
            self.colour = 1
        elif self.colour == 1:
            self.colour = 0


class FourInLineBE:

    def __init__(self):
        self.board = [[' - ' for _ in range(8)] for _ in range(8)]
        self.token = Token()
        self.winCondition = False

    def placeToken(self, column):
        if column in [0, 1, 2, 3, 4, 5, 6, 7]:
            row = self.emptySpace(column)
            self.board[row][column] = self.token.colour
            if row <= 4:
                self.checkForVerticalWinner(row, column)
            self.checkForHorizontalWinner(row)
            self.checkForDiagonalWinner(row, column)
            self.token.changeColour()
        else:
            raise OutOfRange

    def emptySpace(self, column):
        for i in range(8):
            if self.board[7 - i][column] == ' - ':
                return 7 - i
        raise Overflow('La columna está llena')

    """ def checkForVerticalWinner(self, row, column):
        contador = 0
        for i in range(3):
            if self.board[row + i + 1][column] == self.token.colour:
                contador += 1
        if contador == 3:
            raise Winner('Ganaste!') 

    def checkForHorizontalWinner(self, row, column):
        contador = 0
        if column == 0:
            for i in range(3):
                if self.board[row][column + i + 1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        if column == 7:
            for i in range(3):
                if self.board[row][column - i - 1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        if column == 1:
            if self.board[row][column - 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row][column + i + 1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        if column == 6:
            if self.board[row][column + 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row][column - i - 1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        if column in [2, 3, 4, 5]:
            if self.board[row][column + 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row][column - i - 1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
            contador = 0
            if self.board[row][column - 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row][column + i + 1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')   """
 
    def checkForDiagonalWinner(self, row, column):
        contador = 0
        if row in [0, 1, 2, 3, 4] and column in [0, 1, 2, 3, 4]:
            for i in range(3):
                if self.board[row + i + 1][column + i +
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')

        if row in [0, 1, 2, 3, 4] and column in [3, 4, 5, 6, 7]:
            for i in range(3):
                if self.board[row + i + 1][column - i -
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')

        if row in [3, 4, 5, 6, 7] and column in [0, 1, 2, 3, 4]:
            for i in range(3):
                if self.board[row - i - 1][column + i +
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')

        if row in [3, 4, 5, 6, 7] and column in [3, 4, 5, 6, 7]:
            for i in range(3):
                if self.board[row - i - 1][column - i -
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        contador = 0
        if row in [2, 3, 4, 5, 6] and column in [1, 2, 3, 4, 5]:
            if self.board[row + 1][column - 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row - i - 1][column + i +
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        contador = 0
        if row in [2, 3, 4, 5, 6] and column in [2, 3, 4, 5, 6]:
            if self.board[row + 1][column + 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row - i - 1][column - i -
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        contador = 0
        if row in [1, 2, 3, 4, 5] and column in [2, 3, 4, 5, 6]:
            if self.board[row - 1][column + 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row + i + 1][column - i -
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')
        contador = 0
        if row in [1, 2, 3, 4, 5] and column in [1, 2, 3, 4, 5]:
            if self.board[row - 1][column - 1] == self.token.colour:
                contador = contador + 1
            for i in range(2):
                if self.board[row + i + 1][column + i +
                                           1] == self.token.colour:
                    contador = contador + 1
                if contador == 3:
                    raise Winner('Ganaste!')

    def checkForVerticalWinner(self, row, column):
        contador = 0
        for i in range(7 - row + 1):
            if self.board[row + i][column] != self.token.colour:
                contador = 0
            contador += 1
        if contador == 4:
            raise Winner("Ganaste") 

    def checkForHorizontalWinner(self, row):
        contador = 0
        for i in range(8):
            if contador == 4:
                raise Winner("Ganaste")
                break 
            if self.board[row][i] == self.token.colour:
                contador += 1
                continue
            contador = 0
       


    def diagonal(self, row, column):  #chequear
        contador = 0

        if column > 4 and row > 4:
            rowToUse = 0
            colToUse = abs(row - column)
            for i in range(8 - colToUse):
                if self.board[i][i] != self.token.colour:
                    contador = 0
                    continue
                contador += 1
        if contador == 4:
            raise Winner("Ganaste")

        elif column < 4 and row < 4:
            rowToUse = abs(row - column)
            colToUse = 0
            for i in range(8 - rowToUse):
                if self.board[i][i] != self.token.colour:
                    contador = 0
                    continue
                contador += 1
        if contador == 4:
            raise Winner("Ganaste")

        elif row == 0 and column == 0:
            rowToUse = 0
            colToUse = 0
            for i in range(8):
                if self.board[i][i] != self.token.colour:
                    contador = 0
                    continue
                contador += 1
        if contador == 4:
            raise Winner("Ganaste")
