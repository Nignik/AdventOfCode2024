from collections import defaultdict
import regex as re
import sys
import numpy as np
import math

class Machine:
  def __init__(self, A, B, P):
    self.A = A
    self.B = B
    self.P = P
  
  def __iter__(self):
    return iter((self.A, self.B, self.P))

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  res = [] 
  for i in range(0, len(data), 4):
    x = []
    for j in range(3):
      s = data[i + j]
      pattern = r"\d+"
      match = re.findall(pattern, s)
      x.append(np.array([int(match[0]), int(match[1])]))
      
    res.append(Machine(x[0], x[1], x[2]))

  return res

def sol1(file_name):
  machines = load_data(file_name)
  
  ans = 0 
  for m in machines:
    price = math.inf
    for i in range(101):
      for j in range(101):
        pos = i * m.A + j * m.B
        if np.all(pos == m.P):
          print(i, j)
          price =  min(price, i * 3 + j)
    if price != math.inf:
      ans += price
  
  return ans

  
print(f"Star 1:\n test: {sol1('test.in')}\n answer: {sol1('input.in') if len(sys.argv) == 1 else ''}\n")