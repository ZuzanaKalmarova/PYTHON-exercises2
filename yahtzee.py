"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    
    score_list = list()
    for side in set(hand):
        side_score = hand.count(side)*side
        score_list.append(side_score)
    return max(score_list)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    sides = range(1, num_die_sides + 1)
    rolls = gen_all_sequences(sides,num_free_dice)
    prob = 1.0/len(rolls)
    exp_value = 0.0
    for roll in rolls:
        hand = held_dice + roll
        exp_value += score(hand) * prob
    return exp_value


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    handlist = list(hand)
    hold_set = set([()])
    ans_set = set([()])
    for dummy in range(len(hand)):
        temp_set = set()
        for seq in ans_set:
            for seqitem in seq:
                if seqitem in handlist:
                    handlist.remove(seqitem)
            for item in handlist:
                new_seq = list(seq)
                new_seq.append(item)
                temp_set.add(tuple(sorted(new_seq)))
            handlist = list(hand)
        ans_set = temp_set
        hold_set.update(ans_set)
    return hold_set



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    hold_set = gen_all_holds(hand)
    max_exp_val = 0
    for hold in hold_set:
        num_free_dice = len(hand) - len(hold)
        exp_val = expected_value(hold, num_die_sides, num_free_dice)
        if exp_val > max_exp_val:
            max_exp_val = exp_val
            hold_dice = hold   
    return (max_exp_val, hold_dice)

#def run_example():
#    """
#    Compute the dice to hold and expected score for an example hand
#    """
#    num_die_sides = 6
#    hand = (1, 1, 1, 5, 6)
#    hand_score, hold = strategy(hand, num_die_sides)
#    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
#    
#    
#run_example()

#print score((1,2,4,4,6))

#print expected_value((2,2),6,2)

#hand = (1,1,2,3,4)
#gen_all_holds(hand)




#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



