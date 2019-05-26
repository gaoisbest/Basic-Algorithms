
def lcs_dp(x, y):
    x_len = len(x)
    y_len = len(y)
    dp = [[0 for j in range(0, y_len+1)] for i in range(0, x_len+1)]
    # max length of common substring
    max_len = -1
    # current end of common substring
    max_end = -1
    for i in range(x_len+1):
        for j in range(y_len+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]: # if x[i] = y[j]
                dp[i][j] = dp[i-1][j-1] + 1

            if dp[i][j] > max_len:
                max_len = dp[i][j]
                max_end = i
    return x[max_end-max_len: max_end]


if __name__ == '__main__':
    x = '11111testets'
    y = 'tdddestets'
    # result: tsitest
    print(lcs_dp(x, y))