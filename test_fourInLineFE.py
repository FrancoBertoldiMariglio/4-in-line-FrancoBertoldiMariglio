import unittest
from unittest.mock import patch
from fourInLineFE import FourInLineFE


class TestFourInLineFE(unittest.TestCase):

    def test_InputSad(self):
        game = FourInLineFE()
        with patch('builtins.input', side_effect=['a', 'c', '$', '#', '/']):
            with patch('builtins.print') as patch_print:
                game.play()
                patch_print.assert_called_once_with('Ingrese un valor válido')

    def test_InputHappy(self):
        game = FourInLineFE()
        game.game.board[7][0] = 0
        game.game.board[6][0] = 0
        game.game.board[5][0] = 0
        with patch('builtins.input', return_value=0):
            with patch('builtins.print') as patch_print:
                game.play()
                patch_print.assert_called_once_with('Ganaste')


if __name__ == '__main__':
    unittest.main()
