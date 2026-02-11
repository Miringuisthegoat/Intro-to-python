#parent class/super class/base class

class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")

#Child/sub/derived class
class Cat:
    def meow(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")

class Donkey:
    hasTail = True

    def move(self):
        print("Donkey is moving")

a = Animal()


c = Cat()


d = Donkey()

