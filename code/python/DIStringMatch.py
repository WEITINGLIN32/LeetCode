'''
Title: 942. DI String Match (Easy) https://leetcode.com/problems/di-string-match/

Runtime: 56 ms, faster than 100.00% of Python online submissions for DI String Match.
Memory Usage: 13 MB, less than 5.40% of Python online submissions for DI String Match.

Description:
        Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

        Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

        If S[i] == "I", then A[i] < A[i+1]
        If S[i] == "D", then A[i] > A[i+1]

Example:
    Input: "IDID"
    Output: [0,4,1,3,2]

    Input: "III"
    Output: [0,1,2,3]

    Input: "DDI"
    Output: [3,2,0,1]

'''

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low = 0; high = len(S)
        output = []
        for i in S:
            if i == 'I':
                output.append(low)
                low += 1
            else:
                output.append(high)
                high -= 1
        return output + [low]
        