class Animal: #Parent Class
  def __init__(self, name): #Initialize the name attribute
    self.__name = name 
    
#METHODS
  def feed(self): #Define feed method
    print(f"{self.__name} is eating fed.")

  def make_sound(self): #Define make_sound method
    print(f"{self.__name} makes a sound.")

class Lion(Animal): #Child Class
    
  def make_sound(self): #Override make_sound method
    print(f"{self._Animal__name} roars loudly!")

  def feed(self): #Override feed method
    print(f"{self._Animal__name} eats fresh meat.")
    
class Elephant(Animal): #Child Class
    
  def make_sound(self): #Override make_sound method
    print(f"{self._Animal__name} trumpets!")
    
  def feed(self): #Override feed method
    print(f"{self._Animal__name} eats grass and fruits.")
    
class Monkey(Animal): #Child Class
    
  def make_sound(self): #Override make_sound method
    print(f"{self._Animal__name} chatters!")
    
  def feed(self): #Override feed method
    print(f"{self._Animal__name} eats bananas.")

#CREATE OBJECTS
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

#PRINT METHODS
lion.make_sound()
lion.feed()
print("------") #add break line for better readability

elephant.make_sound()
elephant.feed()
print("------") #add break line for better readability

monkey.make_sound()
monkey.feed() 
print("------") #add break line for better readability
