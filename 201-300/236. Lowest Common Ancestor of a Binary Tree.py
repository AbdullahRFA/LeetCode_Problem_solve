'''
236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
Explanation: The LCA of nodes 1 and 2 is 1. 

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

Intuition:
To find the lowest common ancestor (LCA) of two nodes in a binary tree, we can use a depth-first search (DFS) approach. We can recursively traverse the tree starting from the root node. During the traversal, we check if the current node is equal to either p or q. If it is, we return the current node. We then recursively search for p and q in the left and right subtrees. If we find p and q in different subtrees, then the current node is the LCA. If we find p and q in the same subtree, we return the node that we found in that subtree. If we do not find either p or q in the current subtree, we return None.

Approach 1: Using recursion
1. Start at the root of the binary tree.
2. If the current node is None, return None.
3. If the current node is equal to p or q, return the current node.
4. Recursively search for p and q in the left and right subtrees.
5. If both left and right recursive calls return non-null values, then the current node is the LCA, so return the current node.
6. If only one of the recursive calls returns a non-null value, return that value.

Time Complexity: O(n), where n is the number of nodes in the tree, since in the worst case we may need to traverse all nodes in the tree.
Space Complexity: O(h) for the recursive approach, due to the call stack. In the worst case of a skewed tree, the space complexity would be O(n), where n is the number of nodes in the tree. In a balanced tree, the space complexity would be O(log n).

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, node, p,q):
        if not node:
            return None
        if node == p or node ==q:
            return node

        left = self.solve(node.left, p ,q)
        right = self.solve(node.right, p ,q)

        if not left and not right:
            return None
        elif not left:
            return right
        elif not right:
            return left
        else:
            return node
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root, p,q)
        