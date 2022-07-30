from tkinter.tix import Tree
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def checkTreeEqual(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """Checks if both the binary trees are equall"""
    if root1 is None and root2 is None: 
        return True
    elif root1 is None or root2 is None: 
        return False
    else: 
        return all(root1.val == root2.val, checkTreeEqual(root1.left, root2.left), checkTreeEqual(root1.right, root2.right))
    
    
if __name__ == "__main__": 
    tree1 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
    tree2 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))