table = int(input("enter the number you want to print table of:  "))


for i  in range(1, 10):
    print(f"{table} * {i} = {table * i}")

# nested loop

for i in range(2,10):
    print(f"table of {i}")
    for j in range(1,10):
        print(f"{i} * {j} = {i * j}")

    print()     