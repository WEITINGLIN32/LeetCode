'''
Title: 557. Reverse Words in a String III (Easy) https://leetcode.com/problems/reverse-words-in-a-string-iii/

Runtime: 48 ms, faster than 38.44% of Python online submissions for Reverse Words in a String III.
Memory Usage: 12.7 MB, less than 6.35% of Python online submissions for Reverse Words in a String III.

Description:
        Given a string, you need to reverse the order of characters in each word within 
        a sentence while still preserving whitespace and initial word order.

Example:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        
        tmp = s.split(' ')
        
        for index,i in enumerate(tmp):
            output += i[::-1]
            if index != len(tmp)-1:
                output += ' '
        
        return output
            