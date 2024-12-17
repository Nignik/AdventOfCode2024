
A = int(input())
B = A % 8
B = B ^ 6
C = int(A / (2 ** B))
B = B ^ C
B = B ^ 4

print(B)