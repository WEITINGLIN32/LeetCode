'''
Title: 575. Distribute Candies (Easy) https://leetcode.com/problems/distribute-candies/

Runtime: 908 ms, faster than 21.79% of Python online submissions for Distribute Candies.
Memory Usage: 13.5 MB, less than 5.45% of Python online submissions for Distribute Candies.

Description:
        Given an integer array with even length, where different numbers in this array represent different kinds of candies. 
        Each number means one candy of the corresponding kind. 
        You need to distribute these candies equally in number to brother and sister. 
        Return the maximum number of kinds of candies the sister could gain.

Example:
    Input: candies = [1,1,2,2,3,3]
    Output: 3
    Explanation:
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
    The sister has three different kinds of candies. 

    Input: candies = [1,1,2,3]
    Output: 2
    Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
    The sister has two different kinds of candies, the brother has only one kind of candies. 
'''

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kind = {}
        
        for i in candies:
            if i in kind:
                kind[i] += 1
            else:
                kind[i] = 1
        
        
        sis = len(candies) / 2
        max_kinds = 0
        cnt = 0
        
        
        for i in kind:
            if kind[i] == 1 and cnt < sis:
                cnt += 1
                max_kinds += 1
                kind[i] -= 1
 
        for j in kind:
            if cnt < sis and kind[j] > 1:
                cnt += 1
                max_kinds += 1
                kind[j] -= 2

        for k in kind:
            if cnt < sis and kind[k] > 0:
                cnt += 1
                kind[k] -= 1

        return max_kinds
        