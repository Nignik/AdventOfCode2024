from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pprint

up, right, down, left = np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])
commands = {'^': up, '>': right, 'v': down, '<': left}

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  grid = [] 
  start = np.array([-1, -1])
  i = 0
  while data[i][0] != '\n':
    grid.append(list(data[i].strip()))
    if '@' in grid[-1]:
      start = np.array([i, grid[-1].index('@')])
    i += 1
  
  moves = [] 
  i += 1 
  while i < len(data):
    moves.extend(list(data[i].strip()))
    i += 1
  
  return grid, moves, start

def push_box(grid, pos, cmnd, symbol):
  ok = False
  r, c = pos + cmnd
  if grid[r][c] == '#':
    return False
  elif grid[r][c] == 'O':
    ok = push_box(grid, pos + cmnd, cmnd, 'O')
  elif grid[r][c] == '.':
    ok = True
    
  if ok:
    grid[r][c] = symbol
    grid[pos[0]][pos[1]] = '.'
    return True
  else:
    return False

def sol1(file_name):
  grid, moves, start = load_data(file_name)

  pos = start
  for move in moves:
    if push_box(grid, pos, commands[move], '@'):
      pos += commands[move] 

  ans = 0
  for r in range(len(grid)):
    for c in range(len(grid)):
      if grid[r][c] == 'O':
        ans += r * 100 + c
  
  return ans
  
print(f"Star 1:\n test: {sol1('test.in')}")
print(f" answer: {sol1('input.in')}\n")