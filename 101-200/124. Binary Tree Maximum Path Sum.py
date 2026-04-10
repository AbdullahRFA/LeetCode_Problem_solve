'''
124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.   
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 1 -> 2 -> 3 with a sum of 6.
Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a sum of 42.
Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000   

Solution: Depth First Search
1. We can use a depth-first search (DFS) approach to traverse the binary tree and calculate the maximum path sum.
2. We define a helper function `dfs(node)` that returns the maximum path sum starting from the given node and extending downwards.
3. For each node, we calculate the maximum path sum for the left and right subtrees. If the maximum path sum for either subtree is negative, we can ignore it by treating it as 0.
4. We then update the global maximum path sum by considering the path that goes through the current node and both subtrees.
5. Finally, we return the maximum path sum found during the traversal.

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node once.
Space Complexity: O(h), where h is the height of the binary tree, due to the recursive call stack. In the worst case, the height of the tree can be O(n) for a skewed tree, resulting in O(n) space complexity. In the best case, for a balanced tree, the height is O(log n), resulting in O(log n) space complexity.
'''


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if node == None:
                return 0
            left = dfs(node.left)
            if left < 0:
                left = 0
            right = dfs(node.right)
            if right < 0:
                right = 0
            self.max_sum = max(self.max_sum,(node.val+left+right))
            return node.val+max(left,right)
        dfs(root)
        return self.max_sum
        