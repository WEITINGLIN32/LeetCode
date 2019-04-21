'''
Title: 461. Hamming Distance (Easy) https://leetcode.com/problems/hamming-distance/

Runtime: 20 ms, faster than 77.98% of Python online submissions for Hamming Distance.
Memory Usage: 11.7 MB, less than 5.53% of Python online submissions for Hamming Distance.

Description:
        The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
        Given two integers x and y, calculate the Hamming distance.

Example:
    Input: x = 1, y = 4

    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

    The above arrows point to positions where the corresponding bits are different.

'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        
        if x>y:
            while x >= 1:
                if y >= 1:
                    tmp1 = x % 2
                    tmp2 = y % 2
                    if tmp1 != tmp2:
                        count+=1
                    
                else:
                    tmp1 = x % 2
                    if tmp1 == 1:
                        count+=1
                x = int(x / 2)
                y = int(y / 2)
        else:
             while y >= 1:
                if x >= 1:
                    tmp1 = y % 2
                    tmp2 = x % 2
                    if tmp1 != tmp2:
                        count+=1
                  
                else:
                    tmp1 = y % 2
                    if tmp1 == 1:
                        count+=1   
                x = int(x / 2)
                y = int(y / 2)
        return count
                
        