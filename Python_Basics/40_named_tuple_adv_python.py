from collections import namedtuple

'''
some time when we use tuple to store some meaningful values.... naming them might be useful...
traditional tuples won't give us that
'''
# Here three values indicate Red, Green, Blue which is in order
# with out assigning them, it will be difficult to interpret...
nearblack_color_code = (0,1,2)
print(nearblack_color_code[0])

# one way would be using dictionary
nearblack_color_code = {'Red': 0, 'Green': 1, 'Blue':2}
print(nearblack_color_code['Green'])

# other way would be using named tuple. to use it....
color_code = namedtuple('color', ['Red', 'Green', 'Blue'])
nearblack_color_code = color_code(0,1,2)
print(nearblack_color_code.Green)

# Another example....
Person = namedtuple('Person',['name', 'age', 'gender'])

person1 = Person(name = 'Amy', age = 34, gender= 'female')
print(person1.gender)