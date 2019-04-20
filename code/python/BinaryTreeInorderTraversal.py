'''
Title: 94. Binary Tree Inorder Traversal (Medium) https://leetcode.com/problems/two-sum/

Runtime: 36 ms, faster than 82.96% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.1 MB, less than 5.64% of Python3 online submissions for Binary Tree Inorder Traversal.

Description:
        Given a binary tree, return the inorder traversal of its nodes' values.

Example:
    Input: [1,null,2,3]
        1
            \
            2
            /
        3

    Output: [1,3,2]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, root, output):
        if root.left:
            self.search(root.left, output)
        output.append(root.val)
        if root.right:
            self.search(root.right, output)
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        if root:
            self.search(root, output)   
        
        return output
        
        
        
        