from rawOdds import rawOddsCalculator
from deck import Deck


def generate_hands(deck):
    for i in range(51):
        for j in range(i+1, 52):
            return deck._d[i], deck._d[j]



def test_doubles(deck:Deck):
    print(' ========== Testing doubles ========== ')

    river = [deck.play_card() for i in range(5)]

    print (river)




def test_everything(deck:Deck):
    test_doubles(deck)

