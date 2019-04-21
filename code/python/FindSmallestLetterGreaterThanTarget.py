'''
Title: 744. Find Smallest Letter Greater Than Target (Easy) https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Runtime: 92 ms, faster than 26.08% of Python online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 14 MB, less than 6.17% of Python online submissions for Find Smallest Letter Greater Than Target.

Description:
        Given a list of sorted characters letters containing only lowercase letters, 
        and given a target letter target, find the smallest element in the list that is larger than the given target.

        Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Example:
    Input:
    letters = ["c", "f", "j"]
    target = "a"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "c"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "d"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "g"
    Output: "j"

    Input:
    letters = ["c", "f", "j"]
    target = "j"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "k"
    Output: "c"

'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in range(len(letters)):
            if ord(letters[i]) > ord(target):
                return letters[i]
                break
            if i == len(letters) - 1:
                return letters[0]