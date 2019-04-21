'''
Title: 414. Third Maximum Number (Easy) https://leetcode.com/problems/third-maximum-number/

Runtime: 44 ms, faster than 34.32% of Python online submissions for Third Maximum Number.
Memory Usage: 12.5 MB, less than 5.05% of Python online submissions for Third Maximum Number.

Description:
        Given a non-empty array of integers, return the third maximum number in this array. 
        If it does not exist, return the maximum number. The time complexity must be in O(n).

Example:
    Input: [3, 2, 1]
    Output: 1
    Explanation: The third maximum is 1.

    Input: [1, 2]
    Output: 2
    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

    Input: [2, 2, 3, 1]
    Output: 1
    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.

'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1
        max_nums = max(nums)
        n = max(nums)
        nums.remove(n)
        while cnt < 3:
            if len(nums) == 1 and n != nums[0]:
                cnt += 1
                n = nums[0]
                nums.remove(n)
            else:
                if len(nums) == 0:
                    return max_nums
                    break
                while n == max(nums):
                    nums.remove(n)
                    if len(nums) == 0:
                        return max_nums
                        break
                else:
                    cnt += 1
                    n = max(nums)
                    nums.remove(n)
            if nums is None and cnt < 3:
                return max_nums
                break
        
        return n
        