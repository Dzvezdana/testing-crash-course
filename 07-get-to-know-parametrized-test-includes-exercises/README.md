# Getting to know Parametrized tests

Pytest enables test parametrization at several levels:

- pytest.fixture() allows one to parametrize fixture functions.

- @pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class.

- pytest_generate_tests allows one to define custom parametrization schemes or extensions.


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

- Improve the first test case, use your criativity to explore fixtures and python possibilites
- The example uses the setup_method configuration step, take a look at https://docs.pytest.org/en/latest/xunit_setup.html and try to use some other setup functions.
