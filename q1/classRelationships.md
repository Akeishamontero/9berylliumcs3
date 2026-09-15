# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
---
## Existing Class
Class: Apps

Description: My class can function for different needs; entertainment, communication, education or other purposes.

#### Which existing attributes and methods will still be useful when it interacts with another class?

---

## New Related Class
Class: Devices

Description: Devices are electronic equipment that people use to do research, to communicate, to entertain or access digital services. Devices can vary in sizes, capabilities and intended purposes.

#### Why should these two classes be connected?

---

## Association
Relationship: DEVICE CONTAINS APPS

Explanation: The relationship of devices and apps are that they are both technology-related. Devices are used to run apps or mobile application to access digital services and online features. A device provides the hardware and operating system needed for applications to run. 

---

## Multiplicity
Multiplicity: One to Many Device 1 ───────── 0..* Apps

Explanation: A device is an electronic that you can download applications on, there are many apps that contains different features, functions and limits. Inside one device are many applications to compromise of a device.

---

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
---
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
