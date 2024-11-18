#!/bin/python3

# PROBLEM LINK: https://www.hackerrank.com/challenges/exceptions/problem

# Question: You are given two values a and b. Perform integer division and print a/b.
# In the case of ZeroDivisionError or ValueError, print the error code.

# INPUT: The first line contains T, the number of test cases.
#        The next  lines each contain the space separated values of a and b

num_test_cases = int(input())

for case_index in range(num_test_cases):
    case = input("a b").split()
    a, b = case[0], case[1]
    
    try:
        print(int(a) // int(b))
        
    except ValueError as e:
        print("Error Code:", e)
    
    except ZeroDivisionError as e:
        print("Error Code:", e)
