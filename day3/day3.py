import re

def read_data(file_name):
  with open(file_name) as f:
    rows = f.read()
  
  return rows

def sol1(file_name):
  memory = read_data(file_name)
  pattern = r"mul\((\d+),(\d+)\)"
  ops = re.findall(pattern, memory)
  ans = sum(int(op[0]) * int(op[1]) for op in ops)
  
  return ans

def sol2(file_name):
  memory = read_data(file_name)
  pattern = r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)"
  ops = re.finditer(pattern, memory)
  ans = 0
  do = True
  for op in ops:
    if op.group(1) and op.group(2) and do:
      ans += int(op.group(1)) * int(op.group(2))
    elif op.group(0) == "do()":
      do = True
    elif op.group(0) == "don't()":
      do = False
  
  return ans

print(f"Star 1:\n test: {sol1('test.in')}\n answer: {sol1('input.in')}\n")
print(f"Star 2:\n test: {sol2('test.in')}\n answer: {sol2('input.in')}")