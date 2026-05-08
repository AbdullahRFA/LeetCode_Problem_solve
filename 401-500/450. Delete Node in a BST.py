# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def findLastRight(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        while node.right:
            node = node.right
        return node

    def delNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        
        right_child = node.right
        last_right = self.findLastRight(node.left)
        last_right.right=right_child
        return node.left


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            root = self.delNode(root)
        
        temp = root

        while temp:
            if temp.val > key:
                if temp.left and temp.left.val == key:
                    temp.left = self.delNode(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.delNode(temp.right)
                    break
                else:
                    temp = temp.right
        return root
        