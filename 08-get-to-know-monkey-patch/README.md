# Getting to know Monkey tests  

Monkeypatch is a built in pytest fixture that lets you replace one object with another at runtime (modify the behavior of existing code). 

Sometimes it is needed while unit testing. This tests are supposed to be "self contained" (they shouldn't need anything other than python to run).

When we talk about data, it means no:

  - CSVs
  - Databases
  - The internet

When we need to load data, but want to isolate our test suite, monkeypatch can he handy


Monkey patching is the  Now, you’ll use patch() to replace your objects in my_calendar.py:


## How to use

The decorator **@pytest.mark.parametrize** enables parametrization of arguments for a test function.

Example:
```
import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

Here, the `@parametrize` decorator defines three different (test_input,expected) tuples so that the test_eval function will run three times using them in turn.


## Activity

Improve the first test case, use your criativity to explore fixtures and python possibilites
