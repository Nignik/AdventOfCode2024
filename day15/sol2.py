from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pandas as pd

up, right, down, left = np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])
commands = {'^': up, '>': right, 'v': down, '<': left}

def print_grid(grid):
  for r in range(len(grid)):
    s = []
    for c in range(len(grid[0])):
      s.append(grid[r][c])
    print("".join(s))
  print()

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  grid = [] 
  start = np.array([-1, -1])
  i = 0
  while data[i][0] != '\n':
    temp = list(data[i].strip())
    grid.append([])
    for j, x in enumerate(temp):
      if x == '#':
        grid[-1].extend(['#', '#'])
      elif x == 'O':
        grid[-1].extend(['[', ']'])
      elif x == '@':
        start = np.array([i, len(grid[-1])])
        grid[-1].extend(['@', '.'])
      else:
        grid[-1].extend(['.', '.'])
    i += 1
  
  moves = [] 
  i += 1
  while i < len(data):
    moves.extend(list(data[i].strip()))
    i += 1
  
  return grid, moves, start

def move_box(grid, pos, cmnd, symbol):
  r, c = pos + cmnd
  
  if np.all(cmnd == up) or np.all(cmnd == down): 
    if grid[r][c] == '[':
      move_box(grid, pos + cmnd, cmnd, '[')
      move_box(grid, pos + cmnd + right, cmnd, ']')
    elif grid[r][c] == ']':
      move_box(grid, pos + cmnd, cmnd, ']')
      move_box(grid, pos + cmnd + left, cmnd, '[')
  elif grid[r][c] in ['[', ']']:
    move_box(grid, pos + cmnd, cmnd, grid[r][c])
      
  grid[r][c] = symbol
  grid[pos[0]][pos[1]] = '.'
  

def check_box(grid, pos, cmnd, symbol):
  ok = False
  r, c = pos + cmnd
  
  if grid[r][c] == '#':
    return False
  elif grid[r][c] == '.':
    ok = True
  elif np.all(cmnd == up) or np.all(cmnd == down):
    if grid[r][c] == '[':
      ok = check_box(grid, pos + cmnd, cmnd, '[') and check_box(grid, pos + cmnd + right, cmnd, ']')
    elif grid[r][c] == ']':
      ok = check_box(grid, pos + cmnd, cmnd, ']') and check_box(grid, pos + cmnd + left, cmnd, '[')
  elif grid[r][c] in ['[', ']']:
    ok = check_box(grid, pos + cmnd, cmnd, grid[r][c])
  
  if ok:
    return True
  else:
    return False

def sol(file_name):
  grid, moves, start = load_data(file_name)

  pos = start
  for i, move in enumerate(moves):
    if check_box(grid, pos, commands[move], '@'):
      move_box(grid, pos, commands[move], '@')
      pos += commands[move]
    
  ans = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == '[':
        ans += r * 100 + c
        
  return ans
  
print(f"Star 1:\n test: {sol('test.in')}")
print(f" answer: {sol('input.in')}\n")