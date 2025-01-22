# different ways to print  in python

print("Hello, world!")
 
name="Abhi"
age=20
weight=75.3

print(f"My name is {name} and I am {age} years old and weight  is {weight}")
print("My name  is "+name+" and I am "+str(age)+" years old and weight is "+str(weight))
print("My name is %s and I am %d years old." % (name, age))

print("My name is {} and I am {} years old.".format(name, age))
print("My name is", name, "and I am", age, "years old.")
print("My name is", name, "and I am", age, "years old.")

