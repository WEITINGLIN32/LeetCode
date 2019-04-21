'''
Title: 844. Backspace String Compare (Easy) https://leetcode.com/problems/backspace-string-compare/

Runtime: 24 ms, faster than 56.90% of Python online submissions for Backspace String Compare.
Memory Usage: 11.7 MB, less than 5.06% of Python online submissions for Backspace String Compare.

Description:
        Given two strings S and T, return if they are equal when both are typed into empty text editors. 
        # means a backspace character.

Example:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

'''

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        j = []
        
        for i in S:
            if i != '#':
                s.append(i)
            else:
                if len(s) > 0:
                    s.pop()
        
        for i in T:
            if i != '#':
                j.append(i)
            else:
                if len(j) > 0:
                    j.pop()

        return s == j
        