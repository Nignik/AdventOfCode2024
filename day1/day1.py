from collections import Counter

def read_data(file_name):
  with open(file_name) as f:
    rows = f.readlines()
  
  return map(list, zip(*sorted(cols.split() for cols in rows)))

def sol1(file_name):
  return sum([abs(int(x) - int(y)) for x, y in zip(*read_data(file_name))])
  
def sol2(file_name):
  col1, col2 = read_data(file_name)
  
  counts = Counter(col2)
  
  return sum([int(x) * counts[x] for x in col1])
  

print(f"Star 1:\n test: {sol1('test.in')}\n answer: {sol1('input.in')}\n")
print(f"Star 2:\n test: {sol2('test.in')}\n answer: {sol2('input.in')}")