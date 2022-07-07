from typing import Optional


class TreeNode:
    """Please work :<"""

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check if binary tree is symmetric"""
        if root.val is None: 
            return True
        
        def generate_tree_left(node: Optional[TreeNode]) -> list:
            if node is None:
                return [None]
            lst = [node.val, generate_tree_left(node.left), generate_tree_left(node.right)]
            return lst

        def generate_tree_right(node: Optional[TreeNode]) -> list:
            if node is None:
                return [None]
            lst = [node.val, generate_tree_right(node.right), generate_tree_right(node.left)]
            return lst

        return generate_tree_left(root.left) == generate_tree_right(root.right)