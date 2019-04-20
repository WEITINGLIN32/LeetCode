'''
Title: 83. Remove Duplicates from Sorted List (Easy) https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Runtime: 56 ms, faster than 24.85% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13 MB, less than 5.26% of Python3 online submissions for Remove Duplicates from Sorted List.

Description:
        Given a sorted linked list, delete all duplicates such that each element appear only once.

Example:
    Input: 1->1->2
    Output: 1->2

    Input: 1->1->2->3->3
    Output: 1->2->3

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = []
        
        while head is not None:
            if head.val not in tmp:
                tmp.append(head.val)
            head = head.next
        
            
        
        return tmp
        