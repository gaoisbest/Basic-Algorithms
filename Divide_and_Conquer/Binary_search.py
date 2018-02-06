"""
Binary search belongs to Divide_and_Conquer algorithm design technique.
Given a sorted array, according to the comparison result between find
value and middle value, search find value in half array for each iteration.

Time complexity: O(lgn)
T(n) = T(n/2) + O(1)
T(n/2): one sub-problem
O(1): compare find value with middle value
"""


def binary_search(arr, find_value):
    rtn_idx = -1
    left = 0
    right = len(arr) - 1
    while left <= right: # '<=' is valid and '<' does not work
        middle = (left + right) // 2
        if arr[middle] == find_value:
            rtn_idx = middle
            break
        elif arr[middle] > find_value:
            right = middle - 1
        else:
            left = middle + 1
    return rtn_idx


if __name__ == '__main__':
    value = 7
    a = [1, 7, 10, 300, 2000]
    print(binary_search(a, value))