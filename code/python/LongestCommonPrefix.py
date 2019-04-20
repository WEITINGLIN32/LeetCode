'''
Title: 14. Longest Common Prefix (Easy)    https://leetcode.com/problems/longest-common-prefix/

Runtime: 40 ms, faster than 73.25% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.2 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.

Description:
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".

Example:
    Input: ["flower","flow","flight"]
    Output: "fl"

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = ""
        count = 0
        isend = 0
        if len(strs) > 0:
            while True:

                for i in range(len(strs)):
                    if count >= len(strs[i]):
                        isend = 1
                        break
                if isend:
                    break
                tmp = strs[0][count]
                isTrue = 1
                for i in range(1,len(strs)):
                    if tmp != strs[i][count]:
                        isTrue = 0
                        break
                if isTrue:
                    str += strs[0][count]
                    count += 1
                else:
                    break
        return str