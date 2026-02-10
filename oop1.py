
class Dog:
    def __init__(self, name, breed, hasFur):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur

    def bark(self):
        print("Dog is barking")

dog1 = Dog("JJ", "Bulldog", True)
print(dog1.name, dog1.breed, dog1.hasFur)
dog1.bark()
print()

dog2 = Dog("Tony", "German Shepherd", True)
print(dog2.name, dog2.breed, dog2.hasFur)
dog2.bark()
print()

dog3 = Dog("Max", "Siberian Husky", True)
print(dog3.name, dog3.breed, dog3.hasFur)
dog3.bark()
print()






