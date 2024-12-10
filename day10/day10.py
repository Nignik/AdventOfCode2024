import numpy as np

up, down, left, right = np.array([-1, 0]), np.array([1, 0]), np.array([0, -1]), np.array([0, 1])
dirs = [up, right, down, left]

def LOG(file_name, smth):
  if "test.in" in file_name:
    print(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  res = []
  
  for row in data:
    row = row.strip()
    res.append(list(map(int, row)))

  return res

def in_bounds(grid, cell):
  return cell[0] >= 0 and cell[0] < len(grid) and cell[1] >= 0 and cell[1] < len(grid)

def search_ends(grid, cell, depth):  
  if depth == 9:
    return {tuple(cell.tolist())}
  
  res = set()
  for dir in dirs:
    next_cell = cell + dir
    if in_bounds(grid, next_cell) and grid[next_cell[0]][next_cell[1]] == depth + 1:
      res.update(search_ends(grid, next_cell, depth + 1))
  
  return res

def search_paths(grid, cell, depth):  
  if depth == 9:
    return 1
  
  res = 0
  for dir in dirs:
    next_cell = cell + dir
    if in_bounds(grid, next_cell) and grid[next_cell[0]][next_cell[1]] == depth + 1:
      res += search_paths(grid, next_cell, depth + 1)
  
  return res

def sol1(file_name):
  grid = load_data(file_name)
  ans = 0
  
  for r in range(len(grid)):
    for c in range(len(grid)):
      if grid[r][c] == 0:
        ans += len(search_ends(grid, np.array([r, c]), 0))
  
  return ans

def sol2(file_name):
  grid = load_data(file_name)
  ans = 0
  
  for r in range(len(grid)):
    for c in range(len(grid)):
      if grid[r][c] == 0:
        ans += search_paths(grid, np.array([r, c]), 0)
  
  return ans
  
  
print(f"Star 1:\n test: {sol1('day10/test.in')}\n answer: {sol1('day10/input.in')}\n")
print(f"Star 2:\n test: {sol2('day10/test.in')}\n answer: {sol2('day10/input.in')}")