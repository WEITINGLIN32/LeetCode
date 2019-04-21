'''
Title: 876. Middle of the Linked List (Easy) https://leetcode.com/problems/middle-of-the-linked-list/

Runtime: 28 ms, faster than 10.87% of Python online submissions for Middle of the Linked List.
Memory Usage: 11.8 MB, less than 6.82% of Python online submissions for Middle of the Linked List.

Description:
        Given a non-empty, singly linked list with head node head, return a middle node of linked list.

        If there are two middle nodes, return the second middle node.

Example:
    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

    Input: [1,2,3,4,5,6]
    Output: Node 4 from this list (Serialization: [4,5,6])
    Since the list has two middle nodes with values 3 and 4, we return the second one.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        output = head
        
        length = 0
        
        while head is not None:
            length += 1
            head = head.next
        
        for i in range(length/2):
            output = output.next
        
        return output