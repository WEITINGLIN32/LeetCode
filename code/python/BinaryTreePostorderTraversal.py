'''
Title: 145. Binary Tree Postorder Traversal (Hard) https://leetcode.com/problems/binary-tree-postorder-traversal/

Runtime: 36 ms, faster than 81.29% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.2 MB, less than 5.65% of Python3 online submissions for Binary Tree Postorder Traversal.

Description:
        Given a binary tree, return the postorder traversal of its nodes' values.

Example:
    Input: [1,null,2,3]
       1
        \
         2
        /
       3

    Output: [3,2,1]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root, output):
        if root.left:
            self.traverse(root.left, output)
        
        if root.right:
            self.traverse(root.right, output)
        
        output.append(root.val)
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        if root:
            self.traverse(root, output)
        
        return output
        