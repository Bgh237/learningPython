class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat(Pets):
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Tiina(Cat):
  def sing(self, sounds):
    return f'{sounds}'

cat1 = Tiina('Tiina', 5)
cat2 = Simon('Simon', 7)
cat3 = Sally('Sally', 2)

my_cats = [cat1, cat2, cat3]

my_pets = Pets(my_cats)

my_pets.walk()