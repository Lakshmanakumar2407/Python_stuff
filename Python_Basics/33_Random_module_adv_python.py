# all ready knows some stuff so quick recap..

import random as r

random_method = [round(r.random(),2) for _ in range(100)]  # generates random values between [0,1)
print(random_method)

print()

uniform_method = [round(r.uniform(1,10),3) for _ in range(100)] # generates random float values between two intergers
print(uniform_method)

print()

randint_method = [r.randint(10,20) for _ in  range(50)] # generates random integer between the [10,20] 
print(randint_method)

print()

greetings = ['Hello', 'Hola', 'Vankkam', 'Namaste', 'Hallo', 'Konichiwa']
choice_method = r.choice(greetings) # picks a random vale from list...
print(choice_method)

print()

choices_method = r.choices([1,2,3], weights=[2,5,8], k=20) # selects a number k number of time with weight of 2/15(2+5+8), 5/15, 8/15; so chances of selecting 1 is less compared to 2 and 3
print(choices_method)

print()

dummy_list = list(range(1,10))
r.shuffle(dummy_list) # shuffles the list duh;)
print(dummy_list)

print()

dummy_list.sort()
print(dummy_list)
sample_method = [r.sample(dummy_list, k = 3) for _ in range(10)] # selects k number of distinct value from provided list at atime; choices can also be used but values will be repated
print(sample_method)
# if used choices method here....
choices_method = [r.choices(dummy_list, k=3) for _ in range(10)]
print(choices_method)# proves...