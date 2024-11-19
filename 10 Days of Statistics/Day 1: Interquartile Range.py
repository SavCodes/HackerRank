#!/bin/python3

# PROBLEM LINK: https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Question:
# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).
# Given an array, values, of N integers and an array, freqs, representing the respective frequencies of values's elements, construct
# a data set, S, where each value[i] occurs at frequency freqs[i]. Then calculate and print 's interquartile range, rounded to a 
# scale of 1 decimal place (i.e.,12.3 format).

#INPUT:
# The first line contains an integer, N, the number of elements in arrays values and freqs.
# The second line contains N space-separated integers describing the elements of array values.
# The third line contains  space-separated integers describing the elements of array freqs.

# Finds (Q2) of an array
def find_quartile(array):
    N = len(array)
    if N % 2 == 0:
        return (array[N//2 - 1] + array[N//2]) / 2
    else:
        return array[N//2]
    
# Calculates interquartile range of an array  
def interQuartile(values, freqs):
    N = sum(freqs)
    data_set = zip(values, freqs)
    
    # Creates an array of values each with the appropriate frequency
    full_array = sorted([val for val, freq in data_set for i in range(freq)])
    
    # lower_array will always be up to index N//2 (exclusive)
    lower_array = full_array[:N//2]
    
    # upper_array will vary depending on if N is even or odd
    if N % 2 == 0:
        upper_array = full_array[N//2:]
    else:
        upper_array = full_array[N//2 + 1:]
      
    # Calculate (Q1) and (Q3) to display the interquartile range  
    quartile_one = find_quartile(lower_array)
    quartile_three = find_quartile(upper_array)
    print(f"{round(quartile_three - quartile_one, 1):.1f}")  

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
