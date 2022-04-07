import movimentos
from node import Node, generation_checking

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

def expand_node(current_node: Node, target_node: Node, frontier: list, expanded_nodes: list):
  """
    Expands the node in the current iteration of the A-star algorithm, by generating
    new nodes based on the available operations for the 8-number problem

    Args:
      current_node: Node to be expanded in the current iteration,
      target_node: Node with the objective state of the search
      frontier: List with all the node to be expanded whilist the target node is not reached
      expaded_nodes: List with all the expaded node throughout the search
    Returns:
      The frontier updated
  """

  blank_position = current_node.find_target_position(0, current_node.state)

  up_state = movimentos.move_up(blank_position, current_node.state)
  down_state = movimentos.move_down(blank_position, current_node.state)
  left_state = movimentos.move_left(blank_position, current_node.state)
  right_state = movimentos.move_right(blank_position, current_node.state)

  frontier = generation_checking(current_node, target_node, up_state, frontier, expanded_nodes)
  frontier = generation_checking(current_node, target_node, down_state, frontier, expanded_nodes)
  frontier = generation_checking(current_node, target_node, left_state, frontier, expanded_nodes)
  frontier = generation_checking(current_node, target_node, right_state, frontier, expanded_nodes)

  return frontier

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

    frontier = expand_node(current_node, target, frontier, expanded_nodes)
    expanded_nodes.append(current_node)

    if frontier == [] or current_node == target: 
      break

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
  
  initial_node = Node(initial_state, target_state=final_state)

  #final_node = Node(final_state)


  #initial_node.compute_h(final_state)
  #final_node.compute_h(final_state)
