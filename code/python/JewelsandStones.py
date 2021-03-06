'''
Title: 771. Jewels and Stones (Easy) https://leetcode.com/problems/jewels-and-stones/

Runtime: 20 ms, faster than 99.82% of Python online submissions for Jewels and Stones.
Memory Usage: 11.7 MB, less than 5.25% of Python online submissions for Jewels and Stones.

Description:
        You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
        Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

        The letters in J are guaranteed distinct, and all characters in J and S are letters. 
        Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example:
    Input: J = "aA", S = "aAAbbbb"
    Output: 3

    Input: J = "z", S = "ZZ"
    Output: 0

'''

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in S:
            if i in J:
                count += 1
        return count
        