

def move_up(blank_position, state):
  up_move = (blank_position[0] - 1, blank_position[1])
  if up_move[0] >= 0:
    up_value = state[up_move[0]][up_move[1]]
    state[up_move[0]][up_move[1]] = 0
    state[blank_position[0]][blank_position[1]] = up_move
    return state
  return None

def move_down(blank_position, state):
  down_move = (blank_position[0] + 1, blank_position[1])
  if down_move[0] <= len(state):
    down_value = state[down_move[0]][down_move[1]]
    state[down_move[0]][down_move[1]] = 0
    state[blank_position[0]][blank_position[1]] = down_value
    return state
  return None

def move_right(blank_position, state):
  right_move = (blank_position[0], blank_position[1] + 1)
  if right_move[0] <= len(state[0]):
    right_value = state[right_move[0]][right_move[1]]
    state[right_move[0]][right_move[1]] = 0
    state[blank_position[0]][blank_position[1]] = right_value
    return state
  return None

def move_left(blank_position, state):
  left_move = (blank_position[0], blank_position[1] - 1)
  if left_move[0] >= len(state[0]):
    left_value = state[left_move[0]][left_move[1]]
    state[left_move[0]][left_move[1]] = 0
    state[blank_position[0]][blank_position[1]] = left_value
    return state
  return None
