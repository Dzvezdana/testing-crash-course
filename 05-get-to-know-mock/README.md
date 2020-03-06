# Getting to know Mocks
It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

And why is it useful? Because sometimes it is time consuming or impossible to deal with the real things over and over again. 

Examples:

- Analising a data model. It can take hours, so most of time (when we talk about testing) you can simply fake the results of some actions.

- Quering a database. 
  Imagine a very long and complex query, or that you don't even have access to the database for testing

- Calling apis. Many free APIs have limited and/or throttled requests. If you make hundreds of requests to an api you'll run out of quota or will have to leave the free tier boundaries. 

By mocking you can simulate the behaviour of such functionalities and save time, or maybe $$


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
