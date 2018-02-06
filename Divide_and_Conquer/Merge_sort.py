"""
Merge sort belongs to Divide_and_Conquer algorithm design technique.
Divide the array into two sub-arrays, sort them and combine them.

Time complexity: O(nlgn)
T(n) = 2*T(n/2) + O(n)
2*T(n/2): two sub-problems
O(n): combine two sorted array into one sorted array.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        # combine two sorted arrays
        i = 0 # left sorted array first element index
        j = 0 # right sorted array first element index
        k = 0 # array last element index
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1

        # if left array has more elements than right array, combine the remains
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        # if right array has more elements than left array, combine the remains
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

        return arr

if __name__ == '__main__':
    a = [4, 10, 1, -7, 100, -100, -200, 1000, 500, 200000, -2300]
    print(merge_sort(a))