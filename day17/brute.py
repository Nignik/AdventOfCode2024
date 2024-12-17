from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pandas as pd

up, right, down, left = np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])
directions = [up, right, down, left]

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  regs, program = [], []
  for i, line in enumerate(data):
    pattern = r"\d+"
    nums = list(map(int, re.findall(pattern, line)))
    if i < 3:
      regs.extend(nums)
    elif i > 3:
      program.extend(nums)
    
  return regs, program

def sol(file_name):
  regs, program = load_data(file_name)
  
  x = 0
  while x <= 1000000:
    A, B, C = x, 0, 0
    
    def combo(op):
      if op <= 3: return op
      elif op < 7: return [A, B, C][op - 4]
    
    res = []
    i = 0
    while i < len(program):
      opc, op = program[i], program[i+1]
      match opc:
        case 0:
          A = int(A / (2 ** combo(op)))
        case 1:
          B ^= op
        case 2:
          B = combo(op) % 8
        case 3:
          if A != 0:
            i = op - 2
        case 4:
          B ^= C
        case 5:
          res.extend(str(combo(op) % 8))
        case 6:
          B = int(A / (2 ** combo(op)))
        case 7:
          C = int(A / (2 ** combo(op))) 
      
      i += 2
    
    x += 1 
    if list(map(int, res[0:6])) == program[0:6]:
      print(res, x-1)
  
print(f"Test: {sol('mytest.in')}")
#print(f"Answer: {sol('input.in')}\n")