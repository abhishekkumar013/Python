f=open("demo.txt", "r+")
f.write("Hii") # update first 3 characters
print(f.read())
f.close()