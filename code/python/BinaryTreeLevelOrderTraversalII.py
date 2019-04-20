'''
Title: 107. Binary Tree Level Order Traversal II (Easy) https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Runtime: 44 ms, faster than 75.53% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13.3 MB, less than 14.66% of Python3 online submissions for Binary Tree Level Order Traversal II.

Description:
        Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
    [15,7],
    [9,20],
    [3]
    ]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        output = []
        if root:
            thislevel = [root]
            while thislevel:
                tmp = []
                nextlevel = []
                for i in thislevel:
                    tmp.append(i.val)
                    if i.left:
                        nextlevel.append(i.left)
                    if i.right:
                        nextlevel.append(i.right)
                thislevel = nextlevel
                output.append(tmp)
        
        output.reverse()
        
        return output