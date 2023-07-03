class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplemented("Child   classes must implement this method")


class Dog(animal):
    def speak(self):
        return "Woof!"


class Cat(animal):
    def speak(self):
        return "Meows"


class Bird(animal):
    def speak(self):
        return "Chirp"


# create an object for the classes  to be implemented
dog = Dog("Tom", "Brown")
print(dog.name)
print(dog.color)
print(dog.speak())

cat = Cat("Kitty", "White")
print(cat.name)
print(cat.color)
print(cat.speak())

bird = Bird("Dorito", "Yellow")
print(bird.name)
print(bird.color)
print(bird.speak())
