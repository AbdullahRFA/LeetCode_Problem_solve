'''
112. Path Sum
Easy
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children.
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree: (1 --> 2) and (1 --> 3).
    Neither of them sums to 5.
Example 3:
Input: root = [1,2], targetSum = 0
Output: false
Explanation: There is one root-to-leaf path in the tree: (1 --> 2).
    Neither of them sums to 0.
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000


Intuition:
1. We can solve this problem by using a depth-first search (DFS) approach. We will start from the root of the tree and keep track of the current sum of the values along the path. If we reach a leaf node and the current sum equals the target sum, then we can return true. If we reach a leaf node and the current sum does not equal the target sum, then we can return false. If we are at a non-leaf node, we will continue to explore the left and right subtrees.  

Approach:
1. We will define a recursive function that takes the current node and the current sum as arguments.
2. If the current node is null, we will return false.
3. if the right and left child of the current node is null, then we will check if the target sum is equal to the current node value. if it is, then we will return true, otherwise we will return false.
4. If the current node is not a leaf node, we will recursively call the function for the left and right child of the current node, and we will update target sum by subtracting the current node value from it.
5. Finally, we will return the result of the recursive calls for the left and right child of the current node.

Time Complexity: O(n), where n is the number of nodes in the binary tree. We will need to visit each node in the tree once, which takes O(n) time.
Space Complexity: O(h), where h is the height of the binary tree. In the worst case, if the binary tree is skewed (i.e., all nodes have only one child), the height of the tree will be equal to the number of nodes in the tree, which takes O(n) space. In the best case, if the binary tree is balanced, the height of the tree will be log(n), which takes O(log n) space. In general, the space complexity will be O(h) due to the recursive call stack, where h is the height of the binary tree.

Another Solution:

Intuition:
1. We can also solve this problem by using a breadth-first search (BFS) approach. We will use a queue to keep track of the nodes that we need to visit, along with the current sum of the values along the path. We will start from the root of the tree and keep track of the current sum of the values along the path. If we reach a leaf node and the current sum equals the target sum, then we can return true. If we reach a leaf node and the current sum does not equal the target sum, then we can return false. If we are at a non-leaf node, we will continue to explore the left and right subtrees by adding them to the queue.

Approach:
1. We will initialize a queue and add the root node along with its value to the queue.
2. We will then enter a loop that continues until the queue is empty.
3. In each iteration of the loop, we will dequeue a node and its corresponding current sum from the queue.
4. If the current node is a leaf node, we will check if the current sum equals the target sum. If it does, we will return true. If it does not, we will continue to the next iteration of the loop.
5. If the current node is not a leaf node, we will add its left and right child to the queue along with the updated current sum (i.e., current sum + left child value and current sum + right child value).
6. Finally, if we exit the loop without finding a path that sums to the target sum, we will return false.

Time Complexity: O(n), where n is the number of nodes in the binary tree. We will need to visit each node in the tree once, which takes O(n) time.
Space Complexity: O(w), where w is the maximum width of the binary tree. In the worst case, if the binary tree is a complete binary tree, the maximum width of the tree will be equal to the number of nodes in the last level of the tree, which takes O(n) space. In the best case, if the binary tree is skewed (i.e., all nodes have only one child), the maximum width of the tree will be 1, which takes O(1) space. In general, the space complexity will be O(w) due to the queue used for BFS, where w is the maximum width of the binary tree.

Another Solution:
Intuition:
1. We can also solve this problem by using a breadth-first search (BFS) approach, but instead of keeping track of the current sum of the values along the path, we can keep track of the remaining target sum that we need to achieve. We will start from the root of the tree and keep track of the remaining target sum that we need to achieve. If we reach a leaf node and the remaining target sum equals the value of the leaf node, then we can return true. If we reach a leaf node and the remaining target sum does not equal the value of the leaf node, then we can return false. If we are at a non-leaf node, we will continue to explore the left and right subtrees by adding them to the queue along with the updated remaining target sum (i.e., remaining target sum - left child value and remaining target sum - right child value

Approach:
1. We will initialize a queue and add the root node along with the target sum to the queue.
2. We will then enter a loop that continues until the queue is empty.
3. In each iteration of the loop, we will dequeue a node and its corresponding remaining target sum from the queue.
4. If the current node is a leaf node, we will check if the remaining target sum equals the value of the leaf node. If it does, we will return true. If it does not, we will continue to the next iteration of the loop.
5. If the current node is not a leaf node, we will add its left and right child to the queue along with the updated remaining target sum (i.e., remaining target sum - left child value and remaining target sum - right child value).
6. Finally, if we exit the loop without finding a path that sums to the target sum, we will return false.

Time Complexity: O(n), where n is the number of nodes in the binary tree. We will need to visit each node in the tree once, which takes O(n) time.
Space Complexity: O(w), where w is the maximum width of the binary tree. In the worst case, if the binary tree is a complete binary tree, the maximum width of the tree will be equal to the number of nodes in the last level of the tree, which takes O(n) space. In the best case, if the binary tree is skewed (i.e., all nodes have only one child), the maximum width of the tree will be 1, which takes O(1) space. In general, the space complexity will be O(w) due to the queue used for BFS, where w is the maximum width of the binary tree.


'''

from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
        
#         if not root.right and not root.left:
#             return targetSum == root.val
        
#         return self.hasPathSum(root.right, targetSum-root.val) or self.hasPathSum(root.left, targetSum-root.val)


# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
        
#         queue = deque()
#         queue.append([root, root.val])

#         while queue:
#             node, curr_sum = queue.popleft()
#             if not node.left and not node.right and curr_sum == targetSum:
#                 return True
#             if node.left:
#                 queue.append([node.left, curr_sum+node.left.val])
#             if node.right:
#                 queue.append([node.right, curr_sum+node.right.val])
#         return False


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque()
        queue.append([root, targetSum])

        while queue:
            node, curr_sum = queue.popleft()
            if not node.left and not node.right and curr_sum == node.val:
                return True
            if node.left:
                queue.append([node.left, curr_sum-node.val])
            if node.right:
                queue.append([node.right, curr_sum-node.val])
        return False