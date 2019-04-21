'''
Title: 783. Minimum Distance Between BST Nodes (Easy) https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Runtime: 60 ms, faster than 8.16% of Python online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 12.1 MB, less than 5.68% of Python online submissions for Minimum Distance Between BST Nodes.

Description:
        Given a Binary Search Tree (BST) with the root node root, 
        return the minimum difference between the values of any two different nodes in the tree.

Example:
    Input: root = [4,2,6,1,3,null,null]
    Output: 1
    Explanation:
    Note that root is a TreeNode object, not an array.

    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

              4
            /   \
          2      6
         / \    
        1   3  

    while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, root, values):
        values.append(root.val)
        if root.left:
            self.DFS(root.left, values)
        if root.right:
            self.DFS(root.right, values)
            
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = []
        
        if root:
            self.DFS(root, values)
            
        dict = {}
        
        for i in range(len(values)):
            for j in range(len(values)):
                if i != j:
                    dict[abs(values[i] - values[j])] = 1
        
        return min(dict)