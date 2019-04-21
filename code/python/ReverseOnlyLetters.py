'''
Title: 917. Reverse Only Letters (Easy) https://leetcode.com/problems/reverse-only-letters/

Runtime: 32 ms, faster than 15.86% of Python online submissions for Reverse Only Letters.
Memory Usage: 11.9 MB, less than 6.12% of Python online submissions for Reverse Only Letters.

Description:
        Given a string S, return the "reversed" string where all characters 
        that are not a letter stay in the same place, and all letters reverse their positions.

Example:
    Input: "ab-cd"
    Output: "dc-ba"

    Input: "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"

    Input: "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"

'''

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        output = ""
        cnt = len(S)-1
        for i in range(len(S)):
            if (ord(S[i]) >=65 and ord(S[i]) <91) or (ord(S[i]) >=97 and ord(S[i]) <=122):
                if ord(S[i]) >=65 and ord(S[i]) <91 and ord(S[i]) >=97 and ord(S[i]) <=122:
                    output += S[cnt]
                    cnt -= 1
                else:
                    while ord(S[cnt]) < 65 or ord(S[cnt]) > 122 or (ord(S[cnt]) >=91 and ord(S[cnt]) < 97):
                        cnt -= 1
                    output += S[cnt]
                    cnt -= 1
            else:
                output += S[i]
        
        return output
        