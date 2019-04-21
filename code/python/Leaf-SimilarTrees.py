'''
Title: 872. Leaf-Similar Trees (Easy) https://leetcode.com/problems/leaf-similar-trees/

Runtime: 24 ms, faster than 56.79% of Python online submissions for Leaf-Similar Trees.
Memory Usage: 12 MB, less than 5.62% of Python online submissions for Leaf-Similar Trees.

Description:
        Consider all the leaves of a binary tree.  
        From left to right order, the values of those leaves form a leaf value sequence.

        For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

        Two binary trees are considered leaf-similar if their leaf value sequence is the same.

        Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, root,list):
        if root is not None:
            self.DFS(root.left,list)
            self.DFS(root.right,list)
            if not root.left and not root.right:
                list.append(root.val)
                
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1 = []
        list2 = []
        if root1 is not None:
            self.DFS(root1, list1)
        if root2 is not None:
            self.DFS(root2,list2)
        
        return list1 == list2
        