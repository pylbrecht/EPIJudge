from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    last = len(s) - 1
    middle = len(s) // 2
    from_start_to_middle = range(len(s) // 2)
    from_end_to_middle = range(last, middle - 1, -1)
    for i, j in zip(from_start_to_middle, from_end_to_middle):
        if s[i] == s[j]:
            continue
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
