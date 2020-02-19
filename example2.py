##### Each team's file must define four tokens:# team_name: a string# strategy_name: a string# strategy_description: a string# move: A function that returns 'c' or 'b'####

team_name = 'E2'
strategy_name = 'If Greater Than'
strategy_description = 'Betray if total times opponant betrayed is greater than times colluded.'

def move(my_history, their_history, my_score, their_score): 
  '''Make my move based on the history with this player. history: a string with one letter (c or b) per round that has been played with this opponent. their_history: a string of the same length as history, possibly empty. The first round between these two players is my_history[0] and their_history[0] The most recent round is my_history[-1] and their_history[-1] Returns 'c' or 'b' for collude or betray.'''
  
  x = len(their_history) 
  total_b = 0 
  total_c = 0 
  for i in range(1, x): 
    if their_history[i] == "b": 
      total_b += 1 
    else: 
      total_c += 1 
      
  if len(my_history) == 0: 
    return 'c'
  if total_b >= total_c: 
    return 'b' 
  else: 
    return 'c'  
     

    