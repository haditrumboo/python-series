class calculate:
    @staticmethod
    def square(num1):



        return num1 * num1
    @staticmethod
    def cube(num1):
       


        return num1 * num1 * num1
    @staticmethod
    def root(num1):
       


        return round(num1 ** 0.5,3)
    @staticmethod
    def cube(num1):
       


        return num1 * num1 * num1


cal = calculate()
sq = cal.cube(2)
rt =cal.root(5)
cb =cal.cube(5)
print(cb)