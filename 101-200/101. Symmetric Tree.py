'''
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false   
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Intuition:
To determine if a binary tree is symmetric, we can check if the left subtree is a mirror image of the right subtree. This can be done by comparing the left and right subtrees recursively.
1. If both left and right subtrees are null, then they are symmetric.
2. If one of the subtrees is null and the other is not, then they are not symmetric.
3. If the values of the current nodes in the left and right subtrees are not equal, then they are not symmetric.
4. If the values are equal, we need to check if the left child of the left subtree is a mirror image of the right child of the right subtree, and if the right child of the left subtree is a mirror image of the left child of the right subtree.

Approach:
1. We can define a helper function `isMirror` that takes two nodes as input and checks if they are mirror images of each other.
2. In the main function `isSymmetric`, we can call the helper function with the left and right children of the root node.
3. The helper function will recursively check the conditions mentioned above to determine if the subtrees are mirror images of each other.


Time Complexity: O(n), where n is the number of nodes in the tree, since we need to visit each node once to check for symmetry.
Space Complexity: O(h), where h is the height of the tree, due to the recursive call stack. In the worst case of a skewed tree, the space complexity would be O(n), where n is the number of nodes in the tree. In a balanced tree, the space complexity would be O(log n).


'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isMirror(self,left,right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        return(
            self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        )
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)