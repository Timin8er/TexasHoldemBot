import collections
import random
from itertools import combinations

Card = collections.namedtuple('Card', 'suit index')

def deckGenerator():
    """
    Loop throuh all cards in a standard deck
    """
    for s in range(4):
        for i in range(13):
            yield Card(s,i)


class Deck():
    """
    Container for a deck of cards
    """

    _d = [i for i in deckGenerator()]

    def __init__(self):
        pass
    

    def __len__(self):
        return len(self._d)


    def pairs_generator(self):
        return combinations(self._d, 2)


    def pop_card(self):
        return self._d.pop(random.randrange(len(self._d)))
    

    def return_card(self, card):
        if card not in self._d:
            self._d.append(card)

