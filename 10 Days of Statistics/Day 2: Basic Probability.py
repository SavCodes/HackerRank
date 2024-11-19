#!/bin/python3

# PROBLEM LINK: https://www.hackerrank.com/challenges/s10-mcq-1/problem

# Question:
# In a single toss of  fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

def find_probability():
  count = 0
  total = 0
  for i in range(1,7):
    for j in range(1,7):
      if i + j <= 9:
        count += 1
      total += 1 
  print(count/total)
