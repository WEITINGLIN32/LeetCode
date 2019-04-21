'''
Title: 657. Robot Return to Origin (Easy) https://leetcode.com/problems/robot-return-to-origin/

Runtime: 112 ms, faster than 29.41% of Python online submissions for Robot Return to Origin.
Memory Usage: 12.1 MB, less than 6.34% of Python online submissions for Robot Return to Origin.

Description:
        There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, 
        judge if this robot ends up at (0, 0) after it completes its moves.

        The move sequence is represented by a string, and the character moves[i] represents its ith move. 
        Valid moves are R (right), L (left), U (up), and D (down). 
        If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Example:
    Input: "UD"
    Output: true 
    Explanation: The robot moves up once, and then down once.
    All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

    Input: "LL"
    Output: false
    Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. 
    We return false because it is not at the origin at the end of its moves.

'''

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        keys = {'U':0,'D':0,'R':0,'L':0}

        for i in moves:
            if i in keys:
                keys[i] += 1
        if keys['U'] - keys['D'] == 0 and keys['R'] - keys['L'] == 0:
            return True
        else:
            return False