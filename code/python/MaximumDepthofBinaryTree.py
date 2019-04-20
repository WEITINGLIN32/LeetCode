'''
Title: 104. Maximum Depth of Binary Tree (Easy) https://leetcode.com/problems/maximum-depth-of-binary-tree/

Runtime: 48 ms, faster than 87.33% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.5 MB, less than 82.20% of Python3 online submissions for Maximum Depth of Binary Tree.

Description:
        Given a binary tree, find its maximum depth.
        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
        Note: A leaf is a node with no children.

Example:
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its depth = 3.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        
        if root:
            thislevel = [root]
            while thislevel:
                depth += 1
                nextlevel = []
                for i in thislevel:
                    if i.left:
                        nextlevel.append(i.left)
                    if i.right:
                        nextlevel.append(i.right)
                thislevel = nextlevel
                
        return depth
        