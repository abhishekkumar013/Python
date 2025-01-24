# Tuple is immutable
tuples =(1, 2, 1,3,3, 4)

print(type(tuples))
print(len(tuples))
print(tuples)

print(tuples[1])

# empty tuple
tup=()

# tuple with single element 
tupo=(1,)
print(type(tupo))

# isko it smjhega
tupo1=(1)
print(type(tupo1))

#slicing possible
print(tuples[2:])

#method

# index-> return index  off first ocurance
print(tuples.index(3))

# count -> return count of element
print(tuples.count(1))
