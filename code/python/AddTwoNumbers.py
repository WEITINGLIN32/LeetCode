'''
Title: 2. Add Two Numbers (Medium)

Runtime: 88 ms, faster than 82.52% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.1 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.

Description:
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.   
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output1 = []
        output2 = []
        
        while l1 is not None:
            output1.append(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            output2.append(l2.val)
            l2 = l2.next
        
        result = []
        if len(output1) >= len(output2):
            for i in range(len(output1)):
                if i > len(output2)-1:
                    if output1[i] >= 10 and i!= len(output1) -1:
                        output1[i+1] += 1
                        result.append(output1[i]%10)
                    elif output1[i] >= 10 and i== len(output1) - 1:
                        result.append(output1[i]%10)
                        result.append(1)
                    else:
                        result.append(output1[i])
                else:
                    num = output1[i]+output2[i]
                    if num >= 10 and i != len(output1) - 1:
                        output1[i+1] += 1
                        result.append(num%10)
                    elif num >= 10 and i == len(output1) - 1:
                        result.append(num%10)
                        result.append(1)
                    else:
                        result.append(num%10)

            return result
            
        else:
            for i in range(len(output2)):
                if i > len(output1)-1:
                    if output2[i] >= 10 and i!= len(output2) -1:
                        output2[i+1] += 1
                        result.append(output2[i]%10)
                    elif output2[i] >= 10 and i== len(output2) - 1:
                        result.append(output2[i]%10)
                        result.append(1)
                    else:
                        result.append(output2[i])
                else:
                    num = output2[i]+output1[i]
                    if num >= 10 and i != len(output2) - 1:
                        output2[i+1] += 1
                        result.append(num%10)
                    elif num >= 10 and i == len(output2) - 1:
                        result.append(num%10)
                        result.append(1)
                    else:
                        result.append(num%10)

            return result
