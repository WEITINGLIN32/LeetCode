'''
Title: 515. Find Largest Value in Each Tree Row (Medium) https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Runtime: 40 ms, faster than 93.88% of Python online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 16.2 MB, less than 6.06% of Python online submissions for Find Largest Value in Each Tree Row.

Description:
        You need to find the largest value in each row of a binary tree.

Example:
    Input: 

            1
           / \
          3   2
         / \   \  
        5   3   9 

    Output: [1, 3, 9]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root, output):
        thislevel = [root]
        while thislevel:
            nextlevel = []
            values = []
            for i in thislevel:
                values.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            output.append(max(values))
            thislevel = nextlevel
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        
        if root:
            self.traverse(root, output)
        
        return output
        