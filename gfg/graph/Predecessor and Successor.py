'''
You are given the root of a BST and an integer key. You need to find the inorder predecessor and successor of the given key. If either predecessor or successor is not found, then set it to NULL.

Note: In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than the target is the successor. 

Example 1:
Input:
       50
      /  \
    30    70
   / \   / \
 20 40 60 80
key = 65
Output: 60 70
Explanation: In the above test case, the predecessor of 65 is 60 and successor is 70.

Example 2:
Input:
       50
      /  \
    30    70
   / \   / \
 20 40 60 80
key = 20
Output: -1 30
Explanation: In the above test case, the predecessor of 20 is NULL and successor is 30.

Example 3:
Input:
       50
      /  \
    30    70
   / \   / \
 20 40 60 80
key = 90
Output: 80 -1   

Explanation: In the above test case, the predecessor of 90 is 80 and successor is NULL.

Intuition for solution 1:   
To find the predecessor and successor of a given key in a binary search tree (BST), we can perform an inorder traversal of the tree. During the traversal, we can keep track of the last node visited that is smaller than the key (predecessor) and the first node visited that is greater than the key (successor).

Approach 1: Using Inorder Traversal
1. Perform an inorder traversal of the BST and store the nodes in a list.
2. Iterate through the list of nodes and find the predecessor and successor:
   - If the current node's value is less than the key, update the predecessor to the current node.
   - If the current node's value is greater than the key and the successor is not yet set, update the successor to the current node and break the loop.
   
Time Complexity: O(n), where n is the number of nodes in the BST, since we need to traverse all nodes in the worst case.
Space Complexity: O(n) for storing the nodes in a list during the inorder traversal.

Intuition for solution 2:
To find the predecessor and successor of a given key in a binary search tree (BST) without using extra space for storing nodes, we can take advantage of the properties of the BST. We can traverse the tree starting from the root and keep track of the potential predecessor and successor as we go down the tree.

Approach 2: Using BST Properties
1. Start at the root of the BST.
2. While traversing the tree:
   - If the current node's value is less than the key, update the predecessor to the current node and move to the right subtree (since the successor must be in the right subtree).
   - If the current node's value is greater than the key, update the successor to the current node and move to the left subtree (since the predecessor must be in the left subtree).
3. After the traversal, the predecessor and successor will be set to the appropriate nodes or remain None if not found.
Time Complexity: O(h), where h is the height of the BST, since in the worst case we may need to traverse from the root to a leaf node. In a balanced BST, this would be O(log n).
Space Complexity: O(1) for the iterative approach, since we are not using any extra space for storing nodes.

'''




# Solution 1:
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def dfs(self, root, res):
        if not root:
            return
        self.dfs(root.left, res)
        res.append(root)
        self.dfs(root.right, res)
    def findPreSuc(self, root, key):
        # code here
        res = []
        self.dfs(root,res)
        pre = None
        suc = None
        
        for x in res:
            if x.data < key:
                pre = x
            if x.data> key:
                suc=x
                break
        
        
        return [pre, suc]
        
        
# Solution 2: 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    
    def findPreSuc(self, root, key):
        # code here
       curr = root
       
       pre = None
       suc = None
       
       while curr:
           if curr.data < key:
               pre=curr
               curr=curr.right
             
           else:
                curr=curr.left
            
       curr = root
        
       while curr:
            if curr.data>key:
                suc=curr
                curr=curr.left
            else:
                curr=curr.right
        
       return [pre, suc]
           
        