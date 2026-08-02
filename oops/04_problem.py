class Number:
    def __init__(self, num):
        self.num = num

    def check(self):
        if self.num == 0:
            print("The number is zero.")

        elif self.num > 0:
            print("The number is positive.")

            if self.num % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")

        else:
            print("The number is negative.")

            if self.num % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")


num = int(input("Enter the number: "))

ch = Number(num)
ch.check()