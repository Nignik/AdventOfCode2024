from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pandas as pd

up, right, down, left = np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])
directions = [up, right, down, left]

def print_grid(grid):
  for r in range(len(grid)):
    s = []
    for c in range(len(grid[0])):
      s.append(str(grid[r][c]))
    print("".join(f" s"))
  print()

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  grid = [] 
  start = np.array([-1, -1])
  end = np.array([-1, -1])
  for i, line in enumerate(data):
    grid.append(list(line.strip()))
    if 'S' in line:
      start = np.array([i, line.index('S')])
    if 'E' in line:
      end = np.array([i, line.index('E')])
  
  return grid, start, end

def sol(file_name):
  grid, start, end = load_data(file_name)
  
  q = [start]
  scores = defaultdict(lambda: [float('inf')] * 4)
  scores[(start[0], start[1])] = [1000, 0, 2000, 1000]
  contributes = defaultdict(lambda: [])
  while len(q) != 0:
    next_step = []
    for pos in q:
      #print(pos)
      r, c = pos
      cost = {0: min(scores[(r, c)][0], scores[(r, c)][1] + 1000, scores[(r, c)][2] + 2000, scores[(r, c)][3] + 1000), 
              1: min(scores[(r, c)][0] + 1000, scores[(r, c)][1], scores[(r, c)][2] + 1000, scores[(r, c)][3] + 2000), 
              2: min(scores[(r, c)][0] + 2000, scores[(r, c)][1] + 1000, scores[(r, c)][2], scores[(r, c)][3] + 1000), 
              3: min(scores[(r, c)][0] + 1000, scores[(r, c)][1] + 2000, scores[(r, c)][2] + 1000, scores[(r, c)][3]), 
              }
      for d in range(4):
        p = pos + directions[d]
        r, c = p
        new_score = cost[d] + 1
        
        if new_score == scores[(r, c)][d]:
          contributes[(r, c, d)].append((pos[0], pos[1]))
        elif new_score > scores[(r, c)][d]:
          contributes[(r, c, d)] = [(pos[0], pos[1])]
          
        if grid[r][c] == '#' or new_score >= scores[(r, c)][d]:
          continue
        
        scores[(r, c)][d] = new_score
        next_step.append(p)
      
    q = next_step
  
  score_grid = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      score_grid[r][c] = min(scores[(r, c)])
  
  positions = []
  vis = defaultdict(bool)
  q = [(end, 0), (end, 1), (end, 2), (end, 3)]
  pos = end
  print(contributes)
  while len(q) != 0:
    pos, di = q.pop()
    vis[(pos[0], pos[1])] = True
    for d in range(4):
      p = pos + directions[d]
       
      if (p[0], p[1]) in contributes[(pos[0], pos[1], (di + 2) % 4)] and not vis[(p[0], p[1])]:
        q.append((p, d))
        positions.append(p)
  
  for r in range(len(score_grid)):
    s = []
    for c in range(len(score_grid)):
      if any(np.array_equal(arr, np.array([r, c])) for arr in positions):
        s.append(str('O'))
      else:
        s.append(str('.'))
    print("".join(s))
  print()
   
  print(pd.DataFrame(score_grid))
  return len(positions)
  
print(f"Star 1:\n test: {sol('test.in')}")
#print(f" answer: {sol('input.in')}\n")