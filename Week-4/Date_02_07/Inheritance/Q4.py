class Animal:

    def eat(self):
        print("Animal Eats")


class Dog(Animal):

    def bark(self):
        print("Dog Barks")


class Cat(Animal):

    def meow(self):
        print("Cat Meows")


class Lion(Animal):

    def roar(self):
        print("Lion Roars")


dog = Dog()
dog.eat()
dog.bark()

cat = Cat()
cat.eat()
cat.meow()

lion = Lion()
lion.eat()
lion.roar()