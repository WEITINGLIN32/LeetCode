'''
Title: 242. Valid Anagram (Easy) https://leetcode.com/problems/valid-anagram/

Runtime: 36 ms, faster than 91.67% of Python online submissions for Valid Anagram.
Memory Usage: 12.7 MB, less than 9.87% of Python online submissions for Valid Anagram.

Description:
        Given two strings s and t , write a function to determine if t is an anagram of s.

Example:
    Input: s = "anagram", t = "nagaram"
    Output: true 

    Input: s = "rat", t = "car"
    Output: false

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
        
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in t:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        
        if len(dict1) > len(dict2):
            for i in dict1:
                if i not in dict2:
                    return False
                else:
                    if dict1[i] != dict2[i]:
                        return False
        else:
            for i in dict2:
                if i not in dict1:
                    return False
                else:
                    if dict1[i] != dict2[i]:
                        return False
        
        return True
        