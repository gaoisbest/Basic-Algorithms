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


'''
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
'''


def lcs_dp(x, y):
    x_len = len(x)
    y_len = len(y)
    dp = [[0 for j in range(0, y_len+1)] for i in range(0, x_len+1)]

    for i in range(x_len+1):
        for j in range(y_len+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]: # if x[i] = y[j]
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    rtn = ''
    i = x_len
    j = y_len
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j-1]:
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i-1][j-1] + 1:
            i -= 1
            j -= 1
            rtn = x[i] + rtn
    return rtn

if __name__ == '__main__':
    x = 'testets'
    y = 'testets'
    # result: tsitest
    print(lcs_dp(x, y))