'''
Title: 821. Shortest Distance to a Character (Easy) https://leetcode.com/problems/shortest-distance-to-a-character/

Runtime: 56 ms, faster than 44.95% of Python online submissions for Shortest Distance to a Character.
Memory Usage: 11.9 MB, less than 5.88% of Python online submissions for Shortest Distance to a Character.

Description:
        Given a string S and a character C, 
        return an array of integers representing the shortest distance from the character C in the string.

Example:
    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0] 

'''

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        output = []
        C_pos = [i for i in range(len(S)) if S[i] == C]
        
        for i in range(len(S)):
            output.append(min([abs(k-i) for k in C_pos]))

        return output