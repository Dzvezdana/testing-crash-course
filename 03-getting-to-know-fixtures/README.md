# Getting to know fixtures
Fixtures are an important component of testing that allows for reuse of mutable data structures. 

From wikipedia: A software test fixture sets up the system for the testing process by providing it with all the necessary code to initialize it, thereby satisfying whatever preconditions there may be. An example could be loading up a database with known parameters from a customer site before running your test. [1]

## The Example
 Sometimes when working with data some functions/operations can take a loooong time. 
 
### Run and explore the example
From the current directory execute:

  ```
  python 
  ```

### Run the tests

  At first, execute the tests without fixtures and observe the execution
  ```
  pytest test_without_fixture.py
  ```

  then execute
  ```
  pytest test_with_fixture.py
  ```  


[1]: [https://en.wikipedia.org/wiki/Test_fixture#Software]
