'''
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:  
Input: root = [2,1], p = 2, q = 1
Output: 2
Constraints:    
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

Intuition for BST:
To find the lowest common ancestor (LCA) of two nodes in a binary search tree (BST), we can take advantage of the properties of a BST. In a BST, the value of each node is greater than the values of all nodes in its left subtree and less than the values of all nodes in its right subtree.
Given two nodes p and q, we can compare their values with the value of the current node during our traversal. If both p and q have values less than the current node's value, then the LCA must be in the left subtree. If both p and q have values greater than the current node's value, then the LCA must be in the right subtree. If one of p or q has a value less than the current node's value and the other has a value greater than the current node's value, then the current node is the LCA.

Intuition for Binary Tree:
To find the lowest common ancestor (LCA) of two nodes in a binary tree, we can use a depth-first search (DFS) approach. We can recursively traverse the tree starting from the root node. During the traversal, we check if the current node is equal to either p or q. If it is, we return the current node. We then recursively search for p and q in the left and right subtrees. If we find p and q in different subtrees, then the current node is the LCA. If we find p and q in the same subtree, we return the node that we found in that subtree. If we do not find either p or q in the current subtree, we return None.  

Approach 1: Using recursion
1. Start at the root of the BST.
2. If the current node is None, return None.
3. If the current node is equal to p or q, return the current node.
4. Recursively search for p and q in the left and right subtrees.   
5. If both left and right recursive calls return non-null values, then the current node is the LCA, so return the current node.
6. If only one of the recursive calls returns a non-null value, return that value.

Time Complexity: O(h), where h is the height of the tree, since in the worst case we may need to traverse from the root to a leaf node.
Space Complexity: O(h) for the recursive approach, due to the call stack. In the worst case of a skewed tree, the space complexity would be O(n), where n is the number of nodes in the tree. In a balanced tree, the space complexity would be O(log n).

Approach 2: Using iteration with recursion
1. Start at the root of the BST.
2. Compare the values of p and q with the value of the current node.
3. If both p and q are less than the current node, move to the left child.
4. If both p and q are greater than the current node, move to the right child.
5. If one of p or q is less than the current node and the other is greater than the current node, return the current node as the LCA.

Time Complexity: O(h), where h is the height of the tree, since in the worst case we may need to traverse from the root to a leaf node.
Space Complexity: O(h) for the recursive approach, due to the call stack. In the worst case of a skewed tree, the space complexity would be O(n), where n is the number of nodes in the tree. In a balanced tree, the space complexity would be O(log n).


Approach 3 : Using iteration without recursion
1. Start at the root of the BST.
2. Compare the values of p and q with the value of the current node.
3. If both p and q are less than the current node, move to the left child.
4. If both p and q are greater than the current node, move to the right child.
5. If one of p or q is less than the current node and the other is greater than the current node, return the current node as the LCA.

Time Complexity: O(h), where h is the height of the tree, since in the worst case we may need to traverse from the root to a leaf node.
Space Complexity: O(1) for the iterative approach, as we are not using any additional data structures. If we use recursion, the space complexity would be O(h) due to the call stack.
'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Solution 1: Using recursion
    # def solve(self, root, p,q):
    #     if not root:
    #         return None
    #     if root==p or root==q:
    #         return root
    #     left = self.solve(root.left, p,q)
    #     right = self.solve(root.right, p,q)

    #     if not left and not right:
    #         return None
    #     elif not left:
    #         return right
    #     elif not right:
    #         return left
    #     return root
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     return self.solve(root, p,q)
    
    # Solution 2: Using iteration without recursion
    # def solve(self, root, p,q):
    #     if not root:
    #         return None
    #     if p.val<root.val and q.val<root.val:
    #         return self.solve(root.left, p,q)
    #     if p.val>root.val and q.val>root.val:
    #         return self.solve(root.right, p,q)
    #     if p==root or q==root:
    #         return root
    #     if (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
    #         return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return self.solve(root, p,q)
        
        # Solution 3 : Using iteration without recursion

        while True:
            if p.val < root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            elif p==root or q==root:
                return root
            else:
                return  root