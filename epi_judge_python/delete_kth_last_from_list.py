from typing import Optional
from collections import deque

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy = ListNode(0, L)
    first = dummy.next
    for _ in range(k):
        first = first.next

    second = dummy
    while first:
        first, second = first.next, second.next

    second.next = second.next.next

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
