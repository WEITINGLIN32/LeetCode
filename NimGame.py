'''
Title: 292. Nim Game (Easy) https://leetcode.com/problems/nim-game/

Runtime: 20 ms, faster than 69.91% of Python online submissions for Nim Game.
Memory Usage: 11.7 MB, less than 5.36% of Python online submissions for Nim Game.

Description:
        You are playing the following Nim Game with your friend: There is a heap of stones on the table, 
        each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. 
        You will take the first turn to remove the stones.
        Both of you are very clever and have optimal strategies for the game. 
        Write a function to determine whether you can win the game given the number of stones in the heap.

Example:
    Input: 4
    Output: false 
    Explanation: If there are 4 stones in the heap, then you will never win the game;
                No matter 1, 2, or 3 stones you remove, the last stone will always be 
                removed by your friend.
'''

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n % 4 == 0
        