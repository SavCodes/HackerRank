#!/bin/python3

# PROBLEM LINK: https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true

# Question: 
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum 
# number of consecutive 1's in n's binary representation.

# INPUT: A single integer, n

#!/bin/python3

import math
import os
import random
import re
import sys

# Generate a string that is the binary representation of the base-10 input
def base_ten_to_binary(n):
    binary_string = " "
    for exponent in range(31, -1, -1):
        if n < 2 ** exponent:
            binary_string += "0"
        else:
            n -= 2 ** exponent
            binary_string += "1"
    return binary_string

# Use sliding window approach to find maximum amount of consecutive 1's in the binary string and display result
def find_max_consecutive(binary_string):
    window_end = 1
    window_start = 0
    while window_end <= len(binary_string):
        if "0" in binary_string[window_start:window_end]:
            window_start += 1
            window_end += 1
        else:
            window_end += 1
    print(window_end - window_start - 1)

# Takes a base-10 integer input and calculates the maximum number of consecutive 1's in its binary representation
if __name__ == '__main__':
    n = int(input().strip())
    binary_string = base_ten_to_binary(n)
    find_max_consecutive(binary_string)
