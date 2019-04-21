'''
Title: 338. Counting Bits (Medium) https://leetcode.com/problems/counting-bits/

Runtime: 96 ms, faster than 76.97% of Python online submissions for Counting Bits.
Memory Usage: 16.9 MB, less than 5.29% of Python online submissions for Counting Bits.

Description:
    Given a non negative integer number num. 
    For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
    Input: 2
    Output: [0,1,1]

    Input: 5
    Output: [0,1,1,2,1,2]

'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        output = []
        dict = {}
        
        for i in range(num+1):
            tmp = i
            count = 0
            while tmp>0:
                if tmp % 2 == 1:
                    count+=1
                tmp = int(tmp/2)
                if tmp in dict:
                    count += dict[tmp]
                    dict[i] = count
                    tmp = 0
            else:
                if i not in dict:
                    dict[i] = count
                output.append(count)
        return output