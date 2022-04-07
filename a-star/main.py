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

def expand_node(node: Node, frontier): 

  blank_position = node.find_target_position(0, node.state)



def a_star(initial_state, final_state):
  
  if not is_solvable(initial_state): 
    raise Exception('The initial state is unsolvable')

  
  root = Node(initial_state)
  target = Node(final_state)

  frontier = [root]
  expanded_nodes = []

  while True: 
    frontier = sorted(frontier)
    current_node = frontier.pop(0)

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
  
  initial_node = Node(initial_state)

  final_node = Node(final_state)


  initial_node.compute_h(final_state)
  final_node.compute_h(final_state)

