l = ["Harry", "Soham", "Sachin", "Rahul"] 
name = input("enter name: ")
for i in range(len(l)):
    if l[i].startswith('S'):
        print(f"hello {l[i]} welcome")

    else:     
     print(f"hello {l[i]}")


# =====
 
li = ["Harry", "Soham", "Sachin", "Rahul"]

for name in li:
    if name.startswith("S"):
        print(f"Hello {name}, welcome")
    else:
        print(f"Hello {name}")