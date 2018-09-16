"""
Quicksort belongs to Divide and Conquer algorithm design technique.
First find a partition, then quicksort left partition and right partition separately.

Time complexity: O(nlgn)
T(n) = 2*T(n/2) + O(n)
2*T(n/2): two sub-problems
O(n): partition
"""

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


def quicksort(a, p, q):
    if p < q:
        r = partition(a, p, q)
        quicksort(a, p, r)
        # r+1 is must here
        quicksort(a, r+1, q)


if __name__ == '__main__':
    a = [-100, 2, 1, 5, 3, 0]
    quicksort(a, 0, len(a))
    print(a)