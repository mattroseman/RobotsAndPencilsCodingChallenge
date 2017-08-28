import unittest

from Rank import Rank
from Suit import Suit
from Card import Card
from Deck import Deck


class TestDeck(unittest.TestCase):

    def test_construction(self):
        deck = Deck([Card(Rank.ace, Suit.clubs),
                     Card(Rank.eight, Suit.hearts),
                     Card(Rank.king, Suit.hearts),
                     Card(Rank.king, Suit.diamonds)])

    def test_all_invalid_cards(self):
        with self.assertRaises(TypeError):
            deck = Deck(Card(Rank.ace, Suit.hearts))

    def test_one_invalid_card(self):
        with self.assertRaises(TypeError):
            deck = Deck([Card(Rank.ace, Suit.clubs),
                         Card(Rank.eight, Suit.hearts),
                         "king of hearts",
                         Card(Rank.king, Suit.diamonds)])

    def test_deal_card(self):
        deck = Deck([Card(Rank.ace, Suit.clubs),
                     Card(Rank.eight, Suit.hearts),
                     Card(Rank.king, Suit.hearts),
                     Card(Rank.king, Suit.diamonds)])

        self.assertEqual(deck.deal_card(), Card(Rank.ace, Suit.clubs))

    def test_empty_deck_deal_card(self):
        deck = Deck([])
        self.assertEqual(deck.deal_card(), None)

        deck = Deck()
        self.assertEqual(deck.deal_card(), None)

    def test_shuffle(self):
        # There is always a chance that shuffling the deck will result in the same configuration,
        # so I have tested this shuffling function manually (besided checking that it doesn't
        # throw errors here
        deck = Deck([Card(Rank.ace, Suit.clubs),
                     Card(Rank.eight, Suit.hearts),
                     Card(Rank.king, Suit.hearts),
                     Card(Rank.king, Suit.diamonds)])
        deck.shuffle()

    def test_string_conversion(self):
        deck = Deck([Card(Rank.ace, Suit.clubs),
                     Card(Rank.eight, Suit.hearts),
                     Card(Rank.king, Suit.hearts),
                     Card(Rank.king, Suit.diamonds)])

        self.assertEqual(str(deck), 'ace of clubs\neight of hearts\nking of hearts\nking of diamonds')


if __name__ == '__main__':
    unittest.main()
