# Created by: shyraffy
# Recursive and iterative implementation of the binary search algorithm. 

import math

def binary_srch(v, n):
    left = 0
    right = len(v) - 1

    while left <= right:
        m = math.floor((left + right) / 2) ## Calculates the middle point
        current = v[m]
        
        if current < n:
            left = m + 1
        elif current > n:
            right = m - 1
        else:
            return m

    return -1

def binary_srch_recursive(v, n, left, right):
    if left > right:
        return -1
    else:
        m = math.floor((left + right) / 2)
        current = v[m]
        if current < n:
            return binary_srch_recursive(v, n, m + 1, right)
        elif current > n:
            return binary_srch_recursive(v, n, left, m - 1)
        else:
            return m

        

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8]
        
    ##result = binary_srch(vector, 9)

    result = binary_srch_recursive(array, 7, 0, len(array) - 1)
    
    if result == -1:
        print("Search unsuccessful")
    else:
        print(f"Number found at {result}")
