import random

l = {}

for i in range(10):
    l['emp_'+str(i)] = random.randint(1000,10000)

print(l)