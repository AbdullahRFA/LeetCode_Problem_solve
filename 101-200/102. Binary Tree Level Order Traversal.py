'''
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values' s as a list of lists.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
Follow up: Could you solve it using only constant extra space? (The output array does not count as extra space for space complexity analysis.)

Solution: Iteration for Level Order Traversal
1. We can perform a level order traversal of the binary tree using an iterative approach with a queue (BFS).
2. We define a helper function `traverse` that takes a node and a result list as arguments.
3. In the `traverse` function, we first check if the current node is `None`. If it is, we return immediately.
4. We initialize a queue and add the root node to it, and also initialize an empty list `res` to store the result.
5. We enter a while loop that continues until the queue is empty. Inside the loop, we determine the number of nodes at the current level (which is the size of the queue) and initialize an empty list `level` to store the values of the nodes at the current level.
6. We then iterate over the nodes at the current level, removing each node from the queue and appending its value to the `level` list. If the node has a left child, we add it to the queue, and if it has a right child, we also add it to the queue.
7. After processing all nodes at the current level, we append the `level` list to the `res` list.
8. Once the queue is empty, we have traversed all levels of the tree, and the `res` list will contain the level order traversal of the tree. We return this list in the main function `levelOrder`.

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once.
Space Complexity: O(n) in the worst case (when the tree is completely unbalanced), and O(log n) in the best case (when the tree is completely balanced), due to the queue storing nodes at each level.


'''


from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def traverse(root, res):
    if root == None:
        return
    
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        res.append(level)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        traverse(root,res)
        return res
        