'''
Title: 779. K-th Symbol in Grammar (Medium) https://leetcode.com/problems/k-th-symbol-in-grammar/

Runtime: 20 ms, faster than 73.76% of Python online submissions for K-th Symbol in Grammar.
Memory Usage: 11.5 MB, less than 5.26% of Python online submissions for K-th Symbol in Grammar.

Description:
        On the first row, we write a 0. Now in every subsequent row, we look at the previous row 
        and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

        Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Example:
    Examples:
    Input: N = 1, K = 1
    Output: 0

    Input: N = 2, K = 1
    Output: 0

    Input: N = 2, K = 2
    Output: 1

    Input: N = 4, K = 5
    Output: 1

    Explanation:
    row 1: 0
    row 2: 01
    row 3: 0110
    row 4: 01101001

'''

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if(K==1):
            return 0
        if(K==2):
            return 1
        if(K%2==1):
            return self.kthGrammar(-1, (K+1)/2)
        else:
            return 1-self.kthGrammar(-1, K/2)
        