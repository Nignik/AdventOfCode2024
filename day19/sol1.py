from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pandas as pd

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  options, requests = [], []
  for i, line in enumerate(data):
    if i == 0:
      options = line.strip().split(', ')
    elif i > 1:
      requests.append(line.strip())
  
  return options, requests


def sol(file_name):
  options, requests = load_data(file_name)

  ans = 0
  for req in requests:
    idx = [0 for _ in range(len(options))]
    possible = [False for _ in range(len(req))]
    for k, ch in enumerate(req):
      for i in range(len(options)):
        if idx[i] >= len(options[i]):
          idx[i] = 0
          for j in range(len(options[i])):
            possible[k - j - 1] = True
            
        if ch != options[i][idx[i]]:
          idx[i] = 0
        else:
          idx[i] += 1
       
      for i in range(len(options)):
        if idx[i] >= len(options[i]):
          idx[i] = 0
          for j in range(len(options[i])):
            possible[k - j - 1] = True
        
    if all(possible):
      ans += 1
    
  return ans
      
    
print(f"Test: {sol('test.in')}")
print(f"Answer: {sol('input.in')}\n")