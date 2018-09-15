

def insertion_sort(a):
    """left sequence of key element is already sorted"""
    n = len(a)
    # iterate over 1 to n-1
    for j in range(1, n):
        # current element
        key = a[j]
        i = j - 1
        # find approximate index of key
        while (i >= 0) and (a[i] > key):
            a[i+1] = a[i]
            i -= 1
        # since i -= 1 in while loop, i+1 is approximate index
        a[i+1] = key


if __name__ == '__main__':
    a = [54,26,93,17,77,31,44,55,20]
    insertion_sort(a)
    print(a)