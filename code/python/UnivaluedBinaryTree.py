'''
Title: 965. Univalued Binary Tree (Easy) https://leetcode.com/problems/univalued-binary-tree/

Runtime: 32 ms, faster than 12.47% of Python online submissions for Univalued Binary Tree.
Memory Usage: 11.9 MB, less than 5.84% of Python online submissions for Univalued Binary Tree.

Description:
        A binary tree is univalued if every node in the tree has the same value.

        Return true if and only if the given tree is univalued.

Example:
    Input: [1,1,1,1,1,null,1]
    Output: true

    Input: [2,2,2,5,2]
    Output: false

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        data = []
        
        def dfs(node):
            if node is not None:
                data.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)

        if len(set(data)) == 1:
            return True
        else:
            return False