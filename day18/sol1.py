from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pandas as pd

up, right, down, left = (-1, 0), (0, 1), (1, 0), (0, -1)
directions = [up, right, down, left]

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  by = [] 
  for i, line in enumerate(data):
    if i >= int(sys.argv[1]):
      break
    by.append(tuple(map(int, line.split(','))))
  
  return by

def in_bounds(r, c, w, h):
  return r >= 0 and r < w and c >= 0 and c < h

def print_grid(grid):
  for r in range(len(grid)):
    s = []
    for c in range(len(grid[0])):
      s.append(grid[r][c])
    print("".join(s))
  print()

def sol(file_name, w, h):
  by = load_data(file_name)
  
  grid = [['.' for _ in range(w)] for _ in range(h)]
  for r, c in by:
    grid[r][c] = '#'
    
  q = []
  scores = defaultdict(lambda: math.inf)
  print_grid(grid)
  q.append(((0, 0), 0))
  while len(q) != 0:
    (r, c), steps = q.pop()
    #print(r, c, steps)
    for a, b in directions:
      ra, cb = r + a, c + b
      if not in_bounds(ra, cb, w, h) or grid[ra][cb] == '#' :
        continue
      if scores[(ra, cb)] > steps+1:
        scores[(ra, cb)] = steps+1
        q.append(((ra, cb), steps+1))
  
  #print(scores)
  return scores[(w-1, h-1)]
  
print(f"Test: {sol('test.in', 7, 7)}")
print(f"Answer: {sol('input.in', 71, 71)}\n")