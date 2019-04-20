'''
Title: 27. Remove Element    https://leetcode.com/problems/remove-element/

Runtime: 40 ms, faster than 67.49% of Python3 online submissions for Remove Element.
Memory Usage: 13.1 MB, less than 5.09% of Python3 online submissions for Remove Element.

Description:
        Given an array nums and a value val, remove all instances of that value in-place and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
    Given nums = [3,2,2,3], val = 3,
    Your function should return length = 2, with the first two elements of nums being 2.
    It doesn't matter what you leave beyond the returned length. 

    Given nums = [0,1,2,2,3,0,4,2], val = 2,
    Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
    Note that the order of those five elements can be arbitrary.
    It doesn't matter what values are set beyond the returned length.

'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = [i for i in nums]
        cnt = 0
        for i in range(len(tmp)):
            if tmp[i] == val:
                nums.pop(i-cnt)
                cnt += 1
            if i == len(tmp) -1:
                return len(nums)