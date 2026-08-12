try:
    n = int(input("Etner the number: "))

    table = [n*i for i in range(1,11)]
    text = " ".join(map(str, table))
    print(table)

    with open("questions/f/table.txt", "w") as f:
        f.write(text)
        print("done")
except Exception as e:
    print(e)