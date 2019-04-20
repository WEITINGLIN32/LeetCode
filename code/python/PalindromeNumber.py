'''
Title: 9. Palindrome Number (Easy)

Runtime: 84 ms, faster than 92.47% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.2 MB, less than 5.03% of Python3 online submissions for Palindrome Number.

Description:
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example:
    Input: 121
    Output: true

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        index = int(len(x)) - 1
        istrue = 1
        for i in range(int(len(x)/2)):
            if x[i] != x[index-i]:
                istrue = 0
                break
        if istrue:
            return True

        return False