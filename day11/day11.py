from collections import defaultdict

def LOG(file_name, smth):
  if "test.in" in file_name:
    print(smth)

def load_data(file_name):
  with open(file_name) as f:
    data = f.read()
  
  return data.split()

def sol1(file_name):
  data = load_data(file_name)
  for i in range(20):
    new_stones = []
    for stone in data:
      n = len(stone)
      if stone == '0':
        new_stones.append('1')
      elif n % 2 == 0:
        new_stones.extend([stone[:n//2], str(int(stone[n//2:]))])
      else:
        new_stones.append(str(int(stone) * 2024))
    data = new_stones
  
  return len(data)

def sol2(file_name):
  data = load_data(file_name)
  
  stones = defaultdict(int)
  for stone in data:
    stones[stone] = 1
    
  for i in range(75):
    new_stones = defaultdict(int)
    for stone, cnt in sorted(stones.items()):
      n = len(stone)
      if stone == '0':
        new_stones['1'] += cnt
      elif n % 2 == 0:
        left = stone[:n//2]
        right = str(int(stone[n//2:]))
        new_stones[left] += cnt
        new_stones[right] += cnt 
      else:
        new_stones[str(int(stone) * 2024)] += cnt
      
    stones = new_stones 
    
  return sum(stones.values())
  
  
print(f"Star 1:\n test: {sol1('day11/test.in')}\n answer: {sol1('day11/input.in')}\n")
print(f"Star 2:\n test: {sol2('day11/test.in')}\n answer: {sol2('day11/input.in')}")