#  List
marks = [94.3,80,98,98.4,"Abhi"]

print(type(marks))
print(len(marks))

print(marks)

print(marks[1])

# List is mutable
marks[1]=84

print(marks)

# List slicing

print(marks[1:3])
print(marks[:3])
print(marks[2:])

# print 2nd last and 3 last 
print(marks[-3:-1])

# List methods

# append method --> add element at end
marks.append("Kumar")

print(marks)

# sort methods
lists=[5,4,3,1,8,4]
lists.sort()
print(lists)

# decreasing number
lists.sort(reverse=True)
print(lists)

fruits=["Banana","papaya","Apple","banana"]
fruits.sort()
print(fruits)

#reverse
marks.reverse()
print(marks)

# insert (index,Value)
lists.insert(2,98)

print(lists)


#remove -> remove first occurance of element
lists.append(98)
lists.remove(98)
print(lists)

#pop
lists.pop()
# print(lists.pop())
print(lists)

# pop  on index
lists.pop(0)
print(lists)