n = int(input("enter the number: "))

def sumoffirstintnumds(n):
    if n == 0:
        return 0
    else:
        return n + sumoffirstintnumds (n-1)
    

a = sumoffirstintnumds(n)
print(a)