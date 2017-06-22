####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'ErkanTeacher' # Only 10 chars displayed.
strategy_name = 'Check the big one'
strategy_description = '''checks the number of the b and c in both history
if number of b in my_history is larger than or equal to their_history returns b else c
if number of c in my_history is larger than or equal to their_history returns c else b
'''
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'.''' 
    
    their, my = ([],[])
    c = 'c'
    b = 'b'
        
    for c in their_history: #check number of 'c' letter in their_history
        if c==their_history:
            their.append(1)
        if c==my_history:
            my.append(1)
    
    if sum(my)>sum(their):
        return 'c'
        
    if sum(their)>sum(my):
        return 'b'
    else:    
        return 'b'  
    
    their, my = ([],[])            
                                        
    for b in their_history: #check number of 'b' letter in their_history
        if b==their_history:
            their.append(1)
        if b==my_history:
            my.append(1)
    
    if sum(my)>sum(their):
        return 'b'
        
    if sum(their)>sum(my):
        return 'c'
    else:    
        return 'c' 
        
    return 'c'     
     
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             