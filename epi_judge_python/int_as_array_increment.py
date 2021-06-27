from typing import List
from collections import deque

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    carry = A[-1] // 10

    if not carry:
        return A

    result = deque()
    result.appendleft(A[-1] % 10)

    for digit in reversed(A[:-1]):
        digit += carry
        carry = digit // 10
        result.appendleft(digit % 10)

    if carry:
        result.appendleft(1)

    return list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
