import numpy as np
import functools
import timeit


def Fibonacci_matrix_exponentiation(n):
    """
    [[F_n+1, F_n], [F_n, F_n-1]] = [[1, 1], [1, 0]] ^ n
    from https://www.nayuki.io/page/fast-fibonacci-algorithms
    """
    all_matrix = [np.array([[1, 1], [1, 0]]) for i in range(n)]
    return functools.reduce(np.dot, all_matrix)


def Fibonacci_recursive(n):
    """
    Recursive
    T(n) = T(n-1) + T(n-2) + O(1)
    T(n) >= 2T(n-2), O(2^n/2), exponential time.
    """
    if n < 2:
        return n
    else:
        return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)


def Fibonacci_memorization_dp(n, memo):
    """
    Memorization DP algorithms
    fib(k) only recurses the first time
    Time = number of subproblems * time per subproblem, here is n * O(1) = O(n)
    """
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    else:
        rtn = Fibonacci_memorization_dp(n-1, memo) + Fibonacci_memorization_dp(n-2, memo)
        memo[n] = rtn
        return rtn


def Fibonacci_bottom_up_dp(n):
    """
    Bottom-up DP algorithm
    Topological sort of subproblem dependency DAG
    Can save space
    """
    memo = {}
    for i in range(n+1):
        if i <= 2:
            rtn = 1
        else:
            rtn = memo[i-1] + memo[i-2]
        memo[i] = rtn
    return memo[n]


if __name__ == '__main__':
    n = 30

    start = timeit.default_timer()
    F_n = Fibonacci_matrix_exponentiation(n)
    print('Fibonacci_matrix_exponentiation: ', F_n[0][1])
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print('='*100)
    start = timeit.default_timer()
    print('Fibonacci_recursive: ', Fibonacci_recursive(n))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print('=' * 100)
    start = timeit.default_timer()
    memo = {}
    print('Fibonacci_memorization_dp: ', Fibonacci_memorization_dp(n, memo))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print('=' * 100)
    start = timeit.default_timer()
    print('Fibonacci_bottom_up_dp: ', Fibonacci_bottom_up_dp(n))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    """
    Fibonacci_matrix_exponentiation:  832040
    Time:  0.00024427101016044617
    ====================================================================================================
    Fibonacci_recursive:  832040
    Time:  0.42424864901113324
    ====================================================================================================
    Fibonacci_memorization_dp:  832040
    Time:  4.025400266982615e-05
    ====================================================================================================
    Fibonacci_bottom_up_dp:  832040
    Time:  2.078301622532308e-05
    """