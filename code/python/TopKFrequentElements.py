'''
Title: 347. Top K Frequent Elements (Medium) https://leetcode.com/problems/top-k-frequent-elements/

Runtime: 196 ms, faster than 11.32% of Python online submissions for Top K Frequent Elements.
Memory Usage: 15 MB, less than 5.25% of Python online submissions for Top K Frequent Elements.

Description:
        Given a non-empty array of integers, return the k most frequent elements.

Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Input: nums = [1], k = 1
    Output: [1]

'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        output = []
        
        
        for i in range(k):
            max_value = max(dict.values())
            for j in dict:
                if dict[j] == max_value:
                    dict[j] = -1
                    output.append(j)
                    break
        
        return output
        