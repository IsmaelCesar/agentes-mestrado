class Node:

  def __init__(self, state, parent=None): 
    self.state = state

    self.parent = parent
    self.h = 0

    if parent is None:
      self.path_to_root = [self]
      self.g = 0
    else:
      self.path_to_root = parent.path_to_root + [self]
      self.g = parent.g + 1

  def find_target_position(self, value, state_matrix):
    for (row_idx, state_row) in enumerate(state_matrix):
      for (val_idx, state_value) in enumerate(state_row):
        if value == state_value: 
          return (row_idx, val_idx)

    raise Exception('Value not found')

  def compute_h(self, target_state):
    self.h = 0
    for (row_idx, state_row) in enumerate(self.state):
      for (num_idx, number) in enumerate(state_row):
        distance = 0
        if number != 0:
          number_position = (row_idx, num_idx)
          target_position = self.find_target_position(number, target_state)
          distance += abs(number_position[0] - target_position[0])
          distance += abs(number_position[1] - target_position[1])
          self.h += distance

  def f(self):
    return self.g + self.h

  def __str__(self):
    node_str = ''
    for state_row in self.state: 
      for number in state_row: 
        value = str(number) if number != 0 else '_'
        node_str += ' ' + value + ' '

      node_str += '\n'
    return node_str

  def __repr__(self):
    return self.__str__()


  def __eq__(self, other_node):
    equality = isinstance(other_node, self.__class__)
    equality = equality and self.state == other_node.state
    return equality

  def __lt__(self, other_node):
    assert isinstance(other_node, self.__class__)
    return self.f() < other_node.f()
  
  def __le__(self, other_node):
    assert isinstance(other_node, self.__class__)
    return self.f() <= other_node.f()
  
  def __gt__(self, other_node):
    assert isinstance(other_node, self.__class__)
    return self.f() > other_node.f()
  
  def __ge__(self, other_node):
    assert isinstance(other_node, self.__class__)
    return self.f() >= other_node.f()

def generation_checking(current_node: Node, new_state: list, expanded_nodes: list):
  """
    Generates the node based on the new state passed as parameter. Checkin if the generated node is not the same
    as its parent, and if it has not already been expanded before.

    Args: 
      current_node: Node being expanded in the current iteration
      new_state: List, multidimentional list to beused to represent the new state generated
      expanded_nodes: List containin all the nodes that have already been expanded
    Returns: 
      An updated current_node 
  """
  
  if new_state is not None:

    generated_node = Node(new_state, parent=current_node)
    truth_value = generated_node != current_node.parent
    truth_value = truth_value and generated_node not in expanded_nodes
    if truth_value:
      return generated_node

  return None
