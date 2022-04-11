import copy
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

def frontier_to_grid(frontier, n_cols=3):
  grid = [[]] 
  # indexer_for the frontier
  col_counter = 0
  for f_node in frontier:
    grid[-1].append(f_node)
    col_counter += 1
    if col_counter == n_cols: 
      col_counter = 0 
      grid.append([])

  if [] in grid:
    grid.remove([])

  return grid

def print_gridrow(grid_row, last_node, write_file=False, filename='a-star.txt', is_solution=False): 
  """
    Prints the nodes toghether with their costs in the frontier
  """
  frontier_str = ''
  for row_idx in range(3):
    for node in grid_row:
      for row_value in node.state[row_idx]:
        frontier_str += f' {str(row_value)} ' if row_value != 0 else ' _ '

      if row_idx == 1:
        frontier_str += f'  ({str(node.f()).zfill(2)}) '
        if node != last_node: 
          frontier_str +=  '   ;\t' if not is_solution else '|--->   '
      else: 
        frontier_str += '\t\t'
    
    frontier_str += '\n'

  print(frontier_str)

  if write_file: 
    with open(filename, 'a+') as f: 
      f.write(frontier_str)


def print_grid(frontier, write_file=False, filename='a-star.txt', is_solution=False):
  """
    Turn the forntier in to a grid and prints the grid
  """
  grid = frontier_to_grid(frontier)

  last_element = grid[-1][-1]
  for grid_row in grid: 
    print_gridrow(grid_row, last_element, write_file=write_file, filename=filename, is_solution=is_solution)


def print_frontier(frontier, step=3, write_file=False, filename='a-star.txt', is_solution=False):

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
            frontier_str +=  '   ;\t' if not is_solution else '|--->   '
        else: 
          frontier_str += '\t\t'
      frontier_str += '\n'
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

    if verbose:
      print("The frontier is: ")
      if write_file: 
        with open(filename, 'a+') as f:
          f.write("The frontier is: \n")
      print_frontier(frontier, write_file=write_file, filename=filename)

    current_node = frontier.pop(0)

    generated_nodes = expand_node(current_node, expanded_nodes)
    expanded_nodes.append(current_node)

    frontier = insert_f(generated_nodes, target, frontier)

    if frontier == [] or current_node == target: 
      break

  print("The solution is: ")
  print('Total cost:', current_node.g )
  print_frontier(current_node.path_to_root, is_solution=True)

  return current_node.path_to_root

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

  #init_node = Node(initial_state)
  #final_node = Node(final_state)
  #f = [init_node]*20 + [final_node]
  #print_frontier(f)
  found_node = a_star(initial_state, final_state, write_file=False, verbose=True)
