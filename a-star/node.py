
class Node:

  def __init__(self, state, parent=None): 
    self.state = state

    self.g = 0 if parent is None else parent.g + 1

    self.parent = None
    self.children = None

  def find_target_position(self, value, target_state):
    for (row_idx, state_row) in enumerate(target_state):
      for (val_idx, state_value) in enumerate(state_row):
        if value == state_value: 
          return (row_idx, val_idx)

    raise Exception('Value not found')

  def compute_h(self, target_state):
    distance  = 0
    self.h = 0
    for (row_idx, state_row) in enumerate(self.state):
      for (num_idx, number) in enumerate(state_row):
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

  def __eq__(self, other_node):
    equality = isinstance(other_node, self.__class__)
    equality &= self.state == other_node.state
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
