from time import time
import numpy as np

start_matrix = np.array([[2,8,3],[1,6,4],[7,0,5]])
end_matrix =   np.array([[1,2,3],[8,0,4],[7,6,5]])

visited = []
open = []
closed = []

closed.append(start_matrix)

def calculateHuristic(matrix, e_matrix):
  res = matrix == e_matrix
  return 9 - np.count_nonzero(res)

def possibleChildren(matrix, e_matrix):
  visited.append(matrix)
  [i],[j] = np.where(matrix == 0)
  direction = [[-1, 0], [0, -1], [1, 0],[0, 1]]
  children = []
  for dir in direction:
    ni = i + dir[0]
    nj = j + dir[1]
    newMatrix = matrix.copy()

    if(ni>=0 and ni<=2 and nj>=0 and nj<=2):
      newMatrix[i,j], newMatrix[ni, nj] = matrix[ni,nj], matrix[i, j]
      if not(any(np.array_equal(newMatrix, i) for i in visited)):
        visited.append(newMatrix)
        newMatrix_huristic = calculateHuristic(newMatrix, e_matrix)
        children.append([newMatrix_huristic, newMatrix])
  
  children = sorted(children, key=lambda x:x[0])
  for i in range(len(children)) :
    children[i] = children[i][1]
  return children # array

def puzzelFunction(s_matrix, e_matrix):
  start_huristic = calculateHuristic(s_matrix, e_matrix)
  if(start_huristic == 0):
    for node in closed:
      print(node)
    return True
  else:
    # find possible children, and then calculate each huristic value and sort them.
    children = possibleChildren(s_matrix, e_matrix)

    # Add children at start in the open list in ordered list.
    if(len(children)>0):
      for i in range(len(children)):
        open.insert(i, children[i])

    # remove first children compare with the goal marix by hurisitc value,
    if(len(open)>0):
      newCalculated_huristic = calculateHuristic(open[0], e_matrix)
      newMatrix = open[0]
      closed.append(open[0])
      open.pop(0)
      # -- if huristic value is 0 then return True.
      if(newCalculated_huristic == 0):
        for node in closed:
          print(node)
        return True
      # -- if huristic vlaue is not 0 then again call puzzelFunction function with this new matrix as the start matrix.
      else:
        puzzelFunction(newMatrix, e_matrix)
    else:
      return False

result  = puzzelFunction(start_matrix, end_matrix)

print(result)