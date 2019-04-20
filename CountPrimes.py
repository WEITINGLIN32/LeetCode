'''
Title: 204. Count Primes (Easy) https://leetcode.com/problems/count-primes/

Runtime: 1124 ms, faster than 24.97% of Python online submissions for Count Primes.
Memory Usage: 94.6 MB, less than 5.33% of Python online submissions for Count Primes.

Description:
        Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''

class Solution(object):
    def countPrimes(self, n):     
        if n>1:
            isprime = [True for i in range(n)]
            for i in range(2,n):
                if isprime[i]:
                    for j in range(i*2,n,i):
                        isprime[j] = False
            count = 0
            for i in range(2,len(isprime)):
                if isprime[i]:
                    count+=1
            return count
        else:
            return 0
        