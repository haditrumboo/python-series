a =  input("enter 1 number:  ")
b =  input("enter 2 number:  ")
c =  input("enter 3 number:  ")
d =  input("enter 4 number:  ")

if(a > b and a > c and a > d):
    print("a is greatest:", a)

if(b > a and b > c and b > d):
    print("b is greatest:", b)
elif(c > a and c > b and c > d):
    print("c is greatesy:", c)

else:
    print("d is greatest:", d)