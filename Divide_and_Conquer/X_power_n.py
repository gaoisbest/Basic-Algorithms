"""
X to the power of n belongs to Divide_and_Conquer algorithm design technique.
if n is even:
    x^n = x^(n/2) * x^(n/2)
elif n is odd:
    x^n = x^((n-1)/2) * x^((n-1)/2) * x^1
    
Time complexity: O(lgn)
T(n) = T(n/2) + O(1)
T(n/2): one sub-problem
O(1): multiplication operation
"""


def x_power_n(x, n):
    if n == 1:
        return x
    else:
        # if n is even, x^n = x^(n//2) * x^(n//2)
        if n % 2 == 0:
            left = x_power_n(x, n // 2)
            right = left
            return left * right
        # if n is odd, x*n = x^((n-1)//2) * x^((n-1)//2) * x^1
        else:
            left = x_power_n(x, (n-1) // 2)
            right = left
            return left * right * x

if __name__ == '__main__':
    a = 2
    nth = 1
    print(x_power_n(a, nth))