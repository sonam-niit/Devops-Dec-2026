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

def test_div_zero():
    with pytest.raises(ValueError):
        div(10,0)

# Write for multiplication and division
# set up virtual environment to run
# pipenv install pytest
# pipenv shell
# pytest
# it will auto detect test files and test case will executed