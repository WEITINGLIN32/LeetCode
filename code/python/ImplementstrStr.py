'''
Title: 28. Implement strStr()    https://leetcode.com/problems/implement-strstr/

Runtime: 36 ms, faster than 87.94% of Python3 online submissions for Implement strStr().
Memory Usage: 13.1 MB, less than 5.13% of Python3 online submissions for Implement strStr().

Description:
        Implement strStr().
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example:
    Input: haystack = "hello", needle = "ll"
    Output: 2

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1