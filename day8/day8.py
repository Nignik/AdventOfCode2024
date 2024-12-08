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

def is_antinode1(A, B, P):
  AB = B - A
  PA = A - P
  PB = B - P
  if np.array_equal(AB, PA) or np.array_equal(-AB, PB):
    return True
  return False

def is_antinode2(A, B, P):
  AB = B - A
  AP = P - A
  
  cross_prod = AB[0]*AP[1] - AB[1]*AP[0]
  if np.isclose(cross_prod, 0.0):
      return True
  return False

def solve(grid, is_antinode):
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
          if is_antinode(A, B, P):
            ans.add((r, c))
            
  return len(ans)

def sol1(file_name):
  grid = load_data(file_name)
  
  return solve(grid, is_antinode1)
              
def sol2(file_name):
  grid = load_data(file_name)
  
  return solve(grid, is_antinode2)
  

print(f"Star 1:\n test: {sol1('day8/test.in')}\n answer: {sol1('day8/input.in')}\n")
print(f"Star 2:\n test: {sol2('day8/test.in')}\n answer: {sol2('day8/input.in')}")