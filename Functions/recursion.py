# print n to 1 backwards

def show(n):
    if(n==0):
        return
    print(n,end=" ")
    show(n-1)

show(10)
print("\n")

def fact(n):
    if(n==1 or  n==0):
        return 1
    return n*fact(n-1)

print("Factorial of 5 is :",fact(5))

fruits=['apple','banana','mango','orange']

def print_list(list,i=0):
    if(i==len(list)):
        return
    print(list[i],end=" ")
    print_list(list,i+1)

print_list(fruits)