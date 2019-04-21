'''
Title: 819. Most Common Word (Easy) https://leetcode.com/problems/most-common-word/

Runtime: 52 ms, faster than 8.96% of Python online submissions for Most Common Word.
Memory Usage: 11.9 MB, less than 5.05% of Python online submissions for Most Common Word.

Description:
        Given a paragraph and a list of banned words, 
        return the most frequent word that is not in the list of banned words.  
        It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

        Words in the list of banned words are given in lowercase, and free of punctuation.  
        Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:
    Input: 
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    Output: "ball"
    Explanation: 
    "hit" occurs 3 times, but it is a banned word.
    "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
    Note that words in the paragraph are not case sensitive,
    that punctuation is ignored (even if adjacent to words, such as "ball,"), 
    and that "hit" isn't the answer even though it occurs more because it is banned.

'''

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        parse = ""
        
        for index,i in enumerate(paragraph):
            if ord(i) >= 65 and ord(i) <= 91:
                parse += chr(ord(i) + 32)   
                if index < len(paragraph) - 1:
                    if not ((ord(paragraph[index+1]) >= 65 and ord(paragraph[index+1]) <= 91) or (ord(paragraph[index+1]) >= 97 and \
                                                                                                  ord(paragraph[index+1]) <= 123)):
                        key = 1
                        
            elif ord(i) >= 97 and ord(i) <= 123:
                parse += i
                if index < len(paragraph) - 1:
                    if not ((ord(paragraph[index+1]) >= 65 and ord(paragraph[index+1]) <= 91) or (ord(paragraph[index+1]) >= 97 and \
                                                                                                  ord(paragraph[index+1]) <= 123)):
                        key = 1
            else:
                if key:
                    parse += ' '
                    key = 0
                
                


        dict = {}
        for i in parse.split(' '):
            if i in dict and i not in banned:
                dict[i] += 1
            elif i not in dict and i not in banned:
                dict[i] = 1
  
        m = max(dict.values())
        for i in dict:
            if dict[i] == m and len(i) > 0: 
                return i
        