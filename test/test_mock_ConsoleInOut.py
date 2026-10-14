import unittest
from unittest.mock import patch
from card_game.communication.ConsoleInOut import *

class test_mock_ConsoleInOut(unittest.TestCase):

    def test_get_input_string(self, mock_input):
        pass

    def test_get_input_integer(self):
        self.get_string = 18

    def test_get_input_string_builtin(self):
        pass

    def test_get_integer_max_attempts(self):
        self.communication.ConsoleInOut.get_string = "abc"

    def test_get_input_integer_builtin(self):
        pass