from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def _is_symmetric(subtree0: BinaryTreeNode, subtree1: BinaryTreeNode) -> bool:
    if not subtree0 and not subtree1:
        # leaf
        return True

    if subtree0 and subtree1:
        subtrees_have_equal_data = subtree0.data == subtree1.data
        subtrees_are_symmetric = _is_symmetric(
            subtree0.left, subtree1.right
        ) and _is_symmetric(subtree0.right, subtree1.left)
        return subtrees_have_equal_data and subtrees_are_symmetric

    return False


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return not tree or _is_symmetric(tree.left, tree.right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
