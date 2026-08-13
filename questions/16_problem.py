class Students:
    def __init__(self, name):
        self.name = name

    def marks(self, maths, english, urdu, science, sst):
        self.maths = maths
        self.english = english
        self.urdu = urdu
        self.science = science
        self.sst = sst

    def calculate(self):
        self.total = self.maths + self.english + self.urdu + self.science + self.sst
        self.percentage = (self.total / 500) * 100

        return self.total, self.percentage, self.name

    def grades(self):
        if self.percentage >= 90:
            return "Grade A"
        elif self.percentage >= 80:
            return "Grade B"
        elif self.percentage >= 70:
            return "Grade C"
        elif self.percentage >= 60:
            return "Grade D"
        else:
            return "Fail"


hadi = Students("hadi")

hadi.marks(83, 89, 90, 70, 90)

total, percentage, name = hadi.calculate()
g = hadi.grades()

print(name)
print(total)
print(percentage)
print(g)