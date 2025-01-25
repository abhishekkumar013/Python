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