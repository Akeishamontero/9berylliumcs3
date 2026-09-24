# Advanced Class Relationships

## Previous Activities

[classAttrib](q1/classAttributesMethods.md)

[classRel](q1/classRelationships.md)

## Existing System Description:

### What classes currently exist in your system?

Class 1: APPS

Class 2: DEVICE

###  What problem or limitation exists in your current design?

My current design uses an association between DEVICE and APPS, where one DEVICE can contain many APPS. But the problem here is all apps are treated as the same type of object. It does not distinguish between different categories of apps, if it is educational, provides entertainment or communication-related. This can make the system less organized and make it hard to add features that are specific to certain types of apps. My current design also does not show a stronger HAS-A relationship between the DEVICE and the APPS. 
## Inheritance Relationship

Parent:

Child:

Explanation:

## Inheritance UML

![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation

Relationship:

Class containing another object: 

Contained object: 

Explanation:

## Advanced UML Diagram

![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation

[Source Code](advancedRelationships.py)

## Test Run

![Test](images/advancedTestRun.png)

## Object Diagram

![Objects](images/advancedObjectDiagram.png)


## Reflection
Answers:



### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.

### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.

### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.

### What is the difference between Association from Part III and the advanced relationship you implemented?

### How does your design follow the DRY principle?
