####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Wet Bandits'
strategy_name = 'Marve'
strategy_description = 'return \'\', \' \', or int 4'
import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    import random
    #This example player always betrays.      
    if len(my_history)<10:
        return random.choice(['c','b','b'])
    else:
        b = 0
        c = 0
        for x in their_history:
            if x == 'c':
                c += 1
            else:
                b += 1
        if c > b:
            if their_history[-2]=='b' and their_history[-1]=='b':
                return 'b'
            elif their_history[-2]=='b' and their_history[-1]=='c':
                return 'b'
            else:
                return 'c'
        else:
            return random.choice(['b','c'])
