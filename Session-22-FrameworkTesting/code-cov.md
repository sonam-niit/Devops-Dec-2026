# Code Coverage in testing

- to measure code coverage while running test case we can use code coverage
- it tells how much code is actually tested.

- using pytest-cov module

- find untested code
- improve code quality
- important for CI/CD pipeline

*use Same code written in Previous class*

- calulator.py

```py
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    if num2==0:
        raise ValueError("Cannot Divide by zero")
    return num1/num2
```

- calc_test.py

```py
import pytest
from calculator import add,sub,mul,div
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_sub():
    assert sub(4,3) == 1
    assert sub(0,3) == -3
    assert sub(-1,1) == -2
```

- now install required dependency
- pipenv install pytest pytest-cov
- pipenv shell
- pytest --cov=calculator 

*you can see 60% of code coverage*

- then update the code by adding mul and div test

```py
def test_mul():
    assert mul(4,3) == 12

def test_div():
    assert div(4,2) == 2
```

- again check:  pytest --cov=calculator 
- you can see 90% of code coverage

- update code with Error Test

```py
def test_div_zero():
    with pytest.raises(ValueError):
        div(2,0)
```

- now when you run: pytest --cov=calculator 
- you can see 100% of code coverage

- If you wnat to generate HTML Report
- pytest --cov=calculator --cov-report=html

- you can see folder html-cov
- open from you files and try to open index.html in browser 
- you can see generated report