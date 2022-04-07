import movements
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


def print_frontier(frontier): 
  """
    Prints the nodes toghether with their costs in the frontier
  """
  frontier_str = ''
  last_node = frontier[-1]
  for row_idx in range(3): 
    for node in frontier:
      for row_value in node.state[row_idx]:
        frontier_str += f' {str(row_value)} ' if row_value != 0 else ' _ '

      if row_idx == 1:
        frontier_str += f'  ({str(node.f()).zfill(2)}) '
        if node != last_node: 
          frontier_str += '|--->   '
      else: 
        frontier_str += '\t\t'
    
    frontier_str += '\n'
  print(frontier_str)

def expand_node(current_node: Node, expanded_nodes: list):
  """
    Expands the node in the current iteration of the A-star algorithm, by generating
    new nodes based on the available operations for the 8-number problem

    Args:
      current_node: Node to be expanded in the current iteration,
      expaded_nodes: List with all the expaded node throughout the search
    Returns:
      The current node updated
  """

  blank_position = current_node.find_target_position(0, current_node.state)

  up_state = movements.move_up(blank_position, current_node.state)
  down_state = movements.move_down(blank_position, current_node.state)
  left_state = movements.move_left(blank_position, current_node.state)
  right_state = movements.move_right(blank_position, current_node.state)

  for gen_state in [up_state, down_state, left_state, right_state]:
    current_node = generation_checking(current_node, gen_state, expanded_nodes)

  return current_node


def insert_f(current_node: Node, target_node: Node, frontier: list):
  """
    Insert current node's children into the frontier

    Args: 
      currrent_node: Node of the current iteration of the A-star algorithm
      forntier: List with the nodes to be expaded whilist the target_state 
                has not been reached
      target_node: Node of the target state used to compute the h function
    Returns:
      An updated frontier
  """
  if current_node.children: 
    for current_child in current_node.children:
      current_child.compute_h(target_node.state)
      frontier.append(current_child)
    
    frontier = sorted(frontier)
  return frontier

def a_star(initial_state, final_state):
  
  if not is_solvable(initial_state): 
    raise Exception('The initial state is unsolvable')

  
  root = Node(initial_state)
  target = Node(final_state)

  frontier = [root]
  expanded_nodes = []

  while True:

    print("The frontier is: ")
    print(frontier)

    current_node = frontier.pop(0)

    current_node = expand_node(current_node, expanded_nodes)
    expanded_nodes.append(current_node)

    frontier = insert_f(current_node, target, frontier)

    if frontier == [] or current_node == target: 
      break

if __name__ == '__main__': 

  initial_state = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8]
  ]

  final_state = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 0]
  ]

  a_star(initial_state, final_state)
