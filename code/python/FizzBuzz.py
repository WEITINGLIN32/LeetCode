'''
Title: 412. Fizz Buzz (Easy) https://leetcode.com/problems/two-sum/

Runtime: 36 ms, faster than 97.22% of Python online submissions for Fizz Buzz.
Memory Usage: 12.6 MB, less than 5.63% of Python online submissions for Fizz Buzz.

Description:
        Write a program that outputs the string representation of numbers from 1 to n.
        But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
        For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
    n = 15,

    Return:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]

'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = "Fizz"
        b = "Buzz"
        c = "FizzBuzz"
        
        output = []
        
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append(c)
            elif i % 3 == 0:
                output.append(a)
            elif i % 5 == 0:
                output.append(b)
            else:
                output.append(str(i))
        
        return output
        