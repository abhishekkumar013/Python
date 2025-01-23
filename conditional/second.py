marks=int(input("Enter marks : "))

if marks >= 90:
    grade="O"
elif marks >=80:
    grade="E"
else:
    grade="Fail"

print("Grade:", grade)