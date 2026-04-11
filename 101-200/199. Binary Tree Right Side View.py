
'''
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.   
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:
Input: root = [1,null,3]
Output: [1,3]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Solution: Depth First Search
1. We can use a depth-first search (DFS) approach to traverse the binary tree and collect the values of the nodes that are visible from the right side.
2. We define a helper function `reversePostOrder(node, level, res)` that performs a reverse post-order traversal of the tree. This means we visit the right child first, then the left child, and finally the current node.
3. For each node, we check if the current level is equal to the length of the result list `res`. If it is, it means we are visiting the first node at this level, which is the rightmost node, and we add its value to the result list.
4. We then recursively call the helper function for the right child and then for the left child, incrementing the level by 1 for each recursive call.
5. Finally, we return the result list, which contains the values of the nodes visible from the right side.

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node once.
Space Complexity: O(h), where h is the height of the binary tree, due to the recursive call stack. In the worst case, the height of the tree can be O(n) for a skewed tree, resulting in O(n) space complexity. In the best case, for a balanced tree, the height is O(log n), resulting in O(log n) space complexity.

Solution: Breadth First Search
1. We can also use a breadth-first search (BFS) approach to traverse the binary tree level by level and collect the values of the nodes that are visible from the right side.
2. We can use a queue to perform the level order traversal of the tree. For each level, we can keep track of the last node visited at that level, which will be the rightmost node.
3. We iterate through each level of the tree, and for each node at that level, we add its left and right children to the queue for the next level.
4. After processing all nodes at the current level, we add the value of the last node visited (the rightmost node) to the result list.
5. Finally, we return the result list, which contains the values of the nodes visible from the right side.  

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node once.
Space Complexity: O(w), where w is the maximum width of the binary tree, which is the maximum number of nodes at any level in the tree. In the worst case, for a complete binary tree, the maximum width can be O(n/2) = O(n), resulting in O(n) space complexity. In the best case, for a skewed tree, the maximum width is O(1), resulting in O(1) space complexity.

Solution: Depth First Search (Iterative)
1. We can also use an iterative depth-first search (DFS) approach to traverse the binary tree and collect the values of the nodes that are visible from the right side.
2. We can use a stack to perform the DFS traversal of the tree. We can push the right child of the current node onto the stack before the left child, so that we visit the right child first.
3. We can keep track of the current level and the last node visited at that level, which will be the rightmost node.
4. We iterate through the stack, and for each node, we check if the current level is equal to the length of the result list `res`. If it is, it means we are visiting the first node at this level, which is the rightmost node, and we add its value to the result list.
5. We then push the right child and left child of the current node onto the stack, incrementing the level by 1 for each child.  
6. Finally, we return the result list, which contains the values of the nodes visible from the right side.

Time Complexity: O(n), where n is the number of nodes in the binary tree, since we visit each node once.
Space Complexity: O(h), where h is the height of the binary tree, due to the stack used for the DFS traversal. In the worst case, the height of the tree can be O(n) for a skewed tree, resulting in O(n) space complexity. In the best case, for a balanced tree, the height is O(log n), resulting in O(log n) space complexity.


'''


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # queue = deque([root])
        # res = []

        # while queue:
        #     size = len(queue)
        #     level = []
        #     for _ in range(size):
        #         node = queue.popleft()
        #         if node:
        #             level.append(node.val)
        #         if node and node.left:
        #             queue.append(node.left)
        #         if node and node.right:
        #             queue.append(node.right)
        #     if level:
        #         res.append(level[-1])

        # return res

        # queue = deque([root])
        # res = []

        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.popleft()
        #         if i==size-1 and node:
        #             res.append(node.val)
        #         if node and node.left:
        #             queue.append(node.left)
        #         if node and node.right:
        #             queue.append(node.right)
            

        # return res
        def reversePostOrder(node, level, res):
            if node == None:
                return 
            if level == len(res):
                res.append(node.val)
            if node.right:
                reversePostOrder(node.right, level+1, res)
            if node.left:
                reversePostOrder(node.left, level+1, res)
            
        res = []
        reversePostOrder(root, 0, res)
        return res
                

        