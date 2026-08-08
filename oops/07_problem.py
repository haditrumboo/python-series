class Animal:
    def __init__(self, name):
        self.name = name


class Pet(Animal):
    def show(self):
        print(f"The pet name is {self.name}")


class Dog(Pet):
    def bark(self):
        print("Woof!")


dog = Dog("Tommy")

dog.show()
dog.bark()