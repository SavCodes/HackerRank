!# /bin/python3

# QUESTION:

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below N.

def find_sum(n):
    n = n - 1

    # We can deduce there are n//k multiples of k
    # Each valid multiple can be thought of as 3*i for integers i <= n//k
    three_total = sum(3*i for i in range(n//3 + 1)) 
    five_total = sum(5*i for i in range(n//5 + 1))

    # We need to calculate and subtract the redundant multiples
    fift_total = sum(15*i for i in range(n//15 +1))
  
    print(three_total + five_total - fift_total)

#   FAILED: Although this solution works it fails the time constraints required for the 
#           problem. This is most likely because this solution runs with O(n/k)) = O(n)
#           time complexity coming from the sum() function. The solution must require an
#           O(1) constant time complexity


def find_sum_2(n):
  


  
