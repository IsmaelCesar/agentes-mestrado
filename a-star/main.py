import os
import copy
import movements
from node import Node, generation_checking


def write_message_into_file(filename, message, mode=None):
  """
    Checks if the file exists. If not creates it and then writes
    the message into it
  """

  if not mode:
    if not os.path.exists(filename):
      mode = 'w+'
    else: 
      mode = 'a+'

  with open(filename, mode) as f:
        f.write(message)
        
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

def print_frontier(frontier, step=3, write_file=False, verbose=False, filename='a-star.txt', is_solution=False):

  frontier_str = ''
  last_node = frontier[-1]
  for step_idx in range(0, len(frontier), step):
    for row_idx in range(3):
      for node in frontier[step_idx: step_idx+step]:
        for row_value in node.state[row_idx]:
          frontier_str += f' {str(row_value)} ' if row_value != 0 else ' _ '

        if row_idx == 1:
          frontier_str += f'  ({str(node.f()).zfill(2)}) '
          if node != last_node: 
            frontier_str +=  '   ;\t' if not is_solution else '|--->\t'
        else: 
          frontier_str += '\t\t'
      frontier_str += '\n'
    frontier_str += '\n'

  if verbose:
    print(frontier_str)
  if write_file:
    write_message_into_file(filename, frontier_str)
  

def expand_node(current_node: Node, expanded_nodes: list):
  """
    Expands the node in the current iteration of the A-star algorithm, by generating
    new nodes based on the available operations for the 8-number problem

    Args:
      current_node: Node to be expanded in the current iteration,
      expaded_nodes: List with all the expaded node throughout the search
    Returns:
      A list for the generated nodes
  """

  blank_position = current_node.find_target_position(0, current_node.state)

  up_state = movements.move_up(blank_position, copy.deepcopy(current_node.state))
  down_state = movements.move_down(blank_position, copy.deepcopy(current_node.state))
  left_state = movements.move_left(blank_position, copy.deepcopy(current_node.state))
  right_state = movements.move_right(blank_position, copy.deepcopy(current_node.state))

  generated_nodes = []
  for gen_state in [up_state, down_state, left_state, right_state]:
    gen_node = generation_checking(current_node, gen_state, expanded_nodes)
    if gen_node: 
      generated_nodes.append(gen_node)
  return generated_nodes


def insert_f(node_list: list, target_node: Node, frontier: list):
  """
    Insert current node's children into the frontier

    Args: 
      node_list: Node list of the current iteration of the A-star algorithm
      forntier: List with the nodes to be expaded whilist the target_state 
                has not been reached
      target_node: Node of the target state used to compute the h function
    Returns:
      An updated frontier
  """
  if node_list: 
    for eval_node in node_list:
      eval_node.compute_h(target_node.state)
      frontier.append(eval_node)
    
    frontier = sorted(frontier)
  return frontier

def a_star(initial_state, final_state, write_file=False, filename='a-star.txt', verbose=True):
  
  if not is_solvable(initial_state): 
    raise Exception('The initial state is unsolvable')

  
  root = Node(initial_state)
  target = Node(final_state)

  frontier = []
  frontier = insert_f([root], target, frontier)

  expanded_nodes = []

  while True:
    
    message = "The frontier is: \n"
    if verbose:
      print(message)
    if write_file:
      write_message_into_file(filename, message)

    print_frontier(frontier, write_file=write_file, verbose=verbose, filename=filename)

    current_node = frontier.pop(0)

    generated_nodes = expand_node(current_node, expanded_nodes)
    expanded_nodes.append(current_node)

    frontier = insert_f(generated_nodes, target, frontier)

    if frontier == [] or current_node == target: 
      break

  message = "The solution is: \n\n"
  message += f"Total cost: {current_node.g}\n"

  if verbose: 
    print(message)
  if write_file:
    write_message_into_file(filename, message)

  print_frontier(current_node.path_to_root, write_file=write_file, verbose=verbose, filename=filename, is_solution=True)

  return current_node.path_to_root

if __name__ == '__main__': 

  initial_state = [
      [1, 8, 2],
      [0, 4, 3],
      [7, 6, 5]
  ]

  final_state = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 0]
  ]

  found_node = a_star(initial_state, final_state, write_file=False, verbose=True, filename='init-state-lista.txt')
