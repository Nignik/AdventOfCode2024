import pprint

def LOG(file_name, smth):
  if "test" in file_name:
    print(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.read()

  res = [int(x) for x in data]
  return res

def sol1(file_name):
  data = load_data(file_name)
  
  dec = []
  files = []
  comp = 0
  for i in range(len(data)):
    if i % 2:
      dec.extend([-1] * data[i])
    else:
      for j in range(len(dec), len(dec) + data[i]):
        files.append((j, i//2))
      
      comp += data[i]
      dec.extend([i//2] * data[i])
  
  LOG(file_name, comp)
  for i in range(10000000):
    if len(dec) == comp:
      break
    
    if dec[i] == -1:
      while dec[-1] == -1:
        dec.pop()
      
      if len(dec) == comp:
        break
      dec[i] = dec.pop()
  
  ans = 0
  for i in range(len(dec)):
    if dec[i] != -1:
      ans += i * dec[i]
  
  return ans
              
def sol2(file_name):
  data = load_data(file_name)
  
  spaces = []
  files = []
  sz = 0
  for i in range(len(data)):
    if i % 2:
      spaces.append([sz, sz + data[i]-1])
      sz += data[i]
    else:
      files.append([sz, sz + data[i]-1, i//2])
      sz += data[i]
  
  files.reverse()
  for i in range(len(files)):
    for j in range(len(spaces)):
      space_sz = spaces[j][1] - spaces[j][0] + 1
      file_sz = files[i][1] - files[i][0] + 1
      if spaces[j][0] > files[i][0]:
        break
      if space_sz > file_sz:
        files[i][0] = spaces[j][0]
        spaces[j][0] += file_sz
        files[i][1] = spaces[j][0]-1
        break
      elif space_sz == file_sz:
        files[i][0] = spaces[j][0]
        files[i][1] = spaces[j][1]
        spaces.pop(j)
        break
  
  mem = [-1] * sz
  for i in range(len(files)):
    LOG(file_name, mem)
    for j in range(files[i][0], files[i][1]+1):
      mem[j] = files[i][2]
      
  LOG(file_name, mem)
      
  ans = 0
  for i in range(len(mem)):
    if mem[i] != -1:
      ans += i * mem[i]
  
  return ans
  
  
print(f"Star 1:\n test: {sol1('day9/test.in')}\n answer: {sol1('day9/input.in')}\n")
print(f"Star 2:\n test: {sol2('day9/test.in')}\n answer: {sol2('day9/input.in')}")