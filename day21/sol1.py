from collections import defaultdict
import regex as re
import sys
import numpy as np
import math
import pandas as pd
sys.setrecursionlimit(10**6)

up, right, down, left = (-1, 0), (0, 1), (1, 0), (0, -1)
directions = [up, right, down, left]

numKey = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['-1', '0', 'A']
]
numMap = {'0': (3, 1), 'A': (3, 2), '1': (2, 0), '2': (2, 1), '3': (2, 2), '4': (1, 0),
          '5': (1, 1), '6': (1, 2), '7': (0, 0), '8': (0, 1), '9': (0, 2)}

dirKey = [
    ['-1', '^', 'A'],
    ['<', 'v', '>']
]
dirMap = {'<': (1, 0), 'v': (1, 1), '>': (1, 2), '^': (0, 1), 'A': (0, 2)}

def load_data(file_name):
    with open(file_name) as f:
        data = f.readlines()
  
    queries = []
    for i, line in enumerate(data):
        queries.append(line.strip())
    
    return queries

def in_bounds(r, c, w, h):
    return r >= 0 and r < h and c >= 0 and c < w
  
def bfs(keypad, start, end):
    from collections import deque
    
    scores = defaultdict(lambda: float('inf'))
    scores[start] = 0
    q = deque()
    q.append((start, 0))
    
    while q:
        (r, c), dist = q.popleft()
        for dy, dx in directions:
            nr, nc = r + dy, c + dx
            if in_bounds(nr, nc, len(keypad[0]), len(keypad)) and keypad[nr][nc] != '-1':
                new_dist = dist + 1
                if scores[(nr, nc)] > new_dist:
                    scores[(nr, nc)] = new_dist
                    q.append(((nr, nc), new_dist))
    
    return backtrack_paths(keypad, start, end, scores)

def backtrack_paths(keypad, start, end, scores):
    if scores[end] == float('inf'):
        return []
    
    from collections import deque
    stack = deque()
    stack.append([((end[0], end[1]), (0, 0))])
    
    all_paths = []
    while stack:
        path = stack.pop()
        
        (r, c), (dr, dc) = path[-1]
        
        if (r, c) == start:
            all_paths.append(list(reversed(path)))
            continue
        
        current_dist = scores[(r, c)]
        for (dy, dx) in directions:
            nr, nc = r + dy, c + dx
            if in_bounds(nr, nc, len(keypad[0]), len(keypad)):
                if keypad[nr][nc] != '-1':
                    if scores[(nr, nc)] == current_dist - 1:
                        new_step = ((nr, nc), (dy, dx))
                        stack.append(path + [new_step])

    toDir = {up: 'v', right: '<', down: '^', left: '>'}

    all_dir_paths = []
    for path in all_paths:
        directions_list = []
        for i, ((row, col), (dy, dx)) in enumerate(path):
            if (dy, dx) == (0, 0):
                continue
            directions_list.append(toDir[(dy, dx)])
        all_dir_paths.append(directions_list)

    return all_dir_paths

def process_path(path, depth):
    paths_sum = 0
    for ch in path:
        paths = bfs(dirKey, dirMap['A'], dirMap[ch])
        print(f"depth 1: {paths}")
        best_path = float('inf')
        if depth < 0:
            for new_path in paths:
                best_path = min(best_path, process_path(new_path, depth+1))
            paths_sum += best_path
        else:
            for new_path in paths:
                best_path = min(best_path, len(path))
            paths_sum += best_path
    
    return paths_sum

# Currently the program resets the robots to A after each press, which is not correct
def sol(file_name):
    queries = load_data(file_name)
    
    paths_sum = 0
    for query in queries[:1]:
        for ch in query:
            paths = bfs(numKey, (3, 2), numMap[ch])
            print(f"depth 0: {paths}")
            best_path = float('inf')
            for path in paths:
                best_path = min(best_path, process_path(path, 0))
            paths_sum += best_path
      
    return paths_sum
  
print(f"Test: {sol('test.in')}")
#print(f"Answer: {sol('input.in')}\n")