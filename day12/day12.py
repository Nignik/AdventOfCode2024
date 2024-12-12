import numpy as np
from collections import defaultdict

up, down, left, right = np.array([-1, 0]), np.array([1, 0]), np.array([0, -1]), np.array([0, 1])
dirs = [up, right, down, left]

def LOG(file_name, smth):
  if "test.in" in file_name:
    print(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
    
  res = []
  for line in data:
    line = line.strip()
    res.append(list(line))
  
  return res

def in_bounds(grid, pos):
  return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])

def is_same_region(grid, pos, next_pos):
  return grid[pos[0]][pos[1]] == grid[next_pos[0]][next_pos[1]]

def dfs(grid, pos, vis):
  hash = pos[0] * len(grid[0]) + pos[1]
  if vis[hash]:
    return [set(), []] 
  vis[hash] = True
  
  res = [set([(pos[0], pos[1])]), []]
  for dir in dirs:
    next_pos = pos + dir
    if in_bounds(grid, next_pos) and is_same_region(grid, pos, next_pos):
      x = dfs(grid, next_pos, vis)
      res[0].update(x[0])
      res[1].extend(x[1])
    else:
      res[1].append((next_pos[0], next_pos[1]))
      
  return res

def dfs2(grid, pos, vis):
  hash = pos[0] * len(grid[0]) + pos[1]
  if vis[hash]:
    return [set(), []] 
  vis[hash] = True
  
  res = [set([(pos[0], pos[1])]), []]
  for dir in dirs:
    next_pos = pos + dir
    if in_bounds(grid, next_pos) and is_same_region(grid, pos, next_pos):
      x = dfs2(grid, next_pos, vis)
      res[0].update(x[0])
      res[1].extend(x[1])
    else:
      res[1].append((next_pos[0], next_pos[1], dir[0], dir[1]))
      
  return res

def sol1(file_name):
  grid = load_data(file_name)

  cost = 0
  vis = defaultdict(bool)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      area, perim = dfs(grid, np.array([r, c]), vis)
      cost += len(area) * len(perim)
      
  return cost

def sol2(file_name):
  grid = load_data(file_name)

  cost = 0
  vis = defaultdict(bool)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      area, perim = dfs2(grid, np.array([r, c]), vis)
      rows = defaultdict(list)
      cols = defaultdict(list)
      #LOG(file_name, perim)
      for x in perim:
        rows[(x[0], x[2], x[3])].append(x[1])
        cols[(x[1], x[2], x[3])].append(x[0]) 
      for key in rows:
        rows[key].sort()
      for key in cols:
        cols[key].sort()
      
      p = len(perim)  
      if not len(rows) == 0:
        LOG(file_name, rows)
        LOG(file_name, cols)
      
      for y in [rows.values(), cols.values()]:
        for x in y:
          for i in range(1, len(x)):
            if x[i] == x[i-1] + 1:
              p -= 1
            
      if len(area) != 0:
        LOG(file_name, f"{grid[r][c]}: {len(area)} x {p}")
      cost += len(area) * p
      
  return cost

print(f"Star 1:\n test: {sol1('day12/test.in')}\n answer: {sol1('day12/input.in')}\n")
print(f"Star 2:\n test: {sol2('day12/test.in')}\n answer: {sol2('day12/input.in')}")