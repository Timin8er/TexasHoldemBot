from deck import *

def odds_of_opponent_better_pair(river, hand1, hand2):
    """
    Return the odds that an apponent has better pair.
    """
    my_pair = -1
    board_pair = -1
    n_board_pairs = 0

    # do I have a pair in hand?
    if hand1[1] == hand2[1]:
        my_pair = hand1[1]

    # is there a pair on the board?
    for i, card1 in enumerate(river[:-1]):
        for card2 in river[i+1:]:
            if card1[1] == card2[1]:
                if card1[1] > board_pair:
                    board_pair = card1[1]
                if board_pair > my_pair:
                    my_pair = board_pair


    # if I do not have a pair, return the odds of an opponent having a pair
    # return (len(river)+2 /  )
    # 
    
    
    



