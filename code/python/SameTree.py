'''
Title: 100. Same Tree (Easy) https://leetcode.com/problems/same-tree/

Runtime: 36 ms, faster than 81.46% of Python3 online submissions for Same Tree.
Memory Usage: 13.3 MB, less than 5.74% of Python3 online submissions for Same Tree.

Description:
        Given two binary trees, write a function to check if they are the same or not.
        Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example:
    Input:     1         1
            / \       / \
            2   3     2   3

            [1,2,3],   [1,2,3]

    Output: true

    Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

    Output: false

    Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

    Output: false

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BFS(self, root, tree):
        thislevel = [root]
        while thislevel:
            nextlevel = []
            for i in thislevel:
                if i == "Null":
                    tree.append("Null")
                    continue
                tree.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                else:
                    nextlevel.append("Null")
                if i.right:
                    nextlevel.append(i.right)
                else:
                    nextlevel.append("Null")
            thislevel = nextlevel 
            
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tree1 = []
        tree2 = []
        
        if p:
            self.BFS(p, tree1)
        if q:
            self.BFS(q, tree2)

        return tree1 == tree2
        