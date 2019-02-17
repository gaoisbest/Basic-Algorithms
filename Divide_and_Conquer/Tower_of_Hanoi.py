
# We have three columns a, b, and c


def move(n, left, middle, right):
    """
    middle is the auxiliary column
    """

    if n == 0:
        return

    # move n-1 from left to middle via right
    move(n-1, left, right, middle)

    # move n from left to right
    print('move {} from {} to {}'.format(n, left, right))
    #right.append(left.pop())

    # move middle to right via left
    move(n-1, middle, left, right)

if __name__ == '__main__':

    '''
    n = 3

    a = [i+1 for i in range(3)]
    b = []
    c = []

    move(n, a, b, c)

    print('a: ', a)
    print('c: ', c)
    '''

    move(3, 'a', 'b', 'c')