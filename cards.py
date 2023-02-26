import random

    """Greet text to our customers."""
witch_treehouse = input('Welcome to fortune-telling kingdom! Now your future will be explored...')


class Card:
    """All possible options which can be result of fortune-telling process."""    
    ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits

    def __str__(self):
    """Sample text for each random card."""
        return f'{self.ranks} of {self.suits}'


class Deck:
    def __init__(self):
        self.cards = [Card(suits, ranks) for ranks in Card.ranks for suits in Card.suits]

        random.shuffle(self.cards)
    """The process of cards shuffle from cards"""

    def deal(self):
    """Getting the access to the variable of cards set"""
        return self.cards.pop()
    """Get rid off first card and get back the last in the deck"""

