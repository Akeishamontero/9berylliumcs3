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
