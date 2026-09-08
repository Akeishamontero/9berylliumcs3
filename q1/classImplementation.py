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
object1 = APPS("Among Us", "Innersloth", 4.99, True, "Player467", "Light mode")
object2 = APPS("Minecraft", "Mojang", 6.99, True, "Gamergirl123", "Dark Mode")
object3 = APPS("Tiktok", "Zhang Yiming", 0, True, "Starrynights11", "Dark Mode")

#Implementing Methods
print("APPS")
