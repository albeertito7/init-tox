"""production code"""

import sys

# global var
NUMBER = 4

def factorial(n):
    # based on the stop condition which manages the simplest cases
    # and the recursive part to multiply the values
    return 1 if (n==1 or n==0) else (n * factorial(n - 1))
    #raise Exception("EX: Just to test")

def main():
	print("Factorial of {} is {}!!".format(NUMBER, factorial(NUMBER)))

if __name__ == "__main__":
	main()