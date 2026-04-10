'''
543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:
Input: root = [1,2]
Output: 1
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
Follow up: Could you solve it in O(n) time?

Solution: Recursion
1. We can find the diameter of a binary tree using recursion.
2. We define a helper function `calDiameter` that takes a node as an argument.
3. In the `calDiameter` function, we first check if the current node is `None`. If it is, we return 0, indicating that the height of an empty tree is 0.
4. We recursively call `calDiameter` on the left child of the current node and store the result in `left_height`, and then recursively call `calDiameter` on the right child of the current node and store the result in `right_height`.
5. We update the diameter by taking the maximum of the current diameter and the sum of `left_height` and `right_height`, which gives us the length of the longest path that passes through the current node.
6. We return 1 plus the maximum of `left_height` and `right_height`, which gives us the height of the tree rooted at the current node.   
7. In the main function `diameterOfBinaryTree`, we initialize the diameter to 0 and call the `calDiameter` function with the root node. Finally, we return the diameter.

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once.
Space Complexity: O(n) in the worst case (when the tree is completely unbalanced), and O(log n) in the best case (when the tree is completely balanced), due to the recursive call stack.
'''


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def calDiameter(node):
            if node == None:
                return 0
            left_height = calDiameter(node.left)
            right_height = calDiameter(node.right)
            self.diameter = max(self.diameter, left_height+right_height)
            return 1 + max(left_height, right_height)

        calDiameter(root)

        return self.diameter