"""
Randomnized quicksort is independent of input order.
No assumption about input distribution.
Worst-case determined only by random number generator

Time complexity: O(nlgn)
T(n) = 2*T(n/2) + O(n)
2*T(n/2): two sub-problems
O(n): partition
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

def randomized_partition(a, p, q):
    # generate a random index
    random_index = random.randint(p, q-1)
    # swap first element with random number
    tmp = a[p]
    a[p] = a[random_index]
    a[random_index] = tmp
    return partition(a, p, q)

def quicksort(a, p, q):
    if p < q:
        r = randomized_partition(a, p, q)
        quicksort(a, p, r)
        # r+1 is must here
        quicksort(a, r+1, q)


if __name__ == '__main__':
    a = [-100, 2, 1, 5, 3, 0]
    quicksort(a, 0, len(a))
    print(a)