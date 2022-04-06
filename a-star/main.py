from node import Node

def is_solvable(state): 
  flat_state = []
  
  for state_row in state:
      flat_state += state_row
   
  flat_state.remove(0)

  inversions_count = 0
  for (vc_index, value_check) in enumerate(flat_state): 
    for value_compare in flat_state[vc_index+1:]: 
      if value_check > value_compare:
        inversions_count += 1

  if inversions_count % 2 == 0:
    return True
  else: 
   return False

if __name__ == '__main__': 

  initial_state = [
      [3, 4, 6],
      [7, 5, 8],
      [1, 2, 0]
  ]

  final_state = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 0]
  ]   
  

  #unsolvable_state = [
  #    [8, 1, 2],
  #    [0, 4, 3],
  #    [7, 6, 5]
  #]

  print(is_solvable(final_state))