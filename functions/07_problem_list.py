name = input("enter the name:  ")
list = [ "burhan", "wahid", "obaid", "danish", "aizan"]


def remove_name(l, n):
    if n in l:
        l.remove(n)
        print(f"{n} removed.")
    else:
        print(f"{n} not in the list.")


remove_name(list, name)
print(list)