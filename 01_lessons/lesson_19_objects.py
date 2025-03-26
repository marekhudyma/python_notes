class Sample():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)
        print(self.param2)

sample = Sample("a", "b")
sample.some_method()


class Dog():
    def __init__(self, breed):
        self.breed = breed

my_dog = Dog(breed='Lab')
print(my_dog.breed)

class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * self.radius * 2;

my_circle = Circle(30)
print(my_circle.get_circumference())