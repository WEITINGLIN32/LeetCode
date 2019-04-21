'''
Title: 921. Minimum Add to Make Parentheses Valid (Medium) https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Runtime: 24 ms, faster than 55.88% of Python online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 11.7 MB, less than 6.45% of Python online submissions for Minimum Add to Make Parentheses Valid.

Description:
        Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', 
        and in any positions ) so that the resulting parentheses string is valid.

        Formally, a parentheses string is valid if and only if:

        It is the empty string, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.
        Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example:
    Input: "())"
    Output: 1

    Input: "((("
    Output: 3

    Input: "()"
    Output: 0

    Input: "()))(("
    Output: 4

'''

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = 0
        r = 0 
        
        if len(S) == 0:
            return 0
        
        if S[0] == '(':
            l += 1
        else:
            r += 1
        
        
        for i in range(1,len(S)):
            if S[i] == '(':
                l += 1
            elif S[i] == ')' and l > 0:
                l -= 1
            else:
                r += 1
        
        return l + r
        