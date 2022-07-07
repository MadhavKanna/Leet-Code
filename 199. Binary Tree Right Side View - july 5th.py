from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        
        def add_node(root: Optional[TreeNode], level: int, tracker: dict) -> None: 
            if root is None: 
                if level not in tracker.keys(): 
                    tracker[level] = []
            else: 
                if level not in tracker.keys(): 
                    tracker[level] = [root.val]
                else: 
                    tracker[level].append(root.val)
                add_node(root.left, level + 1, tracker)
                add_node(root.right, level + 1, tracker)
                
        right_list = []
        tracker = {}
        add_node(root, 0, tracker)
        for key, value in tracker.items(): 
            if value != []: 
                right_list.append(value[-1])
        return right_list