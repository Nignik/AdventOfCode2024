def read_data(file_name):
  with open(file_name) as f:
    rows = f.readlines()
  
  return [row.split() for row in rows]

def check_report(rep):
  max_diff = max([abs(rep[i+1] - rep[i]) for i in range(len(rep)-1)])
  min_diff = min([abs(rep[i+1] - rep[i]) for i in range(len(rep)-1)])
  if ((rep == sorted(rep) or rep == sorted(rep, reverse=True)) and max_diff <= 3 and min_diff >= 1):
    return True
  return False
    
def sol1(file_name):
  rows = [[int(x) for x in row] for row in read_data(file_name)]
  ans = 0
  for row in rows:
    ans += check_report(row)
  
  return ans

def sol2(file_name):
  rows = [[int(x) for x in row] for row in read_data(file_name)]
  
  ans = 0
  for row in rows:
    for i in range(len(row)):  
      rep = row[:i] + row[i+1:]
      if check_report(rep):
        ans += 1
        break
        
  return ans

print(f"Star 1:\n test: {sol1('test.in')}\n answer: {sol1('input.in')}\n")
print(f"Star 2:\n test: {sol2('test.in')}\n answer: {sol2('input.in')}")