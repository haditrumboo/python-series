number =  int(input("enter the number:  "))
fact = 1

for i in range(number, 0, -1):
    # print(i)
    fact *=i
 
print(fact)

# =======



fact = []
fact1 = 1
for i in range(number, 0, -1):
    fact.append(i)
    for j in fact:
        fact1 *= j
print(fact1)