try:
    with open("questions/f/sample.txt") as f1, open("files/q.txt") as f2:
        print(f1.read())
        print(f2.read())

except Exception as e:
    print(e)