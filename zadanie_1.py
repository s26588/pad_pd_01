class Animal:
  def __init__(self, genus, gender = "Female"):
    self.is_alive = True
    self.gender = gender
    self.genus = genus

  def breed(self, partner):
    try:
      if self.gender == "Female" and partner.gender == "Male" and self.genus == partner.genus:
        if self.genus == "Canis":
          return Dog()
        else:
          return Cat()
    except:
      print("attribute not found")


class Dog(Animal):
  def __init__(self, gender = "Female"):
    super().__init__("Canis", gender)

  def woof(self):
    return "woof woof"


class Cat(Animal):
  def __init__(self, gender = "Female"):
    super().__init__("Felis", gender)

  def purr(self):
    return "purr"


femaleDog = Dog('Female')
maleDog = Dog('Male')

doggie = femaleDog.breed(maleDog)


femaleCat = Cat('Female')
maleCat = Cat('Male')

kitten = femaleCat.breed(maleCat)