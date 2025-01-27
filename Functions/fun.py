
# Built-in Functions
# print( )
# len( )
# type( )
# range( )

# def func-name( param 1, param2..) :
    #some work
# return val


def isEven(num):
    return num%2==0

print(isEven(2))
print(isEven(1))

def add(a,b):
    sum=a+b

    return sum

print(add(2,3))

def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg