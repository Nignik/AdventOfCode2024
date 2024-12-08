from collections import defaultdict
from itertools import combinations
import numpy as np
import pprint

def LOG(file_name, smth):
  if "test" in file_name:
    pprint.pp(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  res = []
  
  for row in data:
    row = row.strip()
    res.append(list(row))

  return res

def sol1(file_name):
  grid = load_data(file_name)
  
  antenas = defaultdict(list)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != '.':
        antenas[grid[r][c]].append(np.array([r, c]))
  
  ans = set()
  for ant in antenas.values():
    for comb in combinations(ant, 2):
      ab = comb[1] - comb[0]
      for r in range(len(grid)):
        for c in range(len(grid[0])):
          p = np.array([r, c])
          ca = comb[0] - p
          cb = comb[1] - p
          if np.array_equal(ab, ca) or np.array_equal(-ab, cb):
            ans.add((r, c))
  
  return len(ans)
              
  
    
def sol2(file_name):
  grid = load_data(file_name)
  
  antenas = defaultdict(list)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != '.':
        antenas[grid[r][c]].append(np.array([r, c]))
  
  ans = set()
  for ant in antenas.values():
    for comb in combinations(ant, 2):
      for r in range(len(grid)):
        for c in range(len(grid[0])):
          A, B = comb[0], comb[1]
          P = np.array([r, c])
          
          AB = B - A
          AP = P - A
          
          cross_prod = AB[0]*AP[1] - AB[1]*AP[0]
          if np.isclose(cross_prod, 0.0):
              ans.add((r, c))
        
  return len(ans)
  

print(f"Star 1:\n test: {sol1('day8/test.in')}\n answer: {sol1('day8/input.in')}\n")
print(f"Star 2:\n test: {sol2('day8/test.in')}\n answer: {sol2('day8/input.in')}")