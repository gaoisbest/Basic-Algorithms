"""
The number of permutation of AABBBC is 6!/(2!*3!)

https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""
import copy

def permute(a, l, r):
    if l == r:
        print(copy.deepcopy(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            # restore the state to before recursive
            a[l], a[i] = a[i], a[l] # backtrack

a = ['1', '2', '3']
permute(a, 0, len(a))