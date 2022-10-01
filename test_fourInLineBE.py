import unittest
from fourInLineBE import Token
from fourInLineBE import FourInLineBE
from fourInLineBEException import Overflow
from fourInLineBEException import Winner
from fourInLineBEException import NotWinner
from fourInLineBEException import OutOfRange


class TestFourInLineBE(unittest.TestCase):

    """ def testCreateGame(self):
        game = FourInLineBE()
        self.assertEqual(game.board,
                         [[' - ' for _ in range(8)] for _ in range(8)])

    def testToken(self):
        token = Token()
        self.assertEqual(token.colour, 0)

    def testChangeColour(self):
        token = Token()
        token.changeColour()
        self.assertEqual(token.colour, 1)

    def testChangeColourInverse(self):
        token = Token()
        token.colour = 1
        token.changeColour()
        self.assertEqual(token.colour, 0)

    def testEmptySpaceHappy(self):
        game = FourInLineBE()
        row = game.emptySpace(1)
        self.assertEqual(row, 7)

    def testEmptySpaceHappy2(self):
        game = FourInLineBE()
        game.board[7][1] = 0
        row = game.emptySpace(1)
        self.assertEqual(row, 6)

    def testEmptySpaceSad(self):
        game = FourInLineBE()
        for i in range(8):
            game.board[7 - i][1] = 0
        with self.assertRaises(Overflow):
            game.emptySpace(1)

    def testPlaceTokenVertcialHappy(self):
        game = FourInLineBE()
        for i in range(3):
            game.board[7 - i][0] = 0
        with self.assertRaises(Winner):
            game.placeToken(0) """

    """ def testPlaceTokenHorizontalHappy0(self):
        game = FourInLineBE()
        for i in range(3):
            game.board[7][i + 1] = 0
        with self.assertRaises(Winner):
            game.placeToken(0)

    def testPlaceTokenHorizontalHappy7(self):
        game = FourInLineBE()
        for i in range(3):
            game.board[7][7 - i - 1] = 0
        with self.assertRaises(Winner):
            game.placeToken(7)

    def testPlaceTokenHorizontalHappy1(self):
        game = FourInLineBE()
        game.board[7][0] = 0
        game.board[7][2] = 0
        game.board[7][3] = 0
        with self.assertRaises(Winner):
            game.placeToken(1)

    def testPlaceTokenHorizontalHappy6(self):
        game = FourInLineBE()
        game.board[7][7] = 0
        game.board[7][5] = 0
        game.board[7][4] = 0
        with self.assertRaises(Winner):
            game.placeToken(6)

    def testPlaceTokenHorizontalHappy21(self):
        game = FourInLineBE()
        game.board[7][0] = 0
        game.board[7][1] = 0
        game.board[7][3] = 0
        with self.assertRaises(Winner):
            game.placeToken(2)

    def testPlaceTokenHorizontalHappy22(self):
        game = FourInLineBE()
        game.board[7][1] = 0
        game.board[7][3] = 0
        game.board[7][4] = 0
        with self.assertRaises(Winner):
            game.placeToken(2)

    def testPlaceTokenHorizontalHappy31(self):
        game = FourInLineBE()
        game.board[7][1] = 0
        game.board[7][2] = 0
        game.board[7][4] = 0
        with self.assertRaises(Winner):
            game.placeToken(3)

    def testPlaceTokenHorizontalHappy32(self):
        game = FourInLineBE()
        game.board[7][2] = 0
        game.board[7][4] = 0
        game.board[7][5] = 0
        with self.assertRaises(Winner):
            game.placeToken(3)

    def testPlaceTokenHorizontalHappy41(self):
        game = FourInLineBE()
        game.board[7][2] = 0
        game.board[7][3] = 0
        game.board[7][5] = 0
        with self.assertRaises(Winner):
            game.placeToken(4)

    def testPlaceTokenHorizontalHappy42(self):
        game = FourInLineBE()
        game.board[7][3] = 0
        game.board[7][5] = 0
        game.board[7][6] = 0
        with self.assertRaises(Winner):
            game.placeToken(4) """

    def testPlaceTokenHorizontalHappy51(self):
        game = FourInLineBE()
        game.board[7][4] = 0
        game.board[7][6] = 0
        game.board[7][7] = 0
        with self.assertRaises(Winner):
            game.placeToken(5)

    """def testPlaceTokenHorizontalHappy52(self):
        game = FourInLineBE()
        game.board[7][3] = 0
        game.board[7][4] = 0
        game.board[7][6] = 0
        with self.assertRaises(Winner):
            game.placeToken(5) """

"""     def testPlaceTokenDiagonalHappy3DAB(self):
        game = FourInLineBE()
        game.board[5][0] = 1
        game.board[6][0] = 1
        game.board[7][0] = 1
        game.board[5][1] = 0
        game.board[6][2] = 0
        game.board[7][3] = 0
        with self.assertRaises(Winner):
            game.placeToken(0)

    def testPlaceTokenDiagonalHappy3IAB(self):
        game = FourInLineBE()
        game.board[5][7] = 1
        game.board[6][7] = 1
        game.board[7][7] = 1
        game.board[5][6] = 0
        game.board[6][5] = 0
        game.board[7][4] = 0
        with self.assertRaises(Winner):
            game.placeToken(7)

    def testPlaceTokenDiagonalHappy3DAR(self):
        game = FourInLineBE()
        game.board[4][0] = 1
        game.board[5][0] = 1
        game.board[6][0] = 1
        game.board[7][0] = 1
        game.board[2][1] = 0
        game.board[1][2] = 0
        game.board[0][3] = 0
        with self.assertRaises(Winner):
            game.placeToken(0)

    def testPlaceTokenDiagonalHappy3IAR(self):
        game = FourInLineBE()
        game.board[4][7] = 1
        game.board[5][7] = 1
        game.board[6][7] = 1
        game.board[7][7] = 1
        game.board[2][6] = 0
        game.board[1][5] = 0
        game.board[0][4] = 0
        with self.assertRaises(Winner):
            game.placeToken(7)

    def testPlaceTokenDiagonalHappy1IAB2DAR(self):
        game = FourInLineBE()
        game.board[7][1] = 1
        game.board[7][0] = 0
        game.board[5][2] = 0
        game.board[4][3] = 0
        with self.assertRaises(Winner):
            game.placeToken(1)

    def testPlaceTokenDiagonalHappy1DAB2IAR(self):
        game = FourInLineBE()
        game.board[7][6] = 1
        game.board[7][7] = 0
        game.board[5][5] = 0
        game.board[4][4] = 0
        with self.assertRaises(Winner):
            game.placeToken(6)

    def testPlaceTokenDiagonalHappy2IAB1DAR(self):
        game = FourInLineBE()
        game.board[7][6] = 1
        game.board[6][6] = 1
        game.board[4][7] = 0
        game.board[6][5] = 0
        game.board[7][4] = 0
        with self.assertRaises(Winner):
            game.placeToken(6)

    def testPlaceTokenDiagonalHappy2DAB1IAR(self):
        game = FourInLineBE()
        game.board[7][1] = 1
        game.board[6][1] = 1
        game.board[4][0] = 0
        game.board[6][2] = 0
        game.board[7][3] = 0
        with self.assertRaises(Winner):
            game.placeToken(1)
 """

if __name__ == '__main__':
    unittest.main()
