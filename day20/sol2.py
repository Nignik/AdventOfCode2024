from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pandas as pd
sys.setrecursionlimit(10**6)

up, right, down, left = (-1, 0), (0, 1), (1, 0), (0, -1)
directions = [up, right, down, left]

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  grid = [] 
  start = (0, 0)
  end = (0, 0)
  for i, line in enumerate(data):
    grid.append(list(line.strip()))
    if 'S' in line:
      start = (i, line.index('S'))
    elif 'E' in line: 
      end = (i, line.index('E'))
    
  return grid, start, end

def in_bounds(r, c, w, h):
  return r >= 0 and r < w and c >= 0 and c < h

def print_grid(grid):
  for r in range(len(grid)):
    s = []
    for c in range(len(grid[0])):
      s.append(grid[r][c])
    print("".join(s))
  print()
  
def dfs(grid, pos, scores, score):
  r, c = pos
  if not in_bounds(r, c, len(grid[0]), len(grid)) or scores[(r, c)] != float('inf') or grid[r][c] == '#':
    return
  scores[(r, c)] = score

  for a, b in directions:
    dfs(grid, (r + a, c + b), scores, score+1) 
  

def sol(file_name):
  grid, start, end = load_data(file_name)
  scores = defaultdict(lambda: float('inf')) 

  dfs(grid, start, scores, 0)
  
  for r, c in scores:
    if scores[(r, c)] != float('inf'):
      grid[r][c] = str(scores[(r, c)])
  #print(pd.DataFrame(grid))
  
  cheats = defaultdict(int)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == '#':
        continue
      
      score = scores[(r, c)] 
      for a in range(-21, 21):
        for b in range(-21, 21):
          if abs(a) + abs(b) > 20 or scores[(r + a, c + b)] == float('inf'):
            continue
          
          cheat = scores[(r + a, c + b)] - score - (abs(a) + abs(b))
          cheats[cheat] += 1
  
  ans = 0
  temp = []
  for x, y in cheats.items():
    if x >= 50:
      temp.append(f"{x}: {y}")
    if x >= 100:
      ans += y
      
  #print(sorted(temp))
      
  return ans
  
print(f"Test: {sol('test.in')}")
print(f"Answer: {sol('input.in')}\n")