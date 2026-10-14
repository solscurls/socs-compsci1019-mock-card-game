import unittest
from unittest.mock import patch
from card_game.card.entity.Deck import *


class TestMockDeck(unittest.TestCase):

    def test_play_a_card_from_deck_random(self):
        self.Deck.play_a_card_from_deck = 0
        pass