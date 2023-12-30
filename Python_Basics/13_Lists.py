## LISTS

l = [1, 3, 5, 7, 200, 1233423]
print(l)
print('\n')

l.append(23) # multiple inputs are nor possible
print(l)
print('\n')

l.append(1)
print(l)
l.remove(1) # will remove the first instance of 1 only
print(l)
# to remove another instance another remove command is used
l.remove(1)
print(l)
print('\n')

# Lists within Lists
l = [1,2,3]
m=[]
m.append(l)
print(m)
print('\n')

j = [4,5,6]
m.append(j)
t = []
k = [7,8,9]
t.append(m)
t.append(k)
print(t)
print('\n')

print(t[0],t[1], sep = '\n')
print('\n')

print(t[0][0], t[0][1], sep = '\n')
print('\n')

# Representation of matrices using lists

l1 = [2,4,6]
l2 = [3,6,9]
l3 = [1,2,3]
m = []
m.append(l1)
m.append(l2)
m.append(l3)
print(m)
print('\n')

# to acess elements in the matrix
print(m[0][0], m[0][1], m[0][2], end='\n')
print(m[1][0], m[1][1], m[1][2], end='\n')
print(m[2][0], m[2][1], m[2][2], end='\n')