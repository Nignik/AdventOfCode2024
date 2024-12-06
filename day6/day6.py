from enum import Enum
import numpy as np

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
  
  return data, spawn

def sol1(file_name):
  grid, spawn = load_data(file_name)
  up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
  dirs = [up, right, down, left]
  
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
  
    
def sol2(file_name):
  grid, spawn = load_data(file_name)
  up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
  dirs = [up, right, down, left]
  
  pos = spawn
  visited = set()
  additional_obstacles = set()
  dir = 0
  while pos[0] < len(grid) and pos[0] >= 0 and pos[1] < len(grid[0]) and pos[1] >= 0:
    if grid[pos[0]][pos[1]] == '#':
      pos = tuple(np.add(pos, (-dirs[dir][0], -dirs[dir][1])))
      dir = (dir + 1) % 4
    
    if pos in visited:
      additional_obstacles.add(tuple(np.add(pos, dirs[dir])))
      
    visited.add(pos)
    pos = tuple(np.add(pos, dirs[dir]))
    
  LOG(file_name, additional_obstacles)
  if 'test.in' in file_name:
    for r in range(len(grid)):
      for c in range(len(grid[r])):
        if (r, c) in additional_obstacles and grid[r][c] == '.':
          print('0', end='')
        else:
          print(grid[r][c], end='')
        
  
  return len(additional_obstacles)
  
  
  
  

print(f"Star 1:\n test: {sol1('day6/test.in')}\n answer: {sol1('day6/input.in')}\n")
print(f"Star 2:\n test: {sol2('day6/test.in')}\n answer: {sol2('day6/input.in')}")