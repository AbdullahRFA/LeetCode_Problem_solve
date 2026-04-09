'''
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values. 
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
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
1. We can perform an inorder traversal of the binary tree using recursion.
2. We define a helper function `inOrder` that takes a node and a result list as arguments.
3. In the `inOrder` function, we first check if the current node is `None`. If it is, we return immediately.
4. We recursively call `inOrder` on the left child of the current node, then append the value of the current node to the result list, and finally recursively call `inOrder` on the right child of the current node.    
5. In the main function `inorderTraversal`, we initialize an empty list `res` to store the result and call the `inOrder` function with the root node and the result list.   
6. Finally, we return the result list containing the values of the nodes in inorder traversal order.

'''



from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inOrder(root, res):
    if root == None:
        return
    inOrder(root.left,res)
    res.append(root.val)
    inOrder(root.right,res)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        inOrder(root, res)
        return res
        