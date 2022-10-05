import unittest
from unittest.mock import patch
from fourInLineFE import FourInLineFE


class TestFourInLineFE(unittest.TestCase):

    def test_InputSad1(self):
        game = FourInLineFE()
        with patch('builtins.input', side_effect=['a', 'c', '$', '#', '/']):
            with patch('builtins.print') as patch_print:
                game.play()
                patch_print.assert_called_once_with('Ingrese un valor válido')

    def test_InputSad2(self):
        game = FourInLineFE()
        with patch('builtins.input', return_value=9):
            with patch('builtins.print') as patch_print:
                game.play()
                patch_print.assert_called_once_with(
                    "Ingrese un nùmero entre 1 y 8")

    def test_InputHappyWin(self):
        game = FourInLineFE()
        game.game.board[7][0] = 0
        game.game.board[6][0] = 0
        game.game.board[5][0] = 0
        with patch('builtins.input', return_value=1):
            with patch('builtins.print') as patch_print:
                game.play()
                patch_print.assert_any_call("¡Ganaste!")


if __name__ == '__main__':
    unittest.main()