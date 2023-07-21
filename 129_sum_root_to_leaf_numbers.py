# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import *

"""
TECHNIQUE: BFS
ALGORITHM:
1. Initialize queue with (root node, number_so_far).
2. While queue is not empty:
    2.1 Pop first node from the queue.
    2.2 Update the number_so far using:  (prev number_so_far * 10) + node.val
    2.3 If this node is a leaf node, add the completed number to the result.
    2.4 Append left and right child nodes to the queue if they aren't empty.
3. Return the result.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
NOTE: The catch here is to create the number by multiplying 10 and adding node.val
    from root -> leaf. 
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue, result = deque([(root, 0)]), 0
        while queue:
            node, number_so_far = queue.popleft()
            curr = (number_so_far * 10) + node.val

            if node.left is None and node.right is None:
                result += curr
            
            if node.left:
                queue.append((node.left, curr))
            if node.right:
                queue.append((node.right, curr))
        
        return result

"""
TECHNIQUE: DFS
ALGORITHM:
1. Create a function traverse with 2 parameters (node, number_so_far).
2. Within the function:
    2.1 Base condition: Return if the node is empty
    2.2 Update the number_so far using: (prev number_so_far * 10) + node.val
    2.3 If the node is a leaf node, add this completed number to nonlocal variable result.
    2.4 Recurse by calling traverse() on both left and right child of the current node.
3. Return result
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], number_so_far = 0):
            nonlocal result
            if not node:
                return
            curr = (number_so_far * 10) + node.val
            if node.left is None and node.right is None:
                result += curr
            traverse(node.left, curr)
            traverse(node.right, curr)

        result = 0
        traverse(root)
        return result

"""
Avoid having a nonlocal variable and calculate result as a return value for this function.
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], prev:int = 0) -> int:
            if not node:
                return 0
            
            curr = (prev * 10) + node.val
            if node.left is None and node.right is None:
                return curr
            
            return traverse(node.left, curr) + traverse(node.right, curr)
        
        return traverse(root)