
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your third number: "))

def greatest(a, b, c):
    if(a == b or a == c or b == a or b == c or c == a or c == b):
        print("two inputs are same.")
    else:
        if (a > b and a > c):
         print(f"a is the greatest {a}")
        elif (b > a and b > c ):
         print(f"b is the greatest {b}")
        else:
         print(f"c is the greatest {c}")


    


greatest(a, b, c)




# ==================built in

print(max(a,b,c))