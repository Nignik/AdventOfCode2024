def load_data(file_name):
  with open(file_name) as f:
    rows = f.readlines()
  
  return [row.strip() for row in rows]
  

def sol1(file_name):
  search = load_data(file_name)
  
  sum_rows = sum(row.count("XMAS") for row in search) + sum(row.count("SAMX") for row in search)
  cols = ["".join(row[col_idx] for row in search) for col_idx in range(len(search[0]))]
  sum_cols = sum(col.count(word) for col in cols for word in ["XMAS", "SAMX"])
    
  dp = [[0] * len(search[0]) for _ in range(len(search))]
  dp[0] = [(x, len(search[0]) + x - 1) for x in range(len(search[0]))]
  mapper = {}
  for x in range(len(search[0])):
    mapper[(x, len(search[0]) + x - 1)] = (0, x)
    
  for row in range(1, len(search)):
    for col in range(len(search[0])):
      val = (dp[row-1][col][0] + 1, dp[row-1][col][1]-1)
      dp[row][col] = val
      mapper[val] = (row, col)
  
  diags1 = [""] * (2 * len(search[0]) - 1)
  for r in range(len(dp)):
    for c in range(len(dp[r])):
      idx = mapper[dp[r][c]]
      diags1[dp[r][c][0]] += search[idx[0]][idx[1]]
  
  diags2 = [""] * (2 * len(search[0]) - 1)
  for r in range(len(dp)):
    for c in range(len(dp[r])):
      idx = mapper[dp[r][c]]
      diags2[dp[r][c][1]] += search[idx[0]][idx[1]]
    
  sum_diags = sum(diag.count("XMAS") for diag in diags1) + sum(diag.count("SAMX") for diag in diags1)
  sum_diags += sum(diag.count("XMAS") for diag in diags2) + sum(diag.count("SAMX") for diag in diags2)
    
  return sum_rows + sum_cols + sum_diags

def rotate90(mat):
    n = len(mat)

    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n - j - 1][i] = mat[i][j]

    for i in range(n):
        for j in range(n):
            mat[i][j] = res[i][j]

def sol2(file_name):
  search = load_data(file_name)
  
  pattern = [['M', '.', 'S'],
             ['.', 'A', '.'],
             ['M', '.', 'S']]
  
  cnt = 0
  for r in range(len(search)-2):
    for c in range(len(search[0])-2):
      square = [["" for l in range(3)] for _ in range(3)]
      found = False
      
      for i in range(3):
        for j in range(3):
          square[i][j] = search[r+i][c+j]

      for i in range(4):
        rotate90(pattern)
        for j in range(4):
          rotate90(square)
          if square[0][0] == pattern[0][0] and square[0][2] == pattern[0][2] and square[1][1] == pattern[1][1] and square[2][0] == pattern[2][0] and square[2][2] == pattern[2][2]:
            found = True
            cnt += 1
            break
        if found:
          break
  
  return cnt


print(f"Star 1:\n test: {sol1('test.in')}\n answer: {sol1('input.in')}\n")
print(f"Star 2:\n test: {sol2('test.in')}\n answer: {sol2('input.in')}")