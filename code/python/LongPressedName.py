'''
Title: 925. Long Pressed Name (Easy) https://leetcode.com/problems/long-pressed-name/

Runtime: 20 ms, faster than 86.53% of Python online submissions for Long Pressed Name.
Memory Usage: 11.7 MB, less than 6.06% of Python online submissions for Long Pressed Name.

Description:
        Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, 
        and the character will be typed 1 or more times.

        You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, 
        with some characters (possibly none) being long pressed.

Example:
    Input: name = "alex", typed = "aaleex"
    Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.

    Input: name = "saeed", typed = "ssaaedd"
    Output: false
    Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

    Input: name = "leelee", typed = "lleeelee"
    Output: true

    Input: name = "laiden", typed = "laiden"
    Output: true
    Explanation: It's not necessary to long press any character.

'''

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        for i in typed:
            if len(name) == 0:
                break
            if name[0] == i:
                name = name[1:]
            else:
                continue
                
        if len(name) == 0:
            return True
        
        return False