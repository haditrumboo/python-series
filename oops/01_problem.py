class Programmer:
    company = "Microsoft"

    def __init__(self, name, age, pin):
        self.name = name
        self.age = age
        self.pin = pin
    @staticmethod
    def done():
        print("done")


p = Programmer("hadi", 20, 190015)

print(p.company, p.name, p.age, p.pin)
p.done()