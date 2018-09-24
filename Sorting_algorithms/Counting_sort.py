"""
Time complexity: O(n + k)
stable sorting algorithm

The lower bound of comparison sorting algorithm is O(nlgn).
"""


def counting_sort(A, k):
    C = [0] * k
    B = [0] * len(A)

    for j in range(len(A)):
        C[A[j]] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B


if __name__ == '__main__':
    k = 4001
    A = [4000, 100, 300, 400, 103]
    B = counting_sort(A, k)
    print(B)