'''
Title: 451. Sort Characters By Frequency (Medium) https://leetcode.com/problems/sort-characters-by-frequency/

Runtime: 36 ms, faster than 93.85% of Python online submissions for Sort Characters By Frequency.
Memory Usage: 14.2 MB, less than 36.76% of Python online submissions for Sort Characters By Frequency.

Description:
        Given a string, sort it in decreasing order based on the frequency of characters.

Example:
    Input:
    "tree"

    Output:
    "eert"

    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

    Input:
    "cccaaa"

    Output:
    "cccaaa"

    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.

    Input:
    "Aabb"

    Output:
    "bbAa"

    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.   

'''

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        cnt = [dict[i] for i in dict]
        cnt.sort(reverse=True)
        output = ""
        
        for i in cnt:
            for j in dict:
                if dict[j] == i:
                    output += j * i 
                    dict[j] = -1
        
        return output
        