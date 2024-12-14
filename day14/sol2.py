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
    pattern = r"-?\d+"
    for line in data:
        p_str, v_str = line.split()
        p = list(map(int, re.findall(pattern, p_str)))
        v = list(map(int, re.findall(pattern, v_str)))
        res.append((np.array(p), np.array(v)))
    return res

def get_quadrant(pos, dims):
    mid_x = dims[0] // 2
    mid_y = dims[1] // 2
    x, y = pos
    if x < mid_x and y < mid_y:
        return 0
    elif x > mid_x and y < mid_y:
        return 1
    elif x < mid_x and y > mid_y:
        return 2
    elif x > mid_x and y > mid_y:
        return 3
    return -1

def sol1(file_name, dims):
  robots = load_data(file_name)
  num_iter = 10000
  quad_cnt = [0, 0, 0, 0]

  for i in range(0, num_iter):
    print(i)
    positions = []
    pos_counts = defaultdict(int)
    for (p, v) in robots:
      pos = p + v * i
      pos[0] %= dims[0]
      pos[1] %= dims[1]
      positions.append(pos)
      pos_counts[(pos[0], pos[1])] += 1
    
    current_quad = [0, 0, 0, 0]
    for pos in positions:
      q = get_quadrant(pos, dims)
      if q != -1:
          current_quad[q] += 1
    
    quad_cnt = current_quad
    if "input" in file_name:
      output_lines = []
      for r in range(dims[1]):
        line = []
        for c in range(dims[0]):
          line.append('#' if pos_counts.get((c, r), 0) > 0 else '.')
        output_lines.append("".join(line))
      print("\n".join(output_lines))
      print()  # blank line

  print(quad_cnt)
  return math.prod(quad_cnt)

print(f"Star 1:\n test: {sol1('test.in', np.array([11, 7], dtype=int))}\n answer: {sol1('input.in', np.array([101, 103], dtype=int))}\n")
