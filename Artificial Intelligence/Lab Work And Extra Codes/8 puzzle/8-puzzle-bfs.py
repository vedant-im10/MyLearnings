import copy
import time

# State class - each instance will present state of grid as well as position of blank element.
class State:
  def __init__(self, state, blank, bfs=True, goal=None):
    self.state = state
    self.blank = blank
    if not bfs: self.cost = self.calc(state, goal)
    self.bfs = bfs
    self.goal = goal

  # utility function to get all options.
  def swap(self, s, b):
    t = self.blank.copy()
    x = s[b[0]][b[1]]
    s[t[0]][t[1]] = x
    s[b[0]][b[1]] = ' '
    return s

  # moving upside in grid if possible.
  def move_up(self):
    # print('e', self.state)
    temp_state = copy.deepcopy(self.state)
    temp_blank = self.blank.copy()
    if(temp_blank[0]-1 >= 0): 
      temp_blank[0] -= 1
      temp_state = self.swap(temp_state, temp_blank)
      return State(temp_state, temp_blank,self.bfs, self.goal)
    else: return -1

  # moving downside in grid if possible.
  def move_down(self):
    temp_state = copy.deepcopy(self.state)
    temp_blank = self.blank.copy()
    if(temp_blank[0]+1 < 3): 
      temp_blank[0] += 1
      self.swap(temp_state, temp_blank)
      return State(temp_state, temp_blank, self.bfs, self.goal)
    else: return -1
  
  # moving leftside in grid if possible.
  def move_left(self):
    temp_state = copy.deepcopy(self.state)
    temp_blank = self.blank.copy()
    if(temp_blank[1]-1 >= 0): 
      temp_blank[1] -= 1
      self.swap(temp_state, temp_blank)
      return State(temp_state, temp_blank, self.bfs, self.goal)
    else: return -1

  # moving rightside in grid if possible.
  def move_right(self):
    temp_state = copy.deepcopy(self.state)
    temp_blank = self.blank.copy()
    if(temp_blank[1]+1 < 3): 
      temp_blank[1] += 1
      self.swap(temp_state, temp_blank)
      return State(temp_state, temp_blank, self.bfs, self.goal)
    else: return -1

  # driver function to get all posible new states.
  def get_all_opts(self):
    opts = []
    up = self.move_up()
    down = self.move_down()
    left = self.move_left()
    right = self.move_right()
    if(up != -1): opts.append(up)
    if(right != -1): opts.append(right)
    if(left != -1): opts.append(left)
    if(down != -1): opts.append(down)
    return opts

# utility functions used to solve 8-puzzle(in bfs).
def exists(explored, new):
  for row in explored:
    if(row==new): return True
  return False

def isGoal(curr, goal):
  return curr.state==goal

# main driver function to solve the problem using BFS
def solve(initial, goal):
  q = [initial]
  explored = [initial.state]
  while (len(q)!=0):
    f = q[0]
    q.pop(0)
    opts = f.get_all_opts()
    if isGoal(f, goal): 
      print(f.state, end=" ")
      break
    for opt in opts:
      x = opt.state
      if (exists(explored, x)==False):
        explored.append(x)
        q.append(opt)

# defining initial and goal state here.
state = [
    [[1, 2, 3], [' ', 4, 5], [6, 7, 8]],
    [[1, 2, 3], [4, 5, 6], [' ', 7, 8]],
    [[' ', 2, 3], [4, 5, 6], [1, 7, 8]]
]

blank = [[1, 0], [2, 0], [0, 0]]

goal = [
  [[1, 2, 3], [4, 5, 6], [7, 8, ' ']],
  [[1, 2, 3], [4, 5, 6], [7, 8, ' ']],
  [[6, 2, 3], [4, 5, ' '], [1, 7, 8]]
]

strt = time.time()
for i in range(3):
  initial = State(state[i], blank[i])
  solve(initial, goal[i])
end = time.time()
print()
print("Time taken: ", end-strt)