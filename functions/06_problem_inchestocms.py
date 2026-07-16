inches = float(input("enter inches:  "))


def inches_to_cms(i):
    one_inches = 2.54

    return i * one_inches 


a = inches_to_cms(inches)
print(f"{a} cm " )