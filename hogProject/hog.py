"""The Game of Hog."""


from random import randint
GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

# Taking turns

def roll_dice(num_rolls, dice=6):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:        A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    assert type(dice) == int and dice >= 1, 'Illegal value for sides'
    total = 0
    for i in range(0,num_rolls):
     roll = randint(1, dice)
     #check for rolling a 1
     if roll == 1:
      total = 1
      break
     total += roll
    return total


def take_turn(num_rolls, opponent_score, dice=6):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:               A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    "*** YOUR CODE HERE ***"

    # check for free bacon

    if num_rolls == 0:
     # return largest digit in opponent_string
     return max( int(i) for i in str(opponent_score)) + 1
    else:
     return roll_dice(num_rolls, dice=dice)

# Playing a game

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).

    >>> select_dice(4, 24) == four_sided
    True
    >>> select_dice(16, 64) == six_sided
    True
    >>> select_dice(0, 0) == four_sided
    True
    """
    "*** YOUR CODE HERE ***"
    if (score+opponent_score)%7 == 0:
     # hog wild
     return 4
    else:
     return 6

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    score, opponent_score = 0, 0
    "*** YOUR CODE HERE ***"
    while score < goal and opponent_score < goal:
     if who == 0:
      #use strategy 0
      num_rolls = strategy0(score,opponent_score)
     else:
      #use strategy 1
      num_rolls = strategy1(score,opponent_score)
     #num_rolls has been defined

     score += take_turn(num_rolls, opponent_score, select_dice(score, opponent_score))
     who = other(who)
     if score*2 != opponent_score and opponent_score*2 != score:
      score,opponent_score = opponent_score,score

    if who == 0:
     return score, opponent_score
    if who == 1:
     return opponent_score,score
     #Swine swap should be added


#######################
# Phase 2: Strategies #
#######################

# Basic Strategy

BASELINE_NUM_ROLLS = 6 # avg of 8.7
BASELINE_NUM_ROLLS_FOUR_SIDE = 4 # avg of 4.48
BACON_MARGIN = 9
BACON_MARGIN_FOUR_SIDE = 5
global roll_a_heck_ton
roll_a_heck_ton = BASELINE_NUM_ROLLS
global diff_scores_change_strat
diff_scores_change_strat = 0

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
     return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=10000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    "*** YOUR CODE HERE ***"

    def avgfn(*args):
        total = 0
        for i in range(0, num_samples):
            total += fn(*args)
        total = total/num_samples
        return total
    return avgfn



def max_scoring_num_rolls(dice=6):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Print all averages as in
    the doctest below.  Assume that dice always returns positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    1 dice scores 3.0 on average
    2 dice scores 6.0 on average
    3 dice scores 9.0 on average
    4 dice scores 12.0 on average
    5 dice scores 15.0 on average
    6 dice scores 18.0 on average
    7 dice scores 21.0 on average
    8 dice scores 24.0 on average
    9 dice scores 27.0 on average
    10 dice scores 30.0 on average
    10
    """
    "*** YOUR CODE HERE ***"
    max_num_rolls=0
    max_roll=0
    for i in range (1,11):
        current_avg = make_averaged(roll_dice)(i, dice)
        print(i, " dice scores ", current_avg, "on average")
        if current_avg > max_roll:
            max_num_rolls,max_roll = i,current_avg
    return max_num_rolls


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    #could implement actual average by doing multiple runs for every run instead of only calling play once
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
     return 0
    else:
     return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
     six_sided_max = max_scoring_num_rolls(6)
     print('Max scoring num rolls for six-sided dice:', six_sided_max)
     four_sided_max = max_scoring_num_rolls(4)
     print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
     print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
     print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
     print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True: # Change to True to test final_strategy
        max_winrate = 0
        list_of_heck = []
        for diff_scores in range (0,20):
            for heck_ton in range (5,11):
                diff_scores_change_strat = diff_scores
                roll_a_heck_ton = heck_ton
                current_winrate = average_win_rate(final_strategy)
                if current_winrate > max_winrate:
                    max_winrate = current_winrate
                    list_of_heck = []
                    list_of_heck.append(diff_scores)
                    list_of_heck.append(heck_ton)
                print(diff_scores_change_strat,' ', heck_ton, ' Final_strategy win rate:', current_winrate)
        print("\nMAX: ", max_winrate, "\nDIFF: ", list_of_heck[0], "\nheck: ", list_of_heck[1])

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score):
    """This strategy rolls 0 dice if that gives at least BACON_MARGIN points,
    and rolls BASELINE_NUM_ROLLS otherwise.

    >>> bacon_strategy(0, 0)
    5
    >>> bacon_strategy(70, 50)
    5
    >>> bacon_strategy(50, 70)
    0
    """
    "*** YOUR CODE HERE ***"
    # Doesn't use score at all????
    if max(int(i) for i in str(opponent_score)) + 1 >= BACON_MARGIN:
     return 0
    else:
     return BASELINE_NUM_ROLLS

