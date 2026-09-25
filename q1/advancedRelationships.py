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
        
#CATALOG CLASS

class CATALOG:
    def __init__(self, catalog_name: str, category: str, access_level: str, count_items: int):
        self.catalog_name = catalog_name
        self.category = category
        self.access_level = access_level
        self.count_items = count_items

    def display_catalog(self): 
        print("Catalog Name:", self.catalog_name)
        print("Category:", self.category)
        print("Access Level:", self.access_level)
        print("Number of Items in Catalog:", self.count_items)

    def update_catalog(self): 
        self.count_items += 1
        print("Catalog updated.")
        print("New Count of Number of Items in Catalog:", self.count_items)

#INHERITANCE AND COMPOSITION

class ENTERTAINMENT_APP(APPS):

    def __init__(self, name, developer, price, available, settings, profile, genre, content_type, rating):
      
        super().__init__(name, developer, price, available, settings, profile)
        self.genre = genre
        self.content_type = content_type
        self.rating = rating

        self.catalog = CATALOG("Entertainment Catalog", "Games", "Public", 0)

    def Rate_App(self, new_rating):
        self.rating = new_rating
        print(self.name, "this has been rated", self.rating)
         
    def ADD_TO_FAVORITES(self):
        print(self.name, "this has been added to favorites.")

    def display_entertainment_info(self):
         self.display_info()
         print("Genre:", self.genre)
         print("Content Type:", self.content_type)
         print("Rating:", self.rating)

    def display_catalog(self):
         self.catalog.display_catalog()

#OBJECTS

entertainment1 = ENTERTAINMENT_APP("Among Us", "Innersloth", 4.99, True, "Light Mode", "Player467", "Party Game", "Online Multiplayer", 4.5)
entertainment2 = ENTERTAINMENT_APP("Minecraft", "Mojang", 6.99, True, "Dark Mode", "Gamergirl123", "Sandbox", "Video Game", 4.8)
entertainment3 = ENTERTAINMENT_APP("TikTok", "Zhang Yiming", 0.00, True, "Dark Mode", "Starrynights11", "Social Entertainment", "Short Videos", 4.3)

#TEST RUN

print("===== TEST 1 — INHERITANCE =====")
print("\nEntertainment App 1:")
entertainment1.display_entertainment_info()
print("\nEntertainment App 2:")
entertainment2.display_entertainment_info()
print("\nEntertainment App 3:")
entertainment3.display_entertainment_info()

print("=====INHERITED METHODS=====")
print("\nLaunching Among Us:")
entertainment1.Launch()
print("\nDownloading Minecraft:")
entertainment2.Download()
print("\nLaunching TikTok:")
entertainment3.Launch()

print("=====ENTERTAINMENT APP=====")
print("\nRating Among Us:")
entertainment1.Rate_App(4.7)
print("\nAdding Minecraft to favorites:")
entertainment2.ADD_TO_FAVORITES()
print("\nAdding TikTok to favorites:")
entertainment3.ADD_TO_FAVORITES()

print("=====TEST 2 - COMPOSITION=====")
print("\nCatalog belonging to Among Us:")
entertainment1.display_catalog()
print("\nCatalog belonging to Minecraft:")
entertainment2.display_catalog()
print("\nCatalog belonging to TikTok:")
entertainment3.display_catalog()

print("=====CATALOG UPDATES=====")
print("\nUpdating Among Us catalog:")
entertainment1.catalog.update_catalog()
print("\nUpdated Among Us catalog:")
entertainment1.display_catalog()
