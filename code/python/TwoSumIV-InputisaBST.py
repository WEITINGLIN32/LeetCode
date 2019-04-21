'''
Title: 653. Two Sum IV - Input is a BST (Easy) https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Runtime: 100 ms, faster than 17.20% of Python online submissions for Two Sum IV - Input is a BST.
Memory Usage: 16.4 MB, less than 5.68% of Python online submissions for Two Sum IV - Input is a BST.

Description:
        Given a Binary Search Tree and a target number, 
        return true if there exist two elements in the BST such that their sum is equal to the given target.

Example:
    Input: 
       5
      / \
     3   6
    / \   \
   2   4   7

    Target = 9

    Output: True

    Input: 
       5
      / \
     3   6
    / \   \
   2   4   7

    Target = 28

    Output: False

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, item):
        if item is not None:
            if item.val in dict:
                dict[item.val] += 1
            else:
                dict[item.val] = 1
            self.traverse(item.left)
            self.traverse(item.right)
            
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        global dict
        dict = {}
        
        if root is not None:
            self.traverse(root)
            
        for i in dict:
            if k - i in dict:
                if i == k - i and dict[i] > 1:
                    return True
                elif i != k - i:
                    return True
                    
        return False
        