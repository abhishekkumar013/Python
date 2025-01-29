# From a file containing numbers senarated by comma, print the count of even numbers.
def addd_dat():
    with open("practic.txt","w")as f:
        f.write("1,2,3,4,5,6,7,8,9,10")

# addd_dat()

def count_even():
    count=0
    with  open("practic.txt","r") as f:
        data=f.read()
        num=data.split(",")
        print(num)
        for i in num:
            if (int(i))%2==0:
                # print(i)
                count+=1
    print(f"Number of even numbers: {count}")
# count_even()

def count_even2():
    count=0
    with  open("practic.txt","r") as f:
        data=f.read()
        num=""
        for i in range(len(data)):
            if (data[i]==","):
                print(num,end=" ")
                if(int(num)%2==0):
                    count+=1
                num=""
            else:
                num+=data[i]
    print(f"Number of even numbers: {count}")
count_even2()