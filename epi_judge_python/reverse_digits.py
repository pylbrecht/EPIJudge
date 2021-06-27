from test_framework import generic_test

import math


def reverse(x: int) -> int:
    sign = int(math.copysign(1, x))
    x = abs(x)
    result = 0
    while x > 0:
        digit = x % 10
        x = x // 10
        result = (result * 10) + digit

    return sign * result


def reverse_brute_force(x: int) -> int:
    try:
        _, number = str(x).split('-')
    except ValueError:
        sign = 1
        number = str(x)
    else:
        sign = -1
    return sign * int(number[-1::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
