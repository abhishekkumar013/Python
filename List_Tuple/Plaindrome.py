# check palindrome 

nums=[1,2,3,2,1,3]

nums1=nums.copy()
nums1.reverse()

if nums==nums1:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")