# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
---
## Existing Class
Class: APPS

Description: My class can function for different needs; entertainment, communication, education or other purposes.

#### Which existing attributes and methods will still be useful when it interacts with another class?

The developer, name, price, available, launch(), download(), updateversion(versionNumber : string) attributes will remain useful. The settings, price, profile can also be used when they interact.

---

## New Related Class
Class: DEVICE

Description: DEVICE is an electronic equipment that people use to do research, to communicate, to entertain or access digital services. Devices can vary in sizes, capabilities and intended purposes.

#### Why should these two classes be connected?

These two classes should be connected because in a DEVICE there is made up of many APPS. The APPS have different features, usages and limits to store and tell information. While a DEVICE is the thing you need to have to have apps, this downloads, launches and other functions that connects these two.

---

## Association
Relationship: DEVICE CONTAINS APPS

Explanation: The relationship of a DEVICE and APPS are that they are both technology-related. Devices are used to run apps or mobile application to access digital services and online features. The class DEVICE provides the hardware and operating system needed for APPS to run. 

---

## Multiplicity
Multiplicity: One to Many DEVICE 1 ───────── 0..* APPS

Explanation: A DEVICE is an electronic that you can download applications on, there are many APPS that contains different features, functions and limits. Inside one device are many applications to compromise of a device.

---

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
![Relationship Test Run](images/relationshipTestRun2.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
---
## Analysis
### What is the association between your two classes?
The association between my classes is that a DEVICE contains APPS. A device can have multiple apps installed o it, which creates a relationship between DEVICE and APPS.

### What multiplicity did you choose and why?
I chose a multiplicity of 1 to 0..*. Because one device is singular and can contain many apps. A DEVICE can exist without any APPS installed but apps can also be added later in the device.
### How did you implement the relationship in Python?
I implemented the relationship by making a list called __APP_LIST inside the DEVICE class. The ADD_APPS() method adds the objects of APPS to this list. The CHECK_APPS() and SEARCH_APPS() method allows the device to check for and search through installed apps.

### Why did you store an object reference instead of copying its data?
I stored an object reference because it lets the DEVICE class work with the existing APPS object. This helps avoid making a copy of the data and this also makes sure changes to the APPS object are reflected in both places.

### If your relationship uses many, why is a list appropriate?
The list is appropriate because one device can contain apps. A list holds than one APPS object, it lets us keep all the apps together and it makes it easy to add new ones or look for specific apps needed. 
