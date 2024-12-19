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


def sol_slow(file_name):
  options, requests = load_data(file_name)

  ans = 0
  for i, req in enumerate(requests):
    n = len(req)
    dp = [set() for _ in range(n+1)]

    dp[0].add(())

    for i in range(1, n+1):
      if req[:i] in options:
        dp[i].add((req[:i],))

      for j in range(1, i):
        if dp[j] and req[j:i] in options:
          for seg_tuple in dp[j]:
            dp[i].add(seg_tuple + (req[j:i],))

    ans += len(dp[n])

  return ans

def sol(file_name):
  options, requests = load_data(file_name)
  option_set = set(options)

  ans = 0
  for req in requests:
    n = len(req)
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
      for j in range(i):
        substring = req[j:i]
        if substring in option_set:
            dp[i] += dp[j]

    ans += dp[n]

  return ans

    
print(f"Test: {sol('test.in')}")
print(f"Answer: {sol('input.in')}\n")