'''
Title: 830. Positions of Large Groups (Easy) https://leetcode.com/problems/positions-of-large-groups/

Runtime: 28 ms, faster than 100.00% of Python online submissions for Positions of Large Groups.
Memory Usage: 11.8 MB, less than 5.00% of Python online submissions for Positions of Large Groups.

Description:
        In a string S of lowercase letters, these letters form consecutive groups of the same character.

        For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

        Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

        The final answer should be in lexicographic order.

Example:
    Input: "abbxxxxzzy"
    Output: [[3,6]]
    Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

    Input: "abc"
    Output: []
    Explanation: We have "a","b" and "c" but no large group.

    Input: "abcdddeeeeaabbbcd"
    Output: [[3,5],[6,9],[12,14]]

'''

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        output = []
        tmp = []
        init = S[0]
        count = 1
        tmp.append(0)
        for i in range(1,len(S)):
            if init == S[i]:
                count+=1
                if i == len(S)-1 and count>=3:
                    tmp.append(i)
                    output.append(tmp)
            else:
                init = S[i]
                if count>=3:
                    tmp.append(i-1)
                    output.append(tmp)
                
                tmp = []
                tmp.append(i)
                count = 1
        return output
        