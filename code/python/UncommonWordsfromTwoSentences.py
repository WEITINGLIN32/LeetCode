'''
Title: 884. Uncommon Words from Two Sentences (Easy) https://leetcode.com/problems/uncommon-words-from-two-sentences/

Runtime: 20 ms, faster than 91.77% of Python online submissions for Uncommon Words from Two Sentences.
Memory Usage: 11.8 MB, less than 6.67% of Python online submissions for Uncommon Words from Two Sentences.

Description:
        We are given two sentences A and B.  (A sentence is a string of space separated words.  
        Each word consists only of lowercase letters.)

        A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

        Return a list of all uncommon words. 

        You may return the list in any order.

Example:
        Input: A = "this apple is sweet", B = "this apple is sour"
        Output: ["sweet","sour"]

        Input: A = "apple apple", B = "banana"
        Output: ["banana"]

'''

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        listA = A.split(' ')
        listB = B.split(' ')
        
        dict = {}
        output = []
        
        for i in listA:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in listB:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for i in dict:
            if dict[i] == 1:
                output.append(i)
                    
        return output