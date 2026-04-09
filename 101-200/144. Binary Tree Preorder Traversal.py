'''
144. Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:  
Input: root = []
Output: []
Example 3:
Input: root = [1]
Output: [1]
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?

Solution: Recursion
1. We can perform a preorder traversal of the binary tree using recursion.
2. We define a helper function `preOrder` that takes a node and a result list as arguments.
3. In the `preOrder` function, we first check if the current node is `None`. If it is, we return immediately.
4. We append the value of the current node to the result list, then recursively call `preOrder` on the left child of the current node, and finally recursively call `preOrder` on the right child of the current node.  
5. In the main function `preorderTraversal`, we initialize an empty list `res` to store the result and call the `preOrder` function with the root node and the result list.
6. Finally, we return the result list containing the values of the nodes in preorder traversal order

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once.
Space Complexity: O(n) in the worst case (when the tree is completely unbalanced), and O(log n) in the best case (when the tree is completely balanced), due to the recursive call stack.
'''


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrder(root,res):
    if root == None:
            return
    res.append(root.val)
    preOrder(root.left,res)
    preOrder(root.right,res)


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        preOrder(root, res)
        return res
        