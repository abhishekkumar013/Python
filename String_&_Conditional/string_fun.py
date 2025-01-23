str="i am a engineer"

#endwith return true if the string end with substr

print(str.endswith("er"))
print(str.endswith("er."))

#capitalize -> create a new string
print(str.capitalize())

# parmanently replace
str = str.capitalize()



# replace all occurences of old  with new

print(str.replace("a","A"))

# find index of a character

print(str.index("e"))

# count

print(str.count("e"))
print(str.count("am"))


# many more functions