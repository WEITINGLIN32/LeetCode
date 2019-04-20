'''
Title: 66. Plus One (Easy) https://leetcode.com/problems/plus-one/

Runtime: 36 ms, faster than 98.68% of Python3 online submissions for Plus One.
Memory Usage: 13.1 MB, less than 5.29% of Python3 online submissions for Plus One.

Description:
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
        You may assume the integer does not contain any leading zero, except the number 0 itself.

Example:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits)-1] + 1 < 10:
            digits[len(digits)-1]+=1
            return digits
        else:
            digits[len(digits)-1] = 0
            for i in range(len(digits)-2,-1,-1):
                digits[i] += 1
                if digits[i] < 10:
                    return digits
                    break
                else:
                    digits[i] = 0
            if digits[0] == 0:
                digits.insert(0,1)
                return digits
        