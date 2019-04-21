'''
Title: 506. Relative Ranks (Easy) https://leetcode.com/problems/relative-ranks/

Runtime: 252 ms, faster than 11.09% of Python online submissions for Relative Ranks.
Memory Usage: 12.6 MB, less than 6.25% of Python online submissions for Relative Ranks.

Description:
        Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
        who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example:
    Input: [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
    For the left two athletes, you just need to output their relative ranks according to their scores.

'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medal = ["Gold Medal","Silver Medal","Bronze Medal"]
        output = ["" for i in range(len(nums))]

        tmp = [i for i in nums]
        tmp.sort(reverse=True)
        for index,i in enumerate(tmp):
            if index<3:
                output[nums.index(i)] = medal[index]
            else:
                output[nums.index(i)] = str(index+1)
        return output
        