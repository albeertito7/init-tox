"""production code"""

import sys

# global var
NUMBER = 4

def factorial_recur(n):
    # control condition
    if n < 0 or n == 0:
        raise Exception("The number must be positive!!")

    # based on the stop condition which manages the simplest cases
    # and the recursive part to multiply the values
    return 1 if (n==1 or n==0) else (n * factorial(n - 1))
    #raise Exception("EX: Just to test")

def factorial(n):
    # to take input from the user
    #num = int(input("Enter a number: "))

    if n < 0 or n == 0:
        raise Exception("The number must be positive!!")

    list_range, n = range(2, n + 1), 1
    for i in list_range: n = n*i
    return n

def main():
    print("Typic Factorial of {} is {}!!".format(NUMBER, factorial(NUMBER)))
    print("Recur Factorial of {} is {}!!".format(NUMBER, factorial_recur(NUMBER)))

if __name__ == "__main__":
	main()