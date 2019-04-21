'''
Title: 914. X of a Kind in a Deck of Cards (Easy) https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

Runtime: 132 ms, faster than 33.95% of Python online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 12.1 MB, less than 6.25% of Python online submissions for X of a Kind in a Deck of Cards.

Description:
        In a deck of cards, each card has an integer written on it.

        Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 
        or more groups of cards, where:

        Each group has exactly X cards.
        All the cards in each group have the same integer.

Example:
    Input: [1,2,3,4,4,3,2,1]
    Output: true
    Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

    Input: [1,1,1,2,2,2,3,3]
    Output: false
    Explanation: No possible partition.

    Input: [1]
    Output: false
    Explanation: No possible partition.

    Input: [1,1]
    Output: true
    Explanation: Possible partition [1,1]

    Input: [1,1,2,2,2,2]
    Output: true
    Explanation: Possible partition [1,1],[2,2],[2,2]

'''

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dict = {}
        
        for i in deck:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        istrue = []
        for i in range(2,max(dict.values())+1):
            tmp = 1
            for j in dict:
                if dict[j] % i != 0:
                    tmp = 0
                    break
            if tmp == 1:
                return True
                break
        
        if len(istrue) == 0: 
            return False
        