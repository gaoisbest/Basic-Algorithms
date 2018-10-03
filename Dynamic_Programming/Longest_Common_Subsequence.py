"""
Two methods
- Brute-force
    Iterate all sub-sequences in X, find if them exist in Y
    - How many sub-sequence of length m sequence
        - 2^m
    - What is the cost of checking each sub-sequence in sequence y (length of n) ?
        - O(n)
    - Total time: O(n * 2^m)

    reference: http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/DynProg/LCS-brute-force.html

- Dynamic programming
    - Total time: O(n * m)
"""


def lcs_dp(x, y):
    x_len = len(x)
    y_len = len(y)
    c = [[0 for j in range(y_len+1)] for i in range(x_len+1)]

    # compute the table bottom-up
    for idx, a in enumerate(x):
        for jdx, b in enumerate(y):
            if a == b:
                c[idx+1][jdx+1] = 1 + c[idx][jdx]
            else:
                c[idx+1][jdx+1] = max(c[idx+1][jdx], c[idx][jdx+1])

    rtn = ''
    i = x_len
    j = y_len
    while (i>0) and (j>0):
        if c[i][j] == c[i-1][j]:
            i -= 1
        elif c[i][j] == c[i][j-1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            rtn = x[i] + rtn
    return rtn


if __name__ == '__main__':
    x = 'thisisatest'
    y = 'testing123testing'
    # result: tsitest
    print(lcs_dp(x, y))