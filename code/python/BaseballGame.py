'''
Title: 682. Baseball Game (Easy) https://leetcode.com/problems/baseball-game/

Runtime: 36 ms, faster than 27.94% of Python online submissions for Baseball Game.
Memory Usage: 11.9 MB, less than 5.81% of Python online submissions for Baseball Game.

Description:
    You're now a baseball game point recorder.

    Given a list of strings, each string can be one of the 4 following types:

    Integer (one round's score): Directly represents the number of points you get in this round.
    "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
    "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
    "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
    Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example:
    Input: ["5","2","C","D","+"]
    Output: 30
    Explanation: 
    Round 1: You could get 5 points. The sum is: 5.
    Round 2: You could get 2 points. The sum is: 7.
    Operation 1: The round 2's data was invalid. The sum is: 5.  
    Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
    Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

    Input: ["5","-2","4","C","D","9","+","+"]
    Output: 27
    Explanation: 
    Round 1: You could get 5 points. The sum is: 5.
    Round 2: You could get -2 points. The sum is: 3.
    Round 3: You could get 4 points. The sum is: 7.
    Operation 1: The round 3's data is invalid. The sum is: 3.  
    Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
    Round 5: You could get 9 points. The sum is: 8.
    Round 6: You could get -4 + 9 = 5 points. The sum is 13.
    Round 7: You could get 9 + 5 = 14 points. The sum is 27.

'''

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid = []
        score = 0
        
        for i in ops:
            if i == 'C':
                score -= valid[-1]
                valid.remove(valid[-1])
            elif i == 'D':
                score += 2*valid[-1]
                valid.append(2*valid[-1])
            elif i == '+':
                score += (valid[-1] + valid[-2])
                valid.append(valid[-1]+valid[-2])
            else:
                score += int(i)
                valid.append(int(i))
        
        return score
        