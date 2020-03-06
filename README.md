# Testing crash course
This is content is intended to introduce the basics of software testing.
No prior testing knowledge is assumed!  

## Goal
Introduce testing philosophy and code.
The idea is to have by the end of the day the hability to write unit tests, integration tests and end-to-end tests. 

Specifically we will pass through:

* Test patterns
* Fixtures
* Mock
* Parametrized tests
* Monkeypatch
* BDD with Behave

# Agenda
## Introduction
About the speaker and format of talk

## Is testing needed in Data Engineering?
TL/DR: Yes! 

Defintely yes! 
Testing is extensively used in serious data science. 

## Requirements

### System requirements
- Python 2.7
- pip

### Libraries
- pytest
- mock
- numpy
- pandas
- behave

  To install all the lib dependencies run the following from the command line:
  
  ```
  pip install -r requirements.txt
  ```


## Activities
This tutorial will have hands on activities. 
The idea is that each of the following topics will include an explanation followed by an implementation challenge.

## Pytest and basic test writing
We'll cover how to structure tests with the native unittest, pytest, behave, cypress.

### Mock
Loading data or running a model sometimes takes minutes or even hours. We'll see how mock can be used to "fake" python data structures to make writing and running tests faster and more isolated.

### Monkey Patch
In data science you'll frequently be using other peoples libraries. This example will show how to alter functionality during testing time and why this is sometimes desired.

### Test Fixtures
Fixtures are an important component of testing that allows for reuse of mutable data structures. If this doesn't make sense now it will after going through this example.
