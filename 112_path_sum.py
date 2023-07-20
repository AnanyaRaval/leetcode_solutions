# https://leetcode.com/problems/path-sum/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
"""
TECHNIQUE: Pre-order traversal
PROCEDURE:
1. Create a function to traverse the tree with 2 parameters: node and running total.
2. Within traverse:
    2.1 If node is empty, return
    2.2 Add node's value to the running total.
    2.3 If it is a leaf node and we have reached targetSum, turn flag to True.
    2.4 Recurse by traversing on left child and right child, with the new total.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(logn)
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node:Optional[TreeNode], total:int = 0):
            nonlocal found
            if not node:
                return
            
            total += node.val

            if node.left is None and node.right is None and total == targetSum:
                found = True
                return
            traverse(node.left, total)
            traverse(node.right, total)
        
        found = False
        traverse(root)
        return found

"""
Can we remove the flag? We can return a boolean value as the result.
TECHNIQUE: Pre-order traversal
PROCEDURE:
1. Create a function to traverse the tree with 2 parameters: node and running total.
    Return value of the function is a boolean.
2.  Within traverse:
    2.1 If node is empty, return False
    2.2 Add node's value to the running total.
    2.3 If it is a leaf node and we have reached targetSum, return True.
    2.4 Recurse by traversing on left child and right child, with the new total.
        If either of the recursions return True, answer will be True. 
        Hence, do a logical or between the return value of recursions.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(logn)
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node:Optional[TreeNode], total:int = 0) -> bool:
            if not node:
                return False
            total += node.val
            if node.left is None and node.right is None:
                if total == targetSum:
                    return True
            return traverse(node.left, total) or traverse(node.right, total)
        
        return traverse(root)

"""
Converting the above code to an iteration.
TECHNIQUE: Iteration using stack
PROCEDURE:
1. <corner: If root is empty, return False>
2. Initialize stack with root and total = 0.
3. While stack has elements:
    3.1 Add value of node to the running total.
    3.2 If node is a leaf and we have reached targetSum, return True.
    3.3 Add left child and running total to stack.
    3.4 Add right child and running total to stack.
4. If the program hasn't returned earlier, we cannot reach targetSum. return False.
NOTE: Stack is LIFO, hence we pop the latest added elements. This will ensure that we are doing DFS.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        stack = [(root, 0)]

        while stack:
            node, total = stack.pop()
            total += node.val
            if node.left is None and node.right is None:
                if total == targetSum:
                    return True
            
            if node.left:
                stack.append((node.left, total))
            if node.right:
                stack.append((node.right, total))
            
        return False