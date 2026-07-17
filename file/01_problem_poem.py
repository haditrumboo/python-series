
def file():
   with open("file/f.txt") as f:
    a = f.read().lower
    print(a)
    if ("twinkle" in a) :
      print("yes")

    b = a.count("twinkle")
    print(b)
   


file()

