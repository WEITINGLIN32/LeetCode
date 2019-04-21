'''
Title: 728. Self Dividing Numbers (Easy) https://leetcode.com/problems/self-dividing-numbers/

Runtime: 44 ms, faster than 75.02% of Python online submissions for Self Dividing Numbers.
Memory Usage: 12 MB, less than 5.00% of Python online submissions for Self Dividing Numbers.

Description:
        A self-dividing number is a number that is divisible by every digit it contains.

        For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

        Also, a self-dividing number is not allowed to contain the digit zero.

        Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example:
    Input: 
    left = 1, right = 22
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(left,right+1,1):
            self_divide = 1
            for j in str(i):
                if j == '0':
                    self_divide = 0
                    break
                if i % int(j) != 0 or j == '0':
                    self_divide = 0
                    break
            if self_divide == 1:
                result.append(i)
                
        return result
        