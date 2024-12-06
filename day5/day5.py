def load_data(file_name):
  with open(file_name) as f:
    rows = f.read().split('\n\n')
  
  return (rows[0].split('\n'), rows[1].split('\n'))

def LOG(file_name, smth):
  if file_name == "day5/test.in":
    print(smth)
    
def get_rules(rules_data):
  rules = {}
  for rule in rules_data:
    rule = rule.split('|')
    if rule[0] not in rules.keys():
      rules[rule[0]] = [rule[1]]
    else:
      rules[rule[0]].append(rule[1])
      
  return rules
    
def check_page(page, rules):
  correct = True
  
  for i, num in enumerate(page):
      for other_num in page[i+1:]:
        if other_num not in rules.keys():
          continue
        if num in rules[other_num]:
          correct = False
          break
      if not correct:
        break
  
  if correct:
    return True
  else:
    return False

def sol1(file_name):
  rules_data, pages_data = load_data(file_name)
  
  rules = get_rules(rules_data)
  ans = []
  for page in pages_data:
    page = page.split(',')
    
    if check_page(page, rules):
      ans.append(page[len(page)//2])
  
  return sum(list(map(int, ans)))
        
def sol2(file_name):
  rules_data, pages_data = load_data(file_name)
  rules = get_rules(rules_data)
  ans = []
  for page in pages_data:
    page = page.split(',')
    LOG(file_name, page)
    
    if check_page(page, rules):
      continue
    
    i = len(page)-1
    while i >= 0:
      cp = page.copy()
      for j in range(i):
        if page[i] not in rules.keys():
          continue
        if page[j] in rules[page[i]]:
          page[i], page[j] = page[j], page[i]
          break
      
      i -= 1
      if cp != page:
        i = len(page)-1

    LOG(file_name, page)
    ans.append(page[len(page)//2])
  
  return sum(list(map(int, ans)))


print(f"Star 1:\n test: {sol1('day5/test.in')}\n answer: {sol1('day5/input.in')}\n")
print(f"Star 2:\n test: {sol2('day5/test.in')}\n answer: {sol2('day5/input.in')}")