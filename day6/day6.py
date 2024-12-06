from enum import Enum
import numpy as np

up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
dirs = [up, right, down, left]

def LOG(file_name, smth):
  if "test.in" in file_name:
    print(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  spawn = (0, 0)
  for r in range(len(data)):
    data[r].strip()
    idx = data[r].find('^')
    if idx != -1:
      spawn = (r, data[r].find('^'))
    data[r] = list(data[r])
  
  return data, spawn

def sol1(file_name):
  grid, spawn = load_data(file_name)
  
  pos = spawn
  visited = set()
  dir = 0
  while pos[0] < len(grid) and pos[0] >= 0 and pos[1] < len(grid[0]) and pos[1] >= 0:
    if grid[pos[0]][pos[1]] == '#':
      pos = tuple(np.add(pos, (-dirs[dir][0], -dirs[dir][1])))
      dir = (dir + 1) % 4
    
    visited.add(pos)
    pos = tuple(np.add(pos, dirs[dir]))
  
  return len(visited)

def check(grid, r, c, spawn):
  grid[r][c] = '#'
  pos, dir = tuple(spawn), 0
  vis = [False] * 1000000
  hash = 0
  while True:
    if pos[0] in (-1, len(grid)) or pos[1] in (-1, len(grid[0])):
      grid[r][c] = '*'
      return False
    
    if grid[pos[0]][pos[1]] == '#':
      pos = tuple(np.add(pos, (-dirs[dir][0], -dirs[dir][1])))
      dir = (dir + 1) % 4
    
    hash = (pos[1] * len(grid[0]) + pos[0]) * 4 + dir
    if vis[hash]:
      break
    
    vis[hash] = True
    pos = tuple(np.add(pos, dirs[dir]))
    
    
  grid[r][c] = '*'
  return True
    
def sol2(file_name):
  grid, spawn = load_data(file_name)
  ans = 0
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] != '.':
        continue
      
      if check(grid, r, c, spawn):
        ans += 1
        print(ans)
      
  return ans
  
print(f"Star 1:\n test: {sol1('day6/test.in')}\n answer: {sol1('day6/input.in')}\n")
print(f"Star 2:\n test: {sol2('day6/test.in')}\n answer: {sol2('day6/input.in')}")