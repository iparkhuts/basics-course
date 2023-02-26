from cards import Card, Deck
import random

def main():
    """Function main is calling constructor of the Deck class"""
    N = 3
    deck = Deck()
    deck.shuffle()
    """Shuffling the deck of cards"""
    print(f'Fortune Teller greets you! Your future is written with {N}')
    for i in range(N):
    """Loop for choosing random cards from the deck"""
        card = deck.deal()
        print(card)

if __name__=='__main__':
    main()
