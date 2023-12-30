# TUPLE OPERATIONS

#packing and unpacking
#packing
t  = 1,2,3
# yup tuple can be intializsed like this too, new to me :). It is done by computer auyomatically
print(t,type(t))
# unpacking
z,y,x = t
print(x,y,z,type(x))

# simple swap
x = 1
y = 2
x,y = y,x
print(x,y)
# in the above code python in the background uses tuple to pack the data in one side and unpack it on another side

l = [5]
print(l,type(l))

t = (5)
print(t,type(t))
# we expect tuple but it show int
# python interprets a tuple as integer when only one value is specified inside the tuple, to change that....

t = (5,)
print(t,type(t))

#a,b,c = input()
#print(a,b,c,'\n')

# Another interesting thing..
t = ([1,2,3],['dad','mom'])
print(t)
# t[0] = [1] - throws error
t[0][2] = 1
print(t)
# from this it can  be infered that if the value inside tuple are mutable then they can be modified but cannot be reestablished

# consider the tuple has some kind of container that holds some values

# in this case of list it is also a container within the another container tuple

# we can change the values of list inside the tuple (mini conatiner which is in big container's va;ue can be changed), but the mini-container itself can't be changed

# the above principle is called hashable and non-hashable

t1 = (1,2,3)
t2 = ([1,2,3],)# or it will change into list

# if the values inside tuple is also immutable then the tuple is called HASHABLE
# if the values inside tuple is mutable then the tuple is called NON-HASHABLE