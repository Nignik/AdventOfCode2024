from collections import defaultdict
import regex as re
import sys
import numpy as np
import math

def log(file_name, smth):
  if "test.in" in file_name:
    print(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  res = [] 
  for line in data:
    p, v = line.split()
    pattern = r"-?\d+"
    p = re.findall(pattern, p)
    v = re.findall(pattern, v)
    res.append((np.array(list(map(int, p))), np.array(list(map(int, v)))))

  return res

def get_quadrant(pos, dims):
  quads = [[dims[0] // 2, dims[1] // 2], [dims[0], dims[1] // 2], [dims[0] // 2, dims[1]], [dims[0], dims[1]]]
  quads = [np.array(x) for x in quads]
  if np.all(pos < quads[0]):
    return 0
  elif np.any(pos > quads[0]) and np.all(pos < quads[1]):
    return 1
  elif np.any(pos > quads[0]) and np.all(pos < quads[2]):
    return 2
  elif pos[0] > quads[2][0] and pos[1] > quads[1][1]:
    return 3
  
  return -1

def sol1(file_name, dims):
  robots = load_data(file_name)
  
  quad_cnt = [0, 0, 0, 0]
  positions = []
  for p, v in robots:
    pos = p + v * 100
    pos[0] %= dims[0]
    pos[1] %= dims[1]
    positions.append(pos)
    quad = get_quadrant(pos, dims)
    if quad != -1:
      quad_cnt[quad] += 1 
    
  if "test" in file_name:
    for r in range(dims[1]):
      for c in range(dims[0]):
        cnt = sum(np.array_equal(pos, [c, r]) for pos in positions)
        print(cnt if cnt > 0 else '.', end='')
      print()
   
  print(quad_cnt)
  return math.prod(quad_cnt)
  
print(f"Star 1:\n test: {sol1('test.in', np.array([11, 7], dtype=int))}\n answer: {sol1('input.in', np.array([101, 103], dtype=int))}\n")