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

    def __init__(self):
        self._d = [i for i in deckGenerator()]


    def __len__(self):
        return len(self._d)


    def pop(self, index1:int, index2:int = None):
        """
        pops and returns the card at index1 or the cards with suit=index1 and rank=index2
        """
        if index2 is None:
            if index1 >= len(self._d):
                raise ValueError('Deck index out of range: %s, max: %s' % (index1, len(self._d)))
            return self._d.pop(index1)

        # start at the initial index of the card
        i = 13*index1 + index2
        # while we havn't foind the card yet, decrement i
        while i >= len(self._d) or self._d[i][0] != index1 or self._d[i][1] != index2:
            i -= 1
            if i < 0:
                raise ValueError('Card Not Found: (%s, %s)' % (index1, index2))

        # return the card at i
        return self._d.pop(i)


    def pairs_generator(self):
        return combinations(self._d, 2)


    def pop_card(self):
        return self._d.pop(random.randrange(len(self._d)))


    def return_card(self, card):
        if card not in self._d:
            self._d.append(card)
