'''
Title: 206. Reverse Linked List (Easy) https://leetcode.com/problems/reverse-linked-list/

Runtime: 28 ms, faster than 56.42% of Python online submissions for Reverse Linked List.
Memory Usage: 13.6 MB, less than 25.52% of Python online submissions for Reverse Linked List.

Description:
        Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        item = []
        
        while tmp:
            item.append(tmp.val)
            tmp = tmp.next
        item = item[::-1]
        tmp = head
        for i in item:
            tmp.val = i
            tmp = tmp.next
        
        return head