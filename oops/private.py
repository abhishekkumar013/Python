# Private(like) attributes & methods
# Conceptual Implementations in Python
# Private attributes & methods are meant to be used only within the class and are not
# accessible from outside the class.

# use __ for private

class Account:
    # private attributes
    __name = 'account'
    def __init__(self, account_number,password):
        self.account_number = account_number
        self.__password = password
    def reset_pass(self):
        print(self.__password)
    #private methods
    def __Hello(self,name):
        print(f"Hello {name}")
    def Welcom(self):
        self.__Hello(self.__name)

acc=Account("1234","abcd")
print(acc.account_number)
acc.Welcom()
# print(acc.__password) #as it private it unable to access
# print(acc.password)
acc.reset_pass() # will work