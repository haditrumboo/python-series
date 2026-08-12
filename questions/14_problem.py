try:
    fnum = int(input("Enter the first number: "))
    snum = int(input("Enter the first number: "))
    print(f"{fnum} / {snum} = {fnum / snum}")

except ZeroDivisionError as e:
    print(f"zeroDivisionError: {e}")

