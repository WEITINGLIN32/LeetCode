'''
Title: 938. Range Sum of BST (Medium) https://leetcode.com/problems/range-sum-of-bst/

Runtime: 364 ms, faster than 16.22% of Python online submissions for Range Sum of BST.
Memory Usage: 28.9 MB, less than 5.00% of Python online submissions for Range Sum of BST.

Description:
        Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

        The binary search tree is guaranteed to have unique values.

Example:
    Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    Output: 32

    Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
    Output: 23

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, node):
        if node is not None:
            if node.val in num:
                num[node.val] += 1
            else:
                num[node.val] = 1
            self.DFS(node.left)
            self.DFS(node.right)
            
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        global num
        num = {}
        
        if root is not None:
            self.DFS(root)
        
        output = 0
        for i in num:
            if i >= L and i <= R:
                output += num[i] * i
        return output