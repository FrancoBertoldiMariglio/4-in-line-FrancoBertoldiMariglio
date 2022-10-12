import unittest
from unittest.mock import patch
from fourInLineFE import FourInLineFE


class TestFourInLineFE(unittest.TestCase):

    def test_InputSad1(self):
        FE = FourInLineFE()
        with patch('builtins.input', side_effect=['a', 'c', '$', '#', '/']):
            with patch('builtins.print') as patch_print:
                FE.play()
                patch_print.assert_called_once_with('Ingrese un valor válido')

    def test_InputSad2(self):
        FE = FourInLineFE()
        with patch('builtins.input', return_value=9):
            with patch('builtins.print') as patch_print:
                FE.play()
                patch_print.assert_called_once_with(
                    "Ingrese un nùmero entre 1 y 8")

    def test_InputHappyWin(self):
        FE = FourInLineFE()
        FE.BE.board[7][0] = 0
        FE.BE.board[6][0] = 0
        FE.BE.board[5][0] = 0
        with patch('builtins.input', return_value=1):
            with patch('builtins.print') as patch_print:
                FE.play()
                patch_print.assert_any_call("¡Gano el jugador: " + str(FE.BE.token.colour) + "!")


if __name__ == '__main__':
    unittest.main()
