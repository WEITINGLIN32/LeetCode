'''
Title: 344. Reverse String (Easy) https://leetcode.com/problems/reverse-string/

Runtime: 180 ms, faster than 97.87% of Python online submissions for Reverse String.
Memory Usage: 18.8 MB, less than 15.63% of Python online submissions for Reverse String.

Description:
        Write a function that reverses a string. The input string is given as an array of characters char[].
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        You may assume all the characters consist of printable ascii characters.

Example:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        index = len(s)-1
        for i in range(len(s)/2):
            tmp = s[index]
            s[index] = s[i]
            s[i] = tmp
            index -= 1
            
        return s
        