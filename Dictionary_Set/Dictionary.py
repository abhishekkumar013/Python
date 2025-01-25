# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys

dict={
    "name":"John",
    "age":25,
    "city":"New York",
    "marks":[98,97,96],
    "topics":("dic","set"),
    12:"twelve",
    12.5:"twelve point five",
}

print(type(dict))
print(dict)
print(dict["name"])
# get -> if not exists then return  None  
print(dict.get("name"))

# keys
print(dict.keys())

# values
print(dict.values())

# items-> return in tuples
print(dict.items())

# assign or add new

dict["gender"]="male"
print(dict)

dict["name"]="Raj"
print(dict)

# Update->assign or add new
dict.update({"name":"Raj","age":30})
dict.update({"country":"India"})
print(dict)

# Removing values

dict.pop("gender")
dict.pop(12) 
print(dict)

dict.popitem() # Removing last inserted item
print(dict)

# delete key-value pair
del dict["age"]
print(dict)

dict.clear() # Clearing dictionary
print(dict)

# Empty dict
null_dict={}
null_dict["name"]="sir ji"

