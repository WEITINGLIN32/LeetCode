'''
Title: 21. Merge Two Sorted Lists (Easy)    https://leetcode.com/problems/merge-two-sorted-lists/

Runtime: 44 ms, faster than 88.26% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.

Description:
        Merge two sorted linked lists and return it as a new list. 
        The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = []

        while l1 is not None:
            tmp.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            tmp.append(l2.val)
            l2 = l2.next

        tmp.sort()
        
        return tmp