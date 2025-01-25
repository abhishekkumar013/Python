# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
#unordered 
#set is mutable but elements are immutable that why no list and dict stores in set

nums={1,2,2,5,3,4,3}


print(type(nums))
print(nums)


collecyions={1,2,2,2,"Abhi","Arya","Abhi"}
print(type(collecyions))
print(collecyions)

#len
print(len(collecyions))

#empty set
empty_set=set()
print(type(empty_set))

#add
collecyions.add(20)  
collecyions.add("half")
collecyions.add((22,23,1,1)) # add tuple

print(collecyions)

# remove-> error if not present
collecyions.remove("Abhi")
print(collecyions)

# pop -> remove a random element
collecyions.pop()
print(collecyions)

#clear
collecyions.clear()
print(collecyions)


# union -> combine all 

set1={1,2,3,4,5}
set2={3,4,5,6,7}

union_set=set1.union(set2)
print("Union set ", union_set)

# intersection -> common elements
intersection_set=set1.intersection(set2)
print("Intersection set ", intersection_set)