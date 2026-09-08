class APPS:

 def __init__(self, name, developer, price, available, settings, profile):
  self.name = name
  self.developer = developer
  self.__settings = settings
  self.available = available
  self.profile = profile
  self.price = price

 def Launch(self):
    print(self.name, "has been launched.")

 def Updateversion(self, versionNumber, string):
    self.__settings = string
    print(self.name, "has been updated to version", versionNumber)

 def Download(self):
     if self.available:
        print(self.name, "is downloading.")
     else:
        print(self.name, "is not available for download.")

 def get_settings(self):
     return self.__settings


 def display_info(self):
     print("App Name:", self.name)
     print("Developer:", self.developer)
     print("Price:", self.price)
     print("Available:", self.available)
     print("Profile:", self.profile)

# Create Objects
object1 = APPS("Among Us", "Innersloth", 4.99, True, "Light mode", "Player467")
object2 = APPS("Minecraft", "Mojang", 6.99, True, "Dark Mode", "Gamergirl123")
object3 = APPS("Tiktok", "Zhang Yiming", 0, True, "Dark Mode", "Starrynights11")

#Implementing Methods
print("APPS")

print("--- BEFORE ---")

print("Object 1:")
object1.display_info()
print()

print("Object 2:")
object2.display_info()
print()

print("Object 3:")
object3.display_info()


# Using methods on Object 1
print("--- IMPLEMENTING METHODS ---")

print("Launching Object 1:")
object1.Launch()

print("Downloading Object 1:")
object1.Download()

print("Updating Object 1:")
object1.Updateversion("2.0", "Dark Mode")


# Show that only Object 1 changed
print("--- AFTER ---")

print("Object 1:")
object1.display_info()

print("Object 2:")
object2.display_info()

print("Object 3:")
object3.display_info()
