from Card import Card
from Rank import Rank
from Suit import Suit
import random
import time


class Deck:
    """
    Deck represents a group of cards
    """

    # standard_deck is the standard 52 card deck that playing cards come in
    standard_deck = [
        Card(Rank.ace, Suit.clubs),
        Card(Rank.two, Suit.clubs),
        Card(Rank.three, Suit.clubs),
        Card(Rank.four, Suit.clubs),
        Card(Rank.five, Suit.clubs),
        Card(Rank.six, Suit.clubs),
        Card(Rank.seven, Suit.clubs),
        Card(Rank.eight, Suit.clubs),
        Card(Rank.nine, Suit.clubs),
        Card(Rank.ten, Suit.clubs),
        Card(Rank.jack, Suit.clubs),
        Card(Rank.queen, Suit.clubs),
        Card(Rank.king, Suit.clubs),
        Card(Rank.ace, Suit.diamonds),
        Card(Rank.two, Suit.diamonds),
        Card(Rank.three, Suit.diamonds),
        Card(Rank.four, Suit.diamonds),
        Card(Rank.five, Suit.diamonds),
        Card(Rank.six, Suit.diamonds),
        Card(Rank.seven, Suit.diamonds),
        Card(Rank.eight, Suit.diamonds),
        Card(Rank.nine, Suit.diamonds),
        Card(Rank.ten, Suit.diamonds),
        Card(Rank.jack, Suit.diamonds),
        Card(Rank.queen, Suit.diamonds),
        Card(Rank.king, Suit.diamonds),
        Card(Rank.ace, Suit.hearts),
        Card(Rank.two, Suit.hearts),
        Card(Rank.three, Suit.hearts),
        Card(Rank.four, Suit.hearts),
        Card(Rank.five, Suit.hearts),
        Card(Rank.six, Suit.hearts),
        Card(Rank.seven, Suit.hearts),
        Card(Rank.eight, Suit.hearts),
        Card(Rank.nine, Suit.hearts),
        Card(Rank.ten, Suit.hearts),
        Card(Rank.jack, Suit.hearts),
        Card(Rank.queen, Suit.hearts),
        Card(Rank.king, Suit.hearts),
        Card(Rank.ace, Suit.spades),
        Card(Rank.two, Suit.spades),
        Card(Rank.three, Suit.spades),
        Card(Rank.four, Suit.spades),
        Card(Rank.five, Suit.spades),
        Card(Rank.six, Suit.spades),
        Card(Rank.seven, Suit.spades),
        Card(Rank.eight, Suit.spades),
        Card(Rank.nine, Suit.spades),
        Card(Rank.ten, Suit.spades),
        Card(Rank.jack, Suit.spades),
        Card(Rank.queen, Suit.spades),
        Card(Rank.king, Suit.spades)]

    def __init__(self, cards=[]):
        """
        @param cards: a list of Card objects representing the initial cards in the deck, and the initial ordering
        """
        if not isinstance(cards, list):
            raise TypeError("cards must be a list")
        if not all(isinstance(card, Card) for card in cards):
            raise TypeError("Each card in cards must be of type Card")

        self._deck = cards

    def shuffle(self):
        """
        shuffle randomly rearranges the order of all the cards in this deck.
        The algorithm used is the Fisher-Yates shuffle, which is done in place in O(n) time
        """
        random.seed(time.time())

        for i in range(len(self._deck) - 1, 0, -1):
            j = random.randrange(0, i + 1)
            self._deck[i], self._deck[j] = self._deck[j], self._deck[i]

    def deal_card(self):
        """
        deal_card will remove the first card of the deck and return it
        @return: a Card type that was the first card of the deck, or None if the deck is empty
        """
        if len(self._deck) == 0:
            return None
        card = self._deck[0]
        self._deck = self._deck[1:]
        return card

    def __str__(self):
        return '\n'.join(str(card) for card in self._deck)
