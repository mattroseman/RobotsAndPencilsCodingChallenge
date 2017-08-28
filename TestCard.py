import unittest

from Rank import Rank
from Suit import Suit
from Card import Card


class TestCard(unittest.TestCase):

    def test_construction(self):
        card = Card(Rank.ace, Suit.hearts)
        self.assertEqual(card.rank, Rank.ace)
        self.assertEqual(card.suit, Suit.hearts)

    def test_bad_rank_construction(self):
        with self.assertRaises(TypeError):
            card = Card('ace', Suit.hearts)

        with self.assertRaises(TypeError):
            card = Card(1, Suit.hearts)

    def test_bad_suit_construction(self):
        with self.assertRaises(TypeError):
            card = Card(Rank.nine, 'hearts')

        with self.assertRaises(TypeError):
            card = Card(Rank.nine, 3)

    def test_equal_cards(self):
        card1 = Card(Rank.nine, Suit.hearts)
        card2 = Card(Rank.nine, Suit.hearts)
        self.assertTrue(card1 == card2)

    def test_not_equal_suit_cards(self):
        card1 = Card(Rank.nine, Suit.hearts)
        card2 = Card(Rank.nine, Suit.clubs)
        self.assertTrue(card1 != card2)

    def test_not_equal_rank_cards(self):
        card1 = Card(Rank.nine, Suit.hearts)
        card2 = Card(Rank.ten, Suit.hearts)
        self.assertTrue(card1 != card2)

    def test_string_conversion(self):
        card = Card(Rank.ace, Suit.hearts)
        self.assertEqual(str(card), 'ace of hearts')


if __name__ == '__main__':
    unittest.main()
