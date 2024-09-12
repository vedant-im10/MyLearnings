import random

# as we are required to start with a random state, this function is used to generate one.
def get_initial_state(tsp):
  cities = list(range(0, len(tsp)))
  state = []

  for i in range(len(tsp)):
    random_city = cities[random.randint(0, len(cities)-1)]
    state.append(random_city);
    cities.remove(random_city);

  return state

# we need to find shortest path and to do so this function will help in finding length of given route.
def get_route_len(tsp, route):
  route_len = 0
  for i in range(len(route)):
    route_len = route_len + tsp[route[i-1]][route[i]]
    # note: for i = 0 this will take distance between first and last city, which will cover the circular path.
  return route_len

# function to get all the neighbours of given state.
def get_neighbours(state):
  nbrs = []
  # basically swapping two consicutive cities to create neighbours.
  for i in range(len(state)):
    for j in range(i+1, len(state)):
      nbr = state.copy()
      nbr[i] = state[j]
      nbr[j] = state[i]
      nbrs.append(nbr)
  return nbrs

# from given set of neighbours, this function will help to find neighbour state having minimum route length.
def get_best_nbr(tsp, nbrs):
  best_nbr = nbrs[0]
  min_len = get_route_len(tsp, best_nbr)
  print("nbr 0", min_len, ":", best_nbr)
  for i in range(1, len(nbrs)):
    curr_nbr = nbrs[i]
    curr_route_len = get_route_len(tsp, curr_nbr)
    print("nbr", i, curr_route_len, ":", curr_nbr)
    if curr_route_len < min_len:
      min_len = curr_route_len
      best_nbr = curr_nbr
  return best_nbr, min_len

# driver function to run hill_climb algorithm
def hill_climb(tsp):
  curr_state = get_initial_state(tsp);
  curr_len = get_route_len(tsp, curr_state)
  nbrs = get_neighbours(curr_state)
  print("curr:", curr_len, ":", curr_state)
  best_nbr, min_nbr_len = get_best_nbr(tsp, nbrs)

  while min_nbr_len < curr_len:
    
    curr_state = best_nbr
    curr_len = min_nbr_len
    print("curr", curr_len, ":", curr_state)
    nbrs = get_neighbours(curr_state)
    best_nbr, min_nbr_len = get_best_nbr(tsp, nbrs)
  
  return curr_state, curr_len

# tsp = [
#     [0, 20, 40, 23],
#     [11, 0, 13, 30],
#     [21, 13, 0, 12],
#     [24, 12, 14, 0]
# ]

tsp = [
  [0, 20, 40, 23],
  [20, 0, 13, 30],
  [40, 13, 0, 12],
  [23, 30, 12, 0]
]

hill_climb(tsp)