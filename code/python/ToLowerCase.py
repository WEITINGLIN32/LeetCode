'''
Title: 709. To Lower Case (Easy) https://leetcode.com/problems/to-lower-case/

Runtime: 32 ms, faster than 7.58% of Python online submissions for To Lower Case.
Memory Usage: 11.9 MB, less than 5.91% of Python online submissions for To Lower Case.

Description:
        Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example:
    Input: "Hello"
    Output: "hello"

    Input: "here"
    Output: "here"

    Input: "LOVELY"
    Output: "lovely"

'''

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
        