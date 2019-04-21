'''
Title: 513. Find Bottom Left Tree Value (Medium) https://leetcode.com/problems/find-bottom-left-tree-value/

Runtime: 36 ms, faster than 91.27% of Python online submissions for Find Bottom Left Tree Value.
Memory Usage: 16.1 MB, less than 15.00% of Python online submissions for Find Bottom Left Tree Value.

Description:
        Given a binary tree, find the leftmost value in the last row of the tree.

Example:
    Input:

        2
       / \
      1   3

    Output:
    1

    Input:

            1
           / \
          2   3
          /   / \
          4   5   6
          /
          7

    Output:
    7   

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dict = {}
        if root:
            height = 0
            thislevel = [root]
            while thislevel:
                height += 1
                nextlevel = []
                values = []
                for i in thislevel:
                    values.append(i.val)
                    if i.left:
                        nextlevel.append(i.left)
                    if i.right:
                        nextlevel.append(i.right)
                dict[height] = values
                thislevel = nextlevel
        
        return dict[max(dict)][0]
        