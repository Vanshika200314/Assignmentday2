class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Dogs Barks")

class Cat(Animal):
    def make_sound(self):
        print("Cats Meows")

def animal_sound_in_zoo(animal):
    animal.make_sound()

Dog_instance=Dog()
Cat_instance=Cat()

print("Dog sound")
animal_sound_in_zoo(Dog_instance)

print("Cat sound")
animal_sound_in_zoo(Cat_instance)
    
