'''
Title: 824. Goat Latin (Easy) https://leetcode.com/problems/goat-latin/

Runtime: 32 ms, faster than 10.77% of Python online submissions for Goat Latin.
Memory Usage: 11.9 MB, less than 5.40% of Python online submissions for Goat Latin.

Description:
        A sentence S is given, composed of words separated by spaces. 
        Each word consists of lowercase and uppercase letters only.

        We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

        The rules of Goat Latin are as follows:

        If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
        For example, the word 'apple' becomes 'applema'.
        
        If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".
        
        Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
        Return the final sentence representing the conversion from S to Goat Latin. 

Example:
    Input: "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    Input: "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

'''

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        string = S.split(' ')
        output = ""
        
        for i in range(len(string)):
            if string[i][0] in vowels:
                output += string[i][:]
                output += 'ma'
                output += 'a' * (i+1)
                if i != len(string)-1:
                    output += ' '
            else:
                output += string[i][1:]
                output += string[i][0]
                output += 'ma'
                output += 'a' * (i+1)
                if i != len(string)-1:
                    output += ' '
        
        return output