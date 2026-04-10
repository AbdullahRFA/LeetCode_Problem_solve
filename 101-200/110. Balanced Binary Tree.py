'''
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.  For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than one.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:
Input: root = []
Output: true
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
Follow up: Could you solve it with a time complexity of O(n)?

Solution: Recursion
1. We can determine if a binary tree is height-balanced using recursion.
2. We define a helper function `dfs` that takes a node as an argument and returns the height of the tree rooted at that node if it is balanced, or -1 if it is not balanced.
3. In the `dfs` function, we first check if the current node is `None`. If it is, we return 0, indicating that the height of an empty tree is 0.
4. We recursively call `dfs` on the left child of the current node and store the result in `left`. If `left` is -1, it means the left subtree is not balanced, so we return -1 immediately.
5. We recursively call `dfs` on the right child of the current node and store the result in `right`. If `right` is -1, it means the right subtree is not balanced, so we return -1 immediately. 
6. We check if the absolute difference between `left` and `right` is greater than 1. If it is, it means the current node is not balanced, so we return -1.
7. If the current node is balanced, we return 1 plus the maximum of `left` and `right`, which gives us the height of the tree rooted at the current node.

8. In the main function `isBalanced`, we call the `dfs` function with the root node and check if the result is not -1. If it is not -1, it means the tree is balanced, so we return `True`. Otherwise, we return `False`.

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once.
Space Complexity: O(n) in the worst case (when the tree is completely unbalanced), and O(log n) in the best case (when the tree is completely balanced), due to the recursive call stack.
'''


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # self.res = True

        # def dfs(node):
        #     if node == None:
        #         return 0
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     if abs(left-right)>1:
        #         self.res = False
        #     return 1 + max(left, right)
        # dfs(root)
        # return self.res

        def dfs(node):
            if node == None:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1 + max(left,right)

        res = dfs(root)
        return True if res != -1 else False
        