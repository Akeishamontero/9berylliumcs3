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

