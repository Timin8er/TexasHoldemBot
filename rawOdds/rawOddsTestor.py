from rawOdds import rawOddsCalculator
from deck import *
import random
from itertools import combinations

STREIGHT_FLUSH = 0
FOUR_OF_A_KIND = 1
FULL_HOUSE = 2
FLUSH = 3
STREIGHT = 4
THREE_OF_A_KIND = 5
TWO_PAIR = 6
PAIR = 7
HIGH_CARD_1 = 8
HIGH_CARD_2 = 9


test_cases = [
    # [(0,9),(1,9)], # pair in hand
    # [(0,6),(1,7),(2,8),(3,9),(0,10)], # streight
    [(0,3),(0,6),(1,3),(2,3),(3,9)] # 3 of a kind
]


def test_odds_of_pair():
    """
    Compare the result of odds_of_opponent_better_pair() to a hard recursive check of all posible pairs
    """

    deck = Deck()

    river = [deck.pop_card() for i in range(random.randrange(3,6))]

    hand1 = deck.pop_card()
    hand2 = deck.pop_card()

    cards = [hand1, hand2] + river

    print(has_hands(cards))

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
    print(' ========== Testings ========== ')

    # test_odds_of_pair()

    for t in test_cases:
        deck = Deck()

        my_cards = [deck.pop(*j) for j in t]
        print(my_cards)
        my_hand_r = hand_rank(my_cards)
        print(my_hand_r)

        # for each posible pair an apponent has
        better_pairs = 0
        for pairs_checked, opp_cards in enumerate(deck.pairs_generator()):

            # get their hand_rank
            hand_r = hand_rank(list(opp_cards) + my_cards[2:])

            # for each index in hand_ranks
            for i, j in zip(my_hand_r, hand_r):
                # if my hand is better, break
                if i > j:
                    break
                # if their hand is better break
                elif i < j:
                    better_pairs += 1
                    break

        print(better_pairs, '/', pairs_checked)




def hand_rank(cards:list):

    igot = [-1] * 10

    # tally the number of each card rank and suit we have
    rank_accumulations = [0] * 13
    suit_accumilations = [0] * 4
    for c in cards:
        rank_accumulations[c[1]] += 1
        suit_accumilations[c[0]] += 1

    # tally all x of a kind
    accumulation_counts = [0] * 5
    for i, acc in enumerate(rank_accumulations):
        accumulation_counts[acc] += 1

        if acc == 4 and i > igot[FOUR_OF_A_KIND]:
            igot[1] = i

        elif acc == 3 and i > igot[THREE_OF_A_KIND]:
            igot[5] = i

        elif acc == 2 and i > igot[PAIR]:
            igot[7] = i

    # look for flush
    for i in suit_accumilations:
        if i >= 5:
            igot[FLUSH] = i

    # look for streight
    iterer = 0
    for i, c in enumerate(rank_accumulations):
        if c:
            iterer += 1
            if iterer >= 5:
                igot[STREIGHT] = i
        else:
            iterer = 0

    # look for streight flush
    #TODO: account for the 5 card limit if the flush and streight use different cards
    if igot[STREIGHT] >= 0 and igot[FLUSH] >= 0:
        igot[STREIGHT_FLUSH] = igot[STREIGHT]

    # look for full house
    #TODO: account for the 5 card limie
    if accumulation_counts[2] + accumulation_counts[3] >= 2:
        igot[FULL_HOUSE] = igot[THREE_OF_A_KIND]

    # look for two pair
    if accumulation_counts[2] >= 2:
        igot[TWO_PAIR] = igot[PAIR]

    # high card
    ## TODO: account for cards unable to be counted towards this due to 5 card max
    igot[HIGH_CARD_1] = max(cards[0][1], cards[1][1])
    igot[HIGH_CARD_2] = min(cards[0][1], cards[1][1])

    return igot
