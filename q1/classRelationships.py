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

class DEVICE:

    def __init__(self, device_name: str, device_type: str, brand: str, storage: int):
        self.device_name = device_name
        self.device_type = device_type
        self.brand = brand
        self.__storage = storage
        self.__APPS_LIST = []

    def ADD_APPS(self, app: APPS):
        """Adds an app to the device."""
        self.__APPS_LIST.append(app)
        print(app.name, "has been added to", self.device_name)

    def CHECK_APPS(self, app: APPS):
        """Checks if an app is installed on the device."""
        if app in self.__APPS_LIST:
            print(app.name, "is installed on", self.device_name)
        else:
            print(app.name, "is not installed on", self.device_name)

    def SEARCH_APPS(self, app_name: str):
        """Searches for an app installed on the device."""
        for app in self.__APPS_LIST:
            if app.name.lower() == app_name.lower():
                print("App found:", app.name)
                print("Developer:", app.developer)
                print("Price:", app.price)
                return

     print(app_name, "was not found on", self.device_name)

#Objects

device1 = DEVICE("My Phone", "Smartphone", "Samsung", 128)

#run

print("--- BEFORE RELATIONSHIP ---")

print("Device created independently:")
print("Device Name:", device1.device_name)
print("Device Type:", device1.device_type)
print("Brand:", device1.brand)
print("Storage:", device1._DEVICE__storage, "GB")
print()


print("Apps created independently:")
print(" -", object1.name)
print(" -", object2.name)
print(" -", object3.name)
print()

print("--- BUILDING RELATIONSHIP ---")

print("Adding apps to", device1.device_name)

device1.ADD_APPS(object1)
device1.ADD_APPS(object2)
device1.ADD_APPS(object3)
print()

print("--- AFTER RELATIONSHIP ---")

device1.CHECK_APPS(object1)
device1.CHECK_APPS(object2)
device1.CHECK_APPS(object3)
print()

print("--- SEARCHING FOR APP ---")

device1.SEARCH_APPS("Minecraft")

print()

device1.SEARCH_APPS("Roblox")

print()


