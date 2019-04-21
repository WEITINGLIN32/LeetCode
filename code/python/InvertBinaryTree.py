'''
Title: 226. Invert Binary Tree (Easy) https://leetcode.com/problems/invert-binary-tree/

Runtime: 20 ms, faster than 76.02% of Python online submissions for Invert Binary Tree.
Memory Usage: 11.8 MB, less than 5.29% of Python online submissions for Invert Binary Tree.

Description:
        Invert a binary tree.

Example:
    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root):
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)
            
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.traverse(root)
            
        return root
        