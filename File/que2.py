# word="Python"
# with open("demo.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("The word  is present in the file.")
#     else:
#         print("The word  is not present in the file.")

def find_word(word):
    with open("demo.txt","r") as f:
        data=f.read()
        # if(data.find(word)!=-1):
        if(word in data):
            print("The word  is present in the file.")
        else:
            print("The word  is not present in the file.")

find_word("Python")