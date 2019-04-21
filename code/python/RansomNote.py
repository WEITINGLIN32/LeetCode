'''
Title: 383. Ransom Note (Easy) https://leetcode.com/problems/ransom-note/

Runtime: 56 ms, faster than 70.32% of Python online submissions for Ransom Note.
Memory Usage: 12.1 MB, less than 5.95% of Python online submissions for Ransom Note.

Description:
        Given an arbitrary ransom note string and another string containing letters from all the magazines, 
        write a function that will return true if the ransom note can be constructed from the magazines ; 
        otherwise, it will return false.
        Each letter in the magazine string can only be used once in your ransom note.

Example:
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true

'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) == 0 and len(ransomNote) == 0:
            return True
        
        char_r = {}
        for i in ransomNote:
            if i in char_r:
                char_r[i] += 1
            else:
                char_r[i] = 1
        
        char_m = {}
        for i in magazine:
            if i in char_m:
                char_m[i] += 1
            else:
                char_m[i] = 1
                
        for i in char_r:
            if i not in char_m:
                return False
                break
            if char_m[i] < char_r[i]:
                return False
                break
                
        return True
        