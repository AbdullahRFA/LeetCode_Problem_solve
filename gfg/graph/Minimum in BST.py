"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        temp = root
        while temp and temp.left:
            
            temp=temp.left
            
                
        return temp.data