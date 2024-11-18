#!/bin/python3

# QUESTION: 

# Given an array, X, of N integers and an array, W, representing the respective weights of X's elements,
# calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1
# decimal place (i.e.,12.3  format).


# Weighted Mean:
# Find the product of an element in X and its repective weight in W for all elements in X,W
# Find the sum of all the products and divide by the sum of the weights

def find_weighted_mean(arr, weights):
  sum_weights = sum(weights)
  sum_products = sum(num*weight for num, weight in zip(arr, weights))
  return sum_products / sum_weights
  
  
