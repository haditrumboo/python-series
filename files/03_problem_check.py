
def check():
    with open("files/check/a.txt") as f:
        a = f.read()
        # print(a)
    with open("files/check/b.txt") as f:
        b = f.read()
        # check
    if a == b:
        print(f"both files contain same content.\n \n {a} \n {b}")
    else:
        print("they have different content.")
    



check()