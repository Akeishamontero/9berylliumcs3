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

    def __init__(self, name, developer, price, available, settings, profile, genre, content, rating):
      
        super().__init__(name, developer, price, available, settings, profile)
        self.genre = genre
        self.content = content
        self.rating = rating

        self.catalog = CATALOG("Entertainment Catalog", "Games", 1)

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

entertainment_object1 = ENTERTAINMENT_APP("Among Us", "Innersloth", 4.99, True, "Light Mode", "Player467", "Party Game", "Online Multiplayer", 4.5)
entertainment_object2 = ENTERTAINMENT_APP("Minecraft", "Mojang", 6.99, True, "Dark Mode", "Gamergirl123", "Sandbox", "Video Game", 4.8)
entertainment_object3 = ENTERTAINMENT_APP("TikTok", "Zhang Yiming", 0.00, True, "Dark Mode", "Starrynights11", "Social Entertainment", "Short Videos", 4.3)

         

