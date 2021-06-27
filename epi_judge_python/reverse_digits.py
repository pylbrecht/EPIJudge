from test_framework import generic_test


def reverse(x: int) -> int:
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
