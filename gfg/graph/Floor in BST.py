'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        floor = -1
        
        while root:
            if root.data == k:
                return root.data
            
            elif k > root.data:
                floor = root.data
                root=root.right
            else:
                root=root.left
        return floor