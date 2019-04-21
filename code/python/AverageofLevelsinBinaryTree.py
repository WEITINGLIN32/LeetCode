'''
Title: 637. Average of Levels in Binary Tree (Easy) https://leetcode.com/problems/average-of-levels-in-binary-tree/

Runtime: 60 ms, faster than 21.54% of Python online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.5 MB, less than 5.81% of Python online submissions for Average of Levels in Binary Tree.

Description:
        Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example:
    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]
    Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        output = []
        
        if root:
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
                output.append(float(sum(values)) / len(values))
                thislevel = nextlevel
        
        return output
        