import pytest
from mycalculator.my_calculator_functions import *

'''
@pytest.mark.parametrize("a,b,result",[(1,2,3), (2,4,6)])
def test_add(a,b,result):
    value = add(a,b)
    assert value == result


def test_add_negative_positive():
    value = add(-1,2,3)
    assert value == 4

def test_add_negative_negative():
    value = add(-1,-2)
    assert value == -5
'''

def test_over_ten_variables():
    """My first documentation of this method
    testing for more than 10 variables
    
    Input
    ------------
    1,2,3,4,5,6,7,8,9,0
    
    Outcome
    ----------
    Error: >10 Values
    
    """
    value = add(1,2,3,4,5,6,7,8,9,10,11, 12)
    assert value == "Error: >10 Values" ##

