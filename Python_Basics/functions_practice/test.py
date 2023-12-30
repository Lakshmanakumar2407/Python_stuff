l = [] 
for i in range(3):
  l.append([])
  #print(l)
  for j in range(2):
   # print(j)
    l[i].append(0)
   # print(l)
  #print(l, '\n')
for i in range(3):
  for k in range(2):
    l[i][k] = int(input(f'Enter {i+1} coordinates {k+1} value: '))

print(l)