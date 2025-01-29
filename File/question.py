with open("demo.txt","w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("This file was created using Python.\n")

with open("demo.txt","r") as f:
    data=f.read()
    print(data)

new_data=data.replace("tes","demo")
print(new_data) 