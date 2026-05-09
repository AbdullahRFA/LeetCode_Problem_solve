'''
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
Input: root = [2,1,3]
Output: true
Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1 

Intuition:
To determine if a binary tree is a valid binary search tree (BST), we can perform an in-order traversal of the tree. In a BST, the in-order traversal will yield values in strictly increasing order. Therefore, we can check if the values obtained from the in-order traversal are in ascending order.

Approach:
1. Perform an in-order traversal of the binary tree and store the values in a list.
2. After the traversal, iterate through the list of values and check if each value is greater than the previous value. If we find any value that is not greater than the previous value, we can conclude that the tree is not a valid BST and return False.
3. If we successfully iterateate through the list without finding any violations, we can return True, indicating that the tree is a valid BST.

Time Complexity: O(n), where n is the number of nodes in the tree, since we need to visit each node once during the in-order traversal. 

Space Complexity: O(n) in the worst case, where n is the number of nodes in the tree, due to the space used to store the values from the in-order traversal. In a balanced tree, the space complexity would be O(h), where h is the height of the tree. 
'''

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root, res):
    if not root:
        return
    dfs(root.left, res)
    res.append(root.val)
    dfs(root.right, res)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        dfs(root,res)

        for i in range(1,len(res)):
            if res[i]<= res[i-1]:
                return False
        return True