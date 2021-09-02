"""
via pytest which is a very simple testing framework easy to use,
yet scales to support complex functionl testing for applications and libraries
we will perform the native assert function for test our production program
"""

from src.main import factorial_recur, factorial

"""
pytest finds all files and modules starting with 'test_' that's why this file name is 'test_main'
and also inside searches for 'test_' again, thus, 'test_factorial' will be executed
even classes are supported for structuring better the code
"""

def test_factorial_recur():
	# functional or unit testing
	assert factorial_recur(4) == 24

def test_factorial():
	assert factorial(4) == 24

def test_all_factorials():
	assert factorial_recur(4) == factorial(4)