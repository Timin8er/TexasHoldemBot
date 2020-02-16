from rawOdds import rawOddsCalculator
from deck import *
import random
from itertools import combinations


def test_odds_of_pair():
    """
    Compare the result of odds_of_opponent_better_pair() to a hard recursive check of all posible pairs
    """

    deck = Deck()

    river = [deck.pop_card() for i in range(random.randrange(3,6))]

    hand1 = deck.pop_card()
    hand2 = deck.pop_card()

    test_result = rawOddsCalculator.odds_of_opponent_better_pair(river, hand1, hand2)

    # determine my pair
    my_pair_value = -1
    my_pair = None
    for card1, card2 in combinations(river + [hand1, hand2], 2):
        if card1[1] == card2[1] and card1[1] > my_pair_value:
            my_pair_value = card1[1]
            my_pair = (card1, card2)

    # determine apponent pairs
    better_pairs = 0
    for i, cards in enumerate(deck.pairs_generator()):
        for card1, card2 in combinations(river + list(cards), 2):
            if card1[1] == card2[1] and card1[1] > my_pair_value:
                better_pairs += 1
                break


    print('==========================================')
    print('\tCards:\t', hand1)
    print('\t\t', hand2)
    print('\tRiver:\t', river)
    print('\tMy Pair Value:', my_pair_value)
    print('\tPairs Checked:', i)
    print('\tBetter Pairs:', better_pairs)


def test_everything(deck:Deck):
    print(' ========== Testing doubles ========== ')

    test_odds_of_pair()

