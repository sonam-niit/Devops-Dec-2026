# fixture is reusable data
# pass it as argument, make the changes on it, execute test case and get everytime fresh data

import pytest

@pytest.fixture
def sample_list():
    return [1,2,3]

def test_list_append(sample_list):
    sample_list.append(4)
    assert sample_list == [1,2,3,4]

def test_list_remove(sample_list):
    sample_list.remove(1)
    assert sample_list == [2,3]