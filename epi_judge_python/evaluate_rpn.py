import operator
from typing import List
from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack: List[int] = []
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv,
    }
    tokens = expression.split(',')
    for token in tokens:
        try:
            number = int(token)
        except ValueError:
            # found operator
            right, left = stack.pop(), stack.pop()
            number = operators[token](left, right)

        stack.append(number)

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
