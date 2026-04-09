'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.  A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2
Example 3:
Input: root = []
Output: 0
Example 4:
Input: root = [0]
Output: 1
Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
Follow up: Could you do it without recursion?   

Solution: Recursion
1. We can find the maximum depth of a binary tree using recursion.
2. We define a helper function `maxHeight` that takes a node as an argument.
3. In the `maxHeight` function, we first check if the current node is `None`. If it is, we return 0, indicating that the depth of an empty tree is 0.
4. We recursively call `maxHeight` on the left child of the current node and store the result in `left_height`, and then recursively call `maxHeight` on the right child of the current node and store the result in `right_height`.
5. We return 1 plus the maximum of `left_height` and `right_height`, which gives us the maximum depth of the tree rooted at the current node.   
6. In the main function `maxDepth`, we simply call the `maxHeight` function with the root node and return its result.   

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once.
Space Complexity: O(n) in the worst case (when the tree is completely unbalanced), and O(log n) in the best case (when the tree is completely balanced), due to the recursive call stack.


Solution: Iteration
1. We can also find the maximum depth of a binary tree using an iterative approach with a queue (BFS).
2. We define a helper function `maxHeight` that takes a node as an argument.
3. In the `maxHeight` function, we first check if the current node is `None`. If it is, we return 0, indicating that the depth of an empty tree is 0.
4. We initialize a queue and add the root node to it, and also initialize a variable `height` to keep track of the depth of the tree.
5. We enter a while loop that continues until the queue is empty. Inside the loop, we determine the number of nodes at the current level (which is the size of the queue) and increment the `height` variable by 1.
6. We then iterate over the nodes at the current level, removing each node from the queue and adding its left and right children to the queue if they are not `None`.
7. Once the queue is empty, we have traversed all levels of the tree, and the `height` variable will contain the maximum depth of the tree. We return this value in the main function `maxDepth`.   

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once.
Space Complexity: O(n) in the worst case (when the tree is completely unbalanced), and O(log n) in the best case (when the tree is completely balanced), due to the queue storing nodes at each level.


'''


# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Recursion Approach 

def maxHeight(root):
    if root == None:
        return 0

    left_height = maxHeight(root.left)
    right_height = maxHeight(root.right)

    return 1 + max(left_height, right_height)


# Iterative Approach
def maxHeight(root):

    if root == None:
        return 0
    queue = deque({root})
    height = 0

    while queue:
        level_size = len(queue)
        height += 1

        for _ in range(level_size):
            e = queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)

    return height

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return maxHeight(root)
        