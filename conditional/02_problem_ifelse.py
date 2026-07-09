m1 = int(input("enter 1 subject marks: "))
m2 = int(input("enter 2 subject marks: "))
m3 = int(input("enter 3 subject marks: "))

total_percentage = ((m1 + m2 + m3)/300)*100
print(total_percentage)

if(total_percentage > 40):
    print("you have passed the exam")

else:
    print("hard luck")
    print("WORK HARD")
