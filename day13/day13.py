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

def LOG(file_name, smth):
  if "test.in" in file_name:
    print(smth)

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

def sol2(file_name):
  machines = load_data(file_name)
  
  ans = 0 
  for A, B, P in machines:
    price = math.inf 
    
    diff = P[0] - P[1] 
    for i in range(101):
      for j in range(101):
        if i * (A[0] - A[1]) + j * (B[0] - B[1]) == diff and :
          #print(i, j)
          price = min(price, 3 * i + j)
    
    ans += price if price != math.inf else 0
    
  return ans 
  
print(f"Star 1:\n test: {sol1('test.in')}\n answer: {sol1('input.in') if len(sys.argv) == 1 else ''}\n")
print(f"Star 2:\n test: {sol2('test.in')}\n answer: {sol2('input.in') if len(sys.argv) == 1 else ''}")