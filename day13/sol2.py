from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
from fractions import Fraction

N = 10000000000000

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
      if s[0] == "P":
        x.append(np.array([int(match[0]) + N, int(match[1]) + N]))
      else:
        x.append(np.array([int(match[0]), int(match[1])]))

    res.append(Machine(x[0], x[1], x[2]))

  return res

def is_whole(norm, tol=1e-9):
  return abs(norm - round(norm)) < tol

def sol2(file_name):
  machines = load_data(file_name)
  
  ans = 0 
  for A, B, P in machines:
    price = 0
    denom = A[0]*B[1] - A[1]*B[0]
    if denom == 0:
      continue
    
    i = Fraction(P[0]*B[1] - P[1]*B[0], denom)
    j = Fraction(A[0]*P[1] - A[1]*P[0], denom)

    if i.denominator == 1 and j.denominator == 1:
      i_int = i.numerator
      j_int = j.numerator
      price = i_int * 3 + j_int
      print(i_int, j_int)
  
    ans += price
    
  return ans 
  
print(f"Star 2:\n test: {sol2('test.in')}\n answer: {sol2('input.in') if len(sys.argv) == 1 else ''}")