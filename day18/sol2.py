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
  
  by = [] 
  for i, line in enumerate(data):
    by.append(tuple(map(int, line.split(','))))
  
  return by

def in_bounds(r, c, w, h):
  return 0 <= r < h and 0 <= c < w

def print_grid(grid):
  for r in range(len(grid)):
    s = []
    for c in range(len(grid[0])):
      s.append(grid[r][c])
    print("".join(s))
  print()
  

def sol(file_name, w, h):
  by = load_data(file_name)
  
  vis = defaultdict(bool) 
  grid = [['.' for _ in range(w)] for _ in range(h)]
  
  def check(r, c):
    if not in_bounds(r, c, w, h) or grid[r][c] == '#' or vis[(r, c)]:
      return False
    
    if r == h-1 and c == w-1:
      return True
    
    vis[(r, c)] = True
    
    for a, b in directions:
      ra, cb = r + a, c + b
      if check(ra, cb):
        return True
    
    return False 
  
  for i, (rx, cx) in enumerate(by):
    print(rx, cx)
    grid[rx][cx] = '#'
    if not check(0, 0):
      return rx, cx
    vis = defaultdict(bool)
  
  return -1  
  
#print(f"Test: {sol('test.in', 7, 7)}")
print(f"Answer: {sol('input.in', 71, 71)}\n")