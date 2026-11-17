# Activity 2!
## Polymorphism

## Instruction: Do what is asked in each item below:
### 1. Answer the following questions:
 a. What is duck typing, as explained in the video? 
- Duck typing, explained in the video is when the focus is on the object and what can it do(actions) and not what the object is. Duck typing means that the class of an object is less important than the methods and properties that the object has. In other words, if an object behaves like a certain type (if it has the same properties) it can be treated as that type, regardless of its actual class. This concept is often summarized by the phrase "If it looks like a duck and quacks like a duck, it must be a duck."

 b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class? 
- The Car class needed to have a method named move() that behaves similarly to the make_sound method in the Dog and Cat classes. This allows the Car class to be used in the same loop as Dog and Cat, as it provides a common interface (the move() method) that can be called on any object, regardless of whether it inherits from the Animal class or not. This is an example of polymorphism, where different classes can be treated uniformly based on shared method names. 

### 2. Create the Python code --> view it on my portfolio and sample output can be seen in the images file.

### 3. How does the code in 2.2 demonstrate polymorphism?

The code in 2.2 demonstrates polymorphism because the 3 classes: Car, Drone and Boat have the same method called move() but each performs a different action. If we define polymorphism, it allows different methods to use the same method but perform different actions depending on the object. We can observe this with the 3 different classes. Also, the start_trip() function can accept any of these objects without needing to know which specific class the object belongs to. It does not only show polymorphism but we can also observe duck typing because the objects do not need to inherit from the same parent class.
