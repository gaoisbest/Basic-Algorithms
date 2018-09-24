"""
Find the i-th element.
Expected running time O(n).
Worst case is O(n^2), but the probability is really small.
"""

import random


def partition(a, p, q):
    # pick first element as pivot
    pivot = a[p]
    # element whose index less than i is less than or equal to pivot
    i = p
    # element whose index between i and j is large than pivot
    # O(n)
    for j in range(i+1, q):
        if a[j] <= pivot:
            i += 1
            # do exchange
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    # exchange pivot and a[i]
    a[p] = a[i]
    a[i] = pivot
    return i


def rand_partition(a, p, q):
    # generate a random index
    random_index = random.randint(p, q - 1)
    # swap first element with random number
    tmp = a[p]
    a[p] = a[random_index]
    a[random_index] = tmp
    return partition(a, p, q)


def quick_select(a, p, q, idx):
    if p == q:
        return a[p]

    r = rand_partition(a, p, q)
    
    if idx == r:
        return a[r]
    elif idx < r:
        return quick_select(a, p, r, idx)
    else:
        return quick_select(a, r+1, q, idx)


if __name__ == '__main__':
    a = [60, 200, 10, 20]
    print(quick_select(a, 0, len(a), 0))