def swap_strategy(score, opponent_score):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls BASELINE_NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least BACON_MARGIN points and rolls
    BASELINE_NUM_ROLLS otherwise.

    >>> swap_strategy(23, 60) # 23 + (1 + max(6, 0)) = 30: Beneficial swap
    0
    >>> swap_strategy(27, 18) # 27 + (1 + max(1, 8)) = 36: Harmful swap
    5
    >>> swap_strategy(50, 80) # (1 + max(8, 0)) = 9: Lots of free bacon
    0
    >>> swap_strategy(12, 12) # Baseline
    5
    """
    "*** YOUR CODE HERE ***"
    if  max(int(i) for i in str(opponent_score)) + 1 + score == opponent_score *2:
        #non-beneficial swap
        return BASELINE_NUM_ROLLS
    elif  max(int(i) for i in str(opponent_score)) + 1 + opponent_score == score *2:
        #beneficial swap
        return 0
    else:
        return bacon_strategy(score,opponent_score)

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    Same as Swap Strategy but incorpirates the 4 sided dice rule
    if you're one away from a good swap roll a lot
    Make dictionary wiht averages of very high number of rolls and for each entry check if its lower than the final needed
    """
    "*** YOUR CODE HERE ***"


    #Makes it more or less risky based on if its behind or not. Try running winrate script and adding/removing this part or mess w numbers and run it
    if score - opponent_score >= 14: #replace with diff_scores_change_strat
        BASELINE_NUM_ROLLS = 5
        BASELINE_NUM_ROLLS_FOUR_SIDE = 3
        BACON_MARGIN = 7
        BACON_MARGIN_FOUR_SIDE = 3
    else:
        BASELINE_NUM_ROLLS = 6  # avg of 8.7
        BASELINE_NUM_ROLLS_FOUR_SIDE = 4  # avg of 4.48
        BACON_MARGIN = 9
        BACON_MARGIN_FOUR_SIDE = 5

    #rolls high if its close to swap amount

    #  checks if bacon will win game
    if max(int(i) for i in str(opponent_score)) + 1 + score >= 100:
        return 0
    #checks for bacon to beneficial swap
    elif max(int(i) for i in str(opponent_score)) + 1 + opponent_score == score * 2:
            # beneficial swap
            return 0
    #checks for one point away from beneficial swap
    elif (score + 1)*2 == opponent_score:
        return 10 # try changing this to roll_a_heck_ton
    #if 4 dice strategy
    elif (score+opponent_score)%7 == 0:
        if max(int(i) for i in str(opponent_score)) + 1 >= BACON_MARGIN_FOUR_SIDE:
            return 0
        else:
            return BASELINE_NUM_ROLLS_FOUR_SIDE
    #check for bacon margin
    elif max(int(i) for i in str(opponent_score)) + 1 >= BACON_MARGIN:
        return 0
    #if no other strats just return baseline
    else:
        return BASELINE_NUM_ROLLS


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#        of Python not yet covered in the course.

def get_int(prompt, min):
    """Return an integer greater than or equal to MIN, given by the user."""
    choice = input(prompt)
    while not choice.isnumeric() or int(choice) < min:
     print('Please enter an integer greater than or equal to', min)
     choice = input(prompt)
    return int(choice)

def interactive_dice():
    """A dice where the outcomes are provided by the user."""
    return get_int('Result of dice roll: ', 1)

def make_interactive_strategy(player):
    """Return a strategy for which the user provides the number of rolls."""
    prompt = 'Number of rolls for Player {0}: '.format(player)
    def interactive_strategy(score, opp_score):
     if player == 1:
      score, opp_score = opp_score, score
     print(score, 'vs.', opp_score)
     choice = get_int(prompt, 0)
     return choice
    return interactive_strategy

def roll_dice_interactive():
    """Interactively call roll_dice."""
    num_rolls = get_int('Number of rolls: ', 1)
    turn_total = roll_dice(num_rolls, interactive_dice)
    print('Turn total:', turn_total)

def take_turn_interactive():
    """Interactively call take_turn."""
    num_rolls = get_int('Number of rolls: ', 0)
    opp_score = get_int('Opponent score: ', 0)
    turn_total = take_turn(num_rolls, opp_score, interactive_dice)
    print('Turn total:', turn_total)

def play_interactive():
    """Interactively call play."""
    strategy0 = make_interactive_strategy(0)
    strategy1 = make_interactive_strategy(1)
    score0, score1 = play(strategy0, strategy1)
    print('Final scores:', score0, 'to', score1)

#@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--interactive', '-i', type=str,
      help='Run interactive tests for the specified question')
    parser.add_argument('--run_experiments', '-r', action='store_true',
      help='Runs strategy experiments')
    args = parser.parse_args()

    if args.interactive:
     test = args.interactive + '_interactive'
     if test not in globals():
      print('To use the -i option, please choose one of these:')
      print('\troll_dice', '\ttake_turn', '\tplay', sep='\n')
      exit(1)
     try:
      globals()[test]()
     except (KeyboardInterrupt, EOFError):
      print('\nQuitting interactive test')
      exit(0)
    elif args.run_experiments:
     run_experiments()
#run_experiments()
print(average_win_rate(final_strategy))
