# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System
### 1. Encapsulation

We can use encapsulation by making a Product class. This class will have all the information about a product, like the product name, price and how many are in stock. It will also have methods that can change these values like `addStock()` and `removeStock()`. This way we can control how the inventory quantities are changed. It keeps the products information from being changed directly and keeps all the related information and operations together in one object.

### 2. Abstraction

We can use abstraction to show the operations that are needed to manage the stores inventory. We do not need to show how these operations work behind the scenes. For example we can have a `sellProduct()` method that checks and updates the stock without the user needing to know how it works. This makes the systems interface simpler. Allows users to interact with the inventory in a clear and meaningful way.

### 3. Inheritance

We can use inheritance to make a `Product` class that has common attributes like product name, price and quantity. Then we can make specific classes, like `FoodProduct` and `HouseholdProduct` that inherit these attributes and methods. These specific classes can also add their characteristics. This reduces code duplication. Provides a structured way of representing different types of products in the inventory.

### 4. Polymorphism

We can use polymorphism to allow different product classes to have their behavior for a common method. For example `FoodProduct` and `HouseholdProduct` can both have a `displayInfo()` method. Each class can show its information in its own way. This allows the inventory system to work with product types through a common interface while maintaining their individual behaviors.

## Reflection

I think encapsulation is the most useful for the sari-sari store inventory system. It provides a structure, for keeping product information together with the operations that manage that information. By controlling how stocks, prices and other product details are changed encapsulation can help prevent mistakes and make the system more reliable. As the number of products increases this organization will make the program easier to maintain and modify. I believe the sari-sari store inventory system will benefit from using encapsulation---by being more organized and easier to use.
