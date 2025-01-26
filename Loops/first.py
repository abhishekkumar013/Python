nums=[2,1,4,1,5,6,3]

# for

for i in range(len(nums)):
    print(nums[i],end=" ")
else:
    print("End of array")

print("\n")
for num in nums:
    print(num,end=" ")

# continue
print("\n")
for num in nums:
    if num==1:
        continue
    print(num,end=" ")

#break
print("\n")
for num in nums:
    if num==6:
        break
    print(num,end=" ")

# WHILE LOOP
n=len(nums)
i=0
print('\n')

while i<n:
    print(nums[i],end=" ")
    i+=1

tup=(1,2,3,4,5)
i=0
print('\n')
while i<len(tup):
    print(tup[i],end=" ")
    i+=1


str="hello world"

for char in str:
    print(char,end=" ")
else:
    print("End of string")