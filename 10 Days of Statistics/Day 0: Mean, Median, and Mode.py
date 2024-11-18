!/bin/python3

# QUESTION Given an array, X, of N integers, calculate and print the respective mean, median, 
# and mode on separate lines. If your array contains more than one modal value, choose the 
# numerically smallest one.

# Mean: The sum of all elements over the number of elements
def find_mean(arr, N):
  return sum(num/N for num in arr)

# Mode: Most commonly occuring value
# This solution runs in O(n^2) time because of the count() function nested our num_set loop
# This can be optimized by using a dictionary counter or hashmap (see second solution at bottom)
def find_mode(arr):
  num_set = sorted(set(arr))
  max_count = 0
  for num in num_set:
    current_count = arr.count(num)
    if current_count > max_count:
      mode = num
      max_count = current_count
  return mode

# Median: Middle element of the array (Average of two middle elements if N is even)
def find_median(arr, N):
  # N = 4 = [1,2,3,4]
  if N % 2 == 0:
    return (arr[N//2] + arr[N//2 - 1]) / 2
  else:
    return arr[N//2]

# Attempting to optimize the find_mode() function
# Using a dictionary counter reduces time complexity to O(n)
def find_mode_optimized(arr, N):
  frequency_dictionary = dict()
  for num in arr:
    frequency_dictionary[num] = frequency_dictionary.get(num, 0) + 1
  return max(frequency_dictionary, key=frequency_dictionary.get)
