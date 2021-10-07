"""Create hierarchy out of birds. Implement 4 classes:

    class Bird with an attribute name and methods fly and walk.
    class FlyingBird with attributes name, ration, and with the same methods. ration must have default value.
Implement the method eat which will describe its typical ration.
    class NonFlyingBird with same characteristics but which obviously without attribute fly.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
    class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
    Implement str() function call for each class."""


class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        ...

    def walk(self):
        print(f"{self.name} can walk")


class FlyingBird(Bird):

    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def fly(self):
        print(f"{self.name} can fly")

    def __str__(self):
        return f"{self.name} can walk and fly"


class NonFlyingBird(Bird):

    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

    def swim(self):
        print(f"{self.name} can swim")

    def __str__(self):
        return f"{self.name} can walk and swim"


class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f"{self.name} can walk, swim and fly"


b = Bird("Any")
b.walk()
# "Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
p.swim()
# "Penguin bird can swim"
# p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
p.eat()
# "It eats mostly fish"

c = FlyingBird("Canary")
print(str(c))
# "Canary can walk and fly"
c.eat()
# "It eats mostly grains"

s = SuperBird("Gull")
print(str(s))
# "Gull bird can walk, swim and fly"
s.swim()
s.fly()
s.walk()
s.eat()
print(SuperBird.__mro__)
# "It eats fish"