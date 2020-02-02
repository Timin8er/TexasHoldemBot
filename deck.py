import collections
import random

Card = collections.namedtuple('Card', 'suit index')

class Deck():

    _d = []

    for s in range(4):
        for i in range(13):
            _d.append(Card(s,i))
    

    def __init__(self):
        pass
    

    def __iter__(self):
        return self._d.__iter__()


    def play_card(self):
        
        while True:
            c = self._d[random.randint(0,51)]

            if not c[2]:
                c[2] = True
                return c

