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
    Recursive.
    """
    if n < 2:
        return n
    else:
        return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)


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