#!/bin/python3

# PROBLEM LINK: https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Question:
# Given an array, arr, of N integers, calculate and print the standard deviation. Your answer should
# be in decimal form, rounded to a scale of 1 decimal place (i.e.,12.3 format). An error margin of 
# +/- 1 will be tolerated for the standard deviation.

# INPUT:
#  The first line contains an integer, N, denoting the size of arr.
#  The second line contains N space-separated integers that describe arr.

# Calculated Standard Deviation
def standard_deviation(arr):
    N = len(arr)
    mean = sum(arr) / N                                    # Calculate the mean of arr
    square_distance_sum = sum((x-mean)**2 for x in arr)    # Calculate sum (x[i] - mean)^2 for x in arr
    standard_deviation = (square_distance_sum / N) ** 0.5  # Calculate standard deviation
    print(f"{standard_deviation:.1f}")                     # Display formatted results
    
if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    standard_deviation(vals)
