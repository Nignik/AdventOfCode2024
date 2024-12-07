import re

up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
dirs = [up, right, down, left]

def LOG(file_name, smth):
  if "test.in" in file_name:
    print(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  res = []
  
  for row in data:
    row = row.strip()
    row = row.split(': ')
    row[1] = re.findall(r'\S+|\s+', row[1])
    res.append(row)

  return res

def sol1(file_name):
  data = load_data(file_name)
  
  ans = 0
  for row in data:
    spaces = [index for index, char in enumerate(row[1]) if char == ' ']
    for i in range(pow(2, len(spaces))):
      res = int(row[1][0])
      for j, space in enumerate(spaces):
        if (i >> j) & 1:
          res *= int(row[1][space+1])
        else:
          res += int(row[1][space+1])
      
      if res == int(row[0]):
        ans += res
        break
      
  return ans

def get_i(num, i):
    base3 = ""
    while num > 0:
        base3 = str(num % 3) + base3
        num //= 3
    
    if i < len(base3):
        return int(base3[-(i + 1)])
    else:
        return 0
    
def sol2(file_name):
  data = load_data(file_name)
  
  ans = 0
  for row in data:
    spaces = [index for index, char in enumerate(row[1]) if char == ' ']
    for i in range(pow(3, len(spaces))):
      res = int(row[1][0])
      for j, space in enumerate(spaces):
        if get_i(i, j) == 0:
          res *= int(row[1][space+1])
        elif get_i(i, j) == 1:
          res += int(row[1][space+1])
        else:
          res = int(str(res) + row[1][space+1])
      
      if res == int(row[0]):
        ans += res
        break
      
  return ans
  
print(f"Star 1:\n test: {sol1('day7/test.in')}\n answer: {sol1('day7/input.in')}\n")
print(f"Star 2:\n test: {sol2('day7/test.in')}\n answer: {sol2('day7/input.in')}")