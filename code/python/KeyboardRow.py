'''
Title: 500. Keyboard Row (Easy) https://leetcode.com/problems/keyboard-row/

Runtime: 20 ms, faster than 76.79% of Python online submissions for Keyboard Row.
Memory Usage: 11.7 MB, less than 5.48% of Python online submissions for Keyboard Row.

Description:
        Given a List of words, 
        return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = ['Q','W','E','R','T','Y','U','I','O','P','q','w','e','r','t','y','u','i','o','p']
        line2 = ['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l']
        line3 = ['Z','X','C','V','B','N','M','z','x','c','v','b','n','m']
        output = []
        for i in words:
            arr = [0,0,0]
            for j in i:
                if j in line1:
                    arr[0] += 1
                elif j in line2:
                    arr[1] += 1
                else:
                    arr[2] += 1
            cnt = 0
            for j in arr:
                if j>0:
                    cnt+=1
            if cnt == 1:
                output.append(i)
        return output
        