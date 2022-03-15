
import random
m = int(input('m: '))
n = int(input('n: '))

A = []
B = []
C = [] # A + B

# A = [[0 for _ in range(n)] for _ in range(m)]
# B = [[0 for _ in range(n)] for _ in range(m)]
# C = [[0 for _ in range(n)] for _ in range(m)]

# generating random matrices of size m x n
for i in range(m):
    A.append([])
    B.append([])
    for j in range(n):
        A[i].append(random.randint(1, 100))
        B[i].append(random.randint(1, 100))

for i in range(m):
    C.append([])
    for j in range(n):
        C[i].append(A[i][j] + B[i][j])

# comment 1
print(A, "+", B, "=", C)

