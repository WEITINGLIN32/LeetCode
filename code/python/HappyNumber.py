'''
Title: 202. Happy Number (Easy) https://leetcode.com/problems/happy-number/

Runtime: 44 ms, faster than 77.35% of Python3 online submissions for Happy Number.
Memory Usage: 13.4 MB, less than 5.29% of Python3 online submissions for Happy Number.

Description:
    Write an algorithm to determine if a number is "happy".
    A happy number is a number defined by the following process: Starting with any positive integer, 
    replace the number by the sum of the squares of its digits, 
    and repeat the process until the number equals 1 (where it will stay), 
    or it loops endlessly in a cycle which does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers.

Example:
    Input: 19
    Output: true
    Explanation: 
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        dict = {}
        num = n
        while True:
            str1 = ""
            for i in str(num):
                str1 += i
            digit = [pow(int(i), 2) for i in str1]
            if sum(digit) in dict and sum(digit) != 1:
                return False
                break
            elif sum(digit) not in dict and sum(digit) != 1:
                dict[sum(digit)] = 1
            elif sum(digit) == 1:
                return True
                break
            num = sum(digit)
        