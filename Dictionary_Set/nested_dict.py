student={
    "name":"raj",
    "subject":{
        "phy":98,
        "chem":96,
        "math":95.7
    },
    "roll":210
}
print(student)

print(student.get("subject"))
print(student["subject"])
print(student["subject"]["phy"])

print(student.keys())
print(student.values())

print(student["subject"].keys())
print(student["subject"].values())


# type casting
print(list(student.keys()))

# total key
print(len(student.keys()))
print(len(list(student.keys())))

print(list(student.values()))

pair=list(student.items())
print(pair)
print(pair[0])