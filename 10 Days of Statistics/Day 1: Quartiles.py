#!/bin/python

# PROBLEM LINK: https://www.hackerrank.com/challenges/s10-quartiles/problem

# Question: Given an array, arr, of N integers, calculate the respective first quartile (Q1), second quartile (Q2),
#           and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

#INPUT: The first line contains an integer, N, the number of elements in arr.
#       The second line contains N space-separated integers, each an arr[i].


# We know that (Q2) of an array, arr, is the same as its median
# Therefore we can deduce that (Q1) of arr is the same as (Q2) arr[:Q2]
# Q(3) can be calculated similarly by finding (Q2) of arr[Q2:]

# Find the median of an array
def find_median(arr, N):
  if N % 2 == 0:
    return int((arr[N//2] + arr[N//2 - 1]) / 2)
  else:
    return int(arr[N//2])

# Split the starting array into lower and upper halves
def split_array(arr, N):
  if N % 2 == 0:
    lower_array = arr[:N//2]
    upper_array = arr[N//2:]
  else:
    lower_array = arr[:N//2]
    upper_array = arr[N//2 + 1:]
  return lower_array, upper_array

# Main function to calculate all three quartiles of an array
def quartiles(data, N):
  data.sort()
  # Pull number of elements in the array, N, from STDIN
  N_updated = N // 2

  # Pull in the array, full_array, from STDIN
  full_array = data
  full_array = [int(num) for num in full_array]

  # Split full array into lower and upper halves to find (Q1) and (Q3)
  lower_array, upper_array =  split_array(full_array, N)
  
  # Find each of the quartiles by calling our find_median() function
  quartile_one = find_median(lower_array, N_updated)
  quartile_two = find_median(full_array, N)
  quartile_three = find_median(upper_array, N_updated)
  return [quartile_one, quartile_two, quartile_three]

  # Print results to STDOUT
  return [quartile_one, quartile_two, quartile_three]
  
if __name__ == "__main__":
  n = int(input("Number of elements in array"))
  data = list(map(int, input().rstrip().split()))
  quartile_list = quartiles(data, n)
  print(quartile_list)
  

