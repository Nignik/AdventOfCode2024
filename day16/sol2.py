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
        new_score_right = new_score + 1000
        new_score_down = new_score + 2000
        new_score_left = new_score + 1000
        
        if grid[r][c] == '#':
          continue 
        
        if new_score < scores[(r, c)][d]:
          scores[(r, c)][d] = new_score
          next_step.append(p)
          if new_score_right < scores[(r, c)][(d + 1) % 4]:
            scores[(r, c)][(d + 1) % 4] = new_score_right
          if new_score_down < scores[(r, c)][(d + 2) % 4]:
            scores[(r, c)][(d + 2) % 4] = new_score_down
          if new_score_left < scores[(r, c)][(d + 3) % 4]:
            scores[(r, c)][(d + 3) % 4] = new_score_left
        
    q = next_step
  
  score_grid = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      score_grid[r][c] = min(scores[(r, c)])
  
  positions = set()
  vis = defaultdict(bool)
  
  q = []
  min_end = min(scores[(end[0], end[1])])
  for d in range(4):
    if scores[(end[0], end[1])][d] == min_end:
      q.append((end, d))
      
  while len(q) != 0:
    pos, di = q.pop()
    # if vis[(pos[0], pos[1])]:
    #   continue
    # vis[(pos[0], pos[1])] = True
    
    for i in range(1, 4):
      p = pos + directions[(di + i) % 4]
      scoreA = scores[(p[0], p[1])][(di + i + 2) % 4]
      scoreB = scores[(pos[0], pos[1])][di]
      sub = 1
      if i == 1 or i == 3:
        sub += 1000
      if scoreA == scoreB - sub:
        q.append((p, (di + i + 2) % 4))
        positions.add((p[0], p[1]))
    
  for r in range(len(score_grid)):
    s = []
    for c in range(len(score_grid)):
      if (r, c) in positions:
        s.append(str('O'))
      else:
        s.append(str(grid[r][c]))
    print("".join(s))
  print()
   
  # print(pd.DataFrame(score_grid))
  return len(positions) + 1
  
print(f"Test: {sol('test.in')}")
print(f"Other test: {sol('test2.in')}")
print(f"Answer: {sol('input.in')}\n")