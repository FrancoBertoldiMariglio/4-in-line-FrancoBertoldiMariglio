import unittest
from fourInLineBE import Token
from fourInLineBE import FourInLineBE
from fourInLineBEException import Overflow
from fourInLineBEException import Winner
from parameterized import parameterized


class TestFourInLineBE(unittest.TestCase):

    def testCreateGame(self):
        game = FourInLineBE()
        self.assertEqual(game.board,
                         [['-' for _ in range(8)] for _ in range(8)])

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

    def testPlaceTokenVertcialHappy1(self):
        game = FourInLineBE()
        for i in range(3):
            game.board[7 - i][0] = 0
        with self.assertRaises(Winner):
            game.placeToken(0)

    def testPlaceTokenVertcialHappy2(self):
        game = FourInLineBE()
        game.board[7][0] = 1
        for i in range(3):
            game.board[6 - i][0] = 0
        with self.assertRaises(Winner):
            game.placeToken(0)

    @parameterized.expand([
        (
            1,
            2,
            3,
            0,
        ),
        (
            4,
            5,
            6,
            7,
        ),
        (
            0,
            2,
            3,
            1,
        ),
        (
            4,
            5,
            7,
            6,
        ),
        (
            0,
            1,
            3,
            2,
        ),
        (
            1,
            3,
            4,
            2,
        ),
        (
            1,
            2,
            4,
            3,
        ),
        (
            2,
            4,
            5,
            3,
        ),
        (
            2,
            3,
            5,
            4,
        ),
        (
            3,
            5,
            6,
            4,
        ),
        (
            4,
            6,
            7,
            5,
        ),
        (
            3,
            4,
            6,
            5,
        ),
    ])
    def testPlaceTokenHorizontalHappy0(self, a, b, c, d):
        game = FourInLineBE()
        game.board[7][a] = 0
        game.board[7][b] = 0
        game.board[7][c] = 0
        with self.assertRaises(Winner):
            game.placeToken(d)

    @parameterized.expand([
        ([5, 0], [6, 0], [7, 0], [5, 1], [6, 2], [7, 3], 0),
        ([5, 7], [6, 7], [7, 7], [5, 6], [6, 5], [7, 4], 7),
    ])
    def testPlaceTokenDiagonalHappy3DAB(self, a, b, c, d, e, f, g):
        game = FourInLineBE()
        game.board[a[0]][a[1]] = 1
        game.board[b[0]][b[1]] = 1
        game.board[c[0]][c[1]] = 1
        game.board[d[0]][d[1]] = 0
        game.board[e[0]][e[1]] = 0
        game.board[f[0]][f[1]] = 0
        with self.assertRaises(Winner):
            game.placeToken(g)

    @parameterized.expand([
        (
            [4, 0],
            [5, 0],
            [6, 0],
            [7, 0],
            [2, 1],
            [1, 2],
            [0, 3],
            0,
        ),
        (
            [4, 7],
            [5, 7],
            [6, 7],
            [7, 7],
            [2, 6],
            [1, 5],
            [0, 4],
            7,
        ),
    ])
    def testPlaceTokenDiagonalHappy3DAR(self, a, b, c, d, e, f, g, h):
        game = FourInLineBE()
        game.board[a[0]][a[1]] = 1
        game.board[b[0]][b[1]] = 1
        game.board[c[0]][c[1]] = 1
        game.board[d[0]][d[1]] = 1
        game.board[e[0]][e[1]] = 0
        game.board[f[0]][f[1]] = 0
        game.board[g[0]][g[1]] = 0
        with self.assertRaises(Winner):
            game.placeToken(h)

    @parameterized.expand([
        (
            [7, 1],
            [7, 0],
            [5, 2],
            [4, 3],
            1,
        ),
        (
            [7, 6],
            [7, 7],
            [5, 5],
            [4, 4],
            6,
        ),
    ])
    def testPlaceTokenDiagonalHappy1IAB2DAR(self, a, b, c, d, e):
        game = FourInLineBE()
        game.board[a[0]][a[1]] = 1
        game.board[b[0]][b[1]] = 0
        game.board[c[0]][c[1]] = 0
        game.board[d[0]][d[1]] = 0
        with self.assertRaises(Winner):
            game.placeToken(e)

    @parameterized.expand([
        (
            [7, 6],
            [6, 6],
            [4, 7],
            [6, 5],
            [7, 4],
            6,
        ),
        (
            [7, 1],
            [6, 1],
            [4, 0],
            [6, 2],
            [7, 3],
            1,
        ),
    ])
    def testPlaceTokenDiagonalHappy2IAB1DAR(self, a, b, c, d, e, f):
        game = FourInLineBE()
        game.board[a[0]][a[1]] = 1
        game.board[b[0]][b[1]] = 1
        game.board[c[0]][c[1]] = 0
        game.board[d[0]][d[1]] = 0
        game.board[e[0]][e[1]] = 0
        with self.assertRaises(Winner):
            game.placeToken(f)


if __name__ == '__main__':
    unittest.main()
