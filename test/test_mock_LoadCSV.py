import unittest
from unittest.mock import patch, mock_open
from card_game.LoadCSV import *

class test_mock_LoadCSV(unittest.TestCase):

    def test_get_csv_rows(self):
        self.get_csv_rows = "Derek\nXi"
        pass