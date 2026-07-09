name = input("enter your name: ").strip()


if(len(name) < 10):
    print("at least contain 10 alphabet name")

else:
    print("all done")


print(name[0:5])