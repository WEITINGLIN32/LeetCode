'''
Title: 144. Binary Tree Preorder Traversal (Medium) https://leetcode.com/problems/binary-tree-preorder-traversal/

Runtime: 36 ms, faster than 81.49% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.2 MB, less than 6.12% of Python3 online submissions for Binary Tree Preorder Traversal.

Description:
        Given a binary tree, return the preorder traversal of its nodes' values.

Example:
    Input: [1,null,2,3]
       1
        \
         2
        /
       3

    Output: [1,2,3

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root, output):
        output.append(root.val)
        if root.left:
            self.traverse(root.left, output)
        if root.right:
            self.traverse(root.right, output)
            
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        if root:
            self.traverse(root, output)
        
        return output