from ast import Break
import random
from cmath import exp
from typing import Collection
from fourInLineBE import FourInLineBE
from fourInLineBE import Token
from fourInLineBEException import Winner
from fourInLineBEException import NotWinner
from fourInLineBEException import OutOfRange
import pygame
from pygame.locals import *


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
            blueP = (20, 34, 238)
            greenP = (20, 240, 50)
            redP = (230, 0, 20)
            BLACK = (0, 0, 0)
            sizeSquare = 75
            pygame.init()
            size = (600, 600)
            screen = pygame.display.set_mode(size)
            screen.fill(BLACK)
            pygame.draw.rect(screen, greenP, (600, 600, 75, 75))
            self.game.placeToken(column)
        except ValueError:
            print("Ingrese un valor válido")
        except OutOfRange:
            print("Ingrese un nùmero entre 0 y 7")
        except Winner:
            self.game.winCondition = True
            for i in range(8):
                for j in range(8):
                    print(self.game.board[i][j], end="")
                print("\n")
            print("Ganaste")


if __name__ == '__main__':
    FourInLineFE().run()
