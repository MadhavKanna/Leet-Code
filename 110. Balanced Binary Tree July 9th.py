from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_node_balanced(root: Optional[TreeNode]) -> bool:
    """
    stuff
    """
    if root is None:
        return True
    elif root.left is None and root.right is None:
        return True
    elif root.left is None and root.right is not None:
        return find_height(root.right, 0) in (0, 1) and check_node_balanced(root.right)
    elif root.left is not None and root.right is None:
        return find_height(root.left, 0) in (0, 1) and check_node_balanced(root.left)
    else:
        if abs(find_height(root.right, 0) - find_height(root.left, 0)) in (0, 1):
            return check_node_balanced(root.left) and check_node_balanced(root.right)
        else:
            return False


def find_height(root: Optional[TreeNode], height: int) -> int:
    """Return the height from current node to end of the branch"""
    if root is None:
        return 0
    else:
        return 1 + max(find_height(root.left, height + 1), find_height(root.right, height + 1))

test_tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)), TreeNode(3, TreeNode(6)))
