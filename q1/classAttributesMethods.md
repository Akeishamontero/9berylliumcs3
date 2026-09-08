# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
---
## Design Revision
 Changes from my previous design:
- Fixed Formatting
- Updated the design explanation section for clarity and emphasis.
---
### Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | String | Public | It should be public, so that people can search for the title and download the app. |
| Developer | String | Private | It should be private because the developer might want to stay mysterious. |
|Price |Float |Public | It is public to show the buyers of the app how much it costs. |
| Available | Boolean | Public | It is public because if the app is still available or not, so the users would be updated. |
---
## Updated UML Class Diagram
![Class Diagram](q1/Montero_OOPActPart2.md)
---
## Python Implementation
[View Python Source](classImplementation.py)
---
## Test Run
![Test Run](images/classTestRun.png)
---
## Object Diagram
![Object Diagram](images/objectDiagram.png)
---
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
