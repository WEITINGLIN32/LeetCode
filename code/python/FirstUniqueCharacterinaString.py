'''
Title: 387. First Unique Character in a String (Easy) https://leetcode.com/problems/first-unique-character-in-a-string/

Runtime: 112 ms, faster than 73.83% of Python online submissions for First Unique Character in a String.
Memory Usage: 12.3 MB, less than 5.06% of Python online submissions for First Unique Character in a String.

Description:
        Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Example:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for index,i in enumerate(s):
            if i in dict:
                dict[i][0] += 1
            else:
                dict[i] = []
                dict[i].append(1)
                dict[i].append(index)
        
        pos = []
        
        for i in dict:
            if dict[i][0] == 1:
                pos.append(dict[i][1])
        
        if len(pos) > 0:
            return min(pos)
            
        return -1
        