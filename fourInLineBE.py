from fourInLineBEException import Overflow
from fourInLineBEException import Winner
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
        self.board = [['-' for _ in range(8)] for _ in range(8)]
        self.token = Token()
        self.winCondition = False

    def placeToken(self, column):
        if column in [0, 1, 2, 3, 4, 5, 6, 7]:
            row = self.emptySpace(column)
            self.board[row][column] = self.token.colour
            if row <= 4:
                self.checkForVerticalWinner(column)
            self.checkForHorizontalWinner(row)
            self.checkForDiagonalWinner(row, column)
            self.token.changeColour()
        else:
            raise OutOfRange

    def emptySpace(self, column):
        for i in range(8):
            if self.board[7 - i][column] == '-':
                return 7 - i

        raise Overflow('La columna está llena')

    def checkForVerticalWinner(self, column):
        contador = 0
        for i in range(8):
            if contador == 4:
                raise Winner("Ganaste")
            if self.board[7 - i][column] == self.token.colour:
                contador += 1
                if contador == 4:
                    raise Winner("Ganaste")
                continue
            contador = 0

    def checkForHorizontalWinner(self, row):
        contador = 0
        for i in range(8):
            if contador == 4:
                raise Winner("Ganaste")
            if self.board[row][i] == self.token.colour:
                contador += 1
                if contador == 4:
                    raise Winner("Ganaste")
                continue
            contador = 0

    def cellToBeginPrincipal(self, row, column):
        if row >= column:
            return [row - column, 0]
        return [0, column - row]

    def cellToBeginSecundaria(self, row, column):
        if row >= 7 - column:
            return [abs(7 - column - row), 7]
        return [0, column + row]

    def diagonalPrincipal(self, row, column):
        vector_principal = [[5, 0], [6, 0], [7, 0], [6, 1], [7, 1], [7, 2],
                            [0, 5], [0, 6], [0, 7], [1, 6], [1, 7], [2, 7]]
        if [row, column] not in vector_principal:
            lugar_donde_empezar = self.cellToBeginPrincipal(row, column)
            i = lugar_donde_empezar[0]
            h = lugar_donde_empezar[1]
            contador = 0
            while i < 8 and h < 8:
                if self.board[i][h] == self.token.colour:
                    contador += 1
                else:
                    contador = 0
                if contador == 4:
                    raise Winner('Ganaste!')
                i += 1
                h += 1

    def diagonalSecundario(self, row, column):
        vector_secundario = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [2, 0],
                             [7, 5], [7, 6], [7, 7], [6, 6], [6, 7], [5, 7]]
        if [row, column] not in vector_secundario:
            lugar_donde_empezar = self.cellToBeginSecundaria(row, column)
            i = lugar_donde_empezar[0]
            h = lugar_donde_empezar[1]
            contador = 0
            while i < 8 and h < 8:
                if self.board[i][h] == self.token.colour:
                    contador += 1
                else:
                    contador = 0
                if contador == 4:
                    raise Winner('Ganaste!')
                i += 1
                h -= 1

    def checkForDiagonalWinner(self, row, column):
        self.diagonalPrincipal(row, column)
        self.diagonalSecundario(row, column)
