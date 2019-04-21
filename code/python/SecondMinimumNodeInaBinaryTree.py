'''
Title: 671. Second Minimum Node In a Binary Tree (Easy) https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

Runtime: 20 ms, faster than 74.81% of Python online submissions for Second Minimum Node In a Binary Tree.
Memory Usage: 11.5 MB, less than 6.06% of Python online submissions for Second Minimum Node In a Binary Tree.

Description:
        Given a non-empty special binary tree consisting of nodes with the non-negative value, 
        where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, 
        then this node's value is the smaller value among its two sub-nodes.

        Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' 
        value in the whole tree.

        If no such second minimum value exists, output -1 instead.

Example:
    Input: 
       2
      / \
     2   5
        / \
       5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.
 
    Input: 
       2
      / \
     2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, root, arr):
        arr.append(root.val)
        if root.left:
            self.DFS(root.left, arr)
        if root.right:
            self.DFS(root.right, arr)
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = []
        
        if root:
            self.DFS(root, arr)
        
        arr.sort()
        
        first = arr[0]
        
        if len(arr) == 1:
            return -1
        for i in range(1,len(arr)):
            if arr[i] > first:
                return arr[i]
                break
            if i == len(arr) - 1:
                return -1