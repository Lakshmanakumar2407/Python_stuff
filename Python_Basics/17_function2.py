# Functions for matrix multiplication

# Main idea is to simplify the matrix multiplication into block codes

dim = 3
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[2,3,4],[5,6,7],[8,9,0]]

# initializi matrix C
def init_c(n):
  c = []
  for i in range(n):
    c.append([])
    for k in range(n):
      c[i].append(0)
  return c
#print(init_c(dim))

# select a row in first matrix
def row(F,i):
  x=[]
  for p in range(dim):
    x.append(F[i-1][p])
  return x

# Select a column in second matrix
def column(G,i):
  x = []
  for p in range(dim):
    x.append(G[p][i-1])
  return x

# dot product of row and column
def dot_p(a,b):
  dp = 0
  for i in range(len(a)):
    dp += a[i]*b[i]
  return dp
print(dot_p(row(A,1),column(B,1)))

# Matrix multi
def mat_mul(A,B):
  c = init_c(dim)
  for i in range(dim):
    for j in range(dim):
      c[i][j] = dot_p(row(A,i+1),column(B,j+1))
      #print(c)
  return c
'''
def mul_matrix(a,b):
  C = [[0,0,0],[0,0,0],[0,0,0]]
  for i in range(dim):
    for j in range(dim):
      for k in range(dim):
        C[i][j] += A[i][k]*B[k][j]
  return C
'''
    
print(mat_mul(A,B))