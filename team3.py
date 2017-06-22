import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Scofield' # Only 10 chars displayed.
strategy_name = 'Random with lead protection'
strategy_description = 'Starts with 20 random events, then checks position.  If leading, preserves lead with all betrayl.  If losing, checks opponents previous behavior and makes a prediction.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    if len(my_history) < 20:
        return random.choice(['c','b'])
    if len(my_history)>20:
      if int(my_score)<int(their_score):
          if their_history[-1] =='b':
              return 'b'
          else:
              return 'c'
      if int(my_score)>int(their_score):
          return 'b'
    
