# Store following word meanings in a python dictionary :
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}

print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++ , C

# 1st way
sets=set()
sets.add("python")
sets.add("java")
print(len(sets))


classes={"python", "java", "C++", "python", "javascript","java", "python", "java", "C++" , "C"}
print(len(classes))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
list1=["phy","chem","math"]
dict1={}

for i in range(len(list1)):
    x=int(input(f"Enter marks for {list1[i]}"))
    dict1[list1[i]]=x

print(dict1)

# Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)

value={9,9.0}
print(value)


values={
("float", 9.0),
("int", 9)
}
print(values)