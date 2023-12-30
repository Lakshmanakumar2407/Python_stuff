# MATRIX OPERATIONS

# Matrix Addition

#dim = int(input('Enter the dimension of the matrix you want to add: '))

A = []
B = []

'''for i1 in range(dim):
  l = []
  for i2 in range(dim):
    print(i2)
    l.append(int(input(f'Enter the value:')))
  A.append(l)
print(A)
'''
dim = 3
A = [[1,2,3],[3,4,3],[1,4,9]]
B = [[5,6,3],[7,8,3],[2,7,8]]

C = [[0,0,0],[0,0,0],[0,0,0]]
# Python is not smart enough to give the matrix C a value 0

for i in range(dim):
  for j in range(dim):
    C[i][j] = A[i][j] + B[i][j]

print(C)

# MATRIX MULTIPLICATION

for i in range (dim):
  for j in range(dim):
    temp = 0
    for k in range(dim):
      temp = temp + A[i][k]*B[k][j]
    C[i][j] = temp
print(C)
print('\n')

## shortcut
import numpy
X = numpy.mat(A)
Y = numpy.mat(B)
print(X)
print('\n')
print(Y)
print('\n')
print(X*Y)