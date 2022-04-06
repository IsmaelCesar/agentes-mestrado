
class Node: 

  def __init__(self, state): 
      self.state = state

      self.parent = None
      self.children = None

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

