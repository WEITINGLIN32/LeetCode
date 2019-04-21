'''
Title: 811. Subdomain Visit Count (Easy) https://leetcode.com/problems/subdomain-visit-count/

Runtime: 44 ms, faster than 100.00% of Python online submissions for Subdomain Visit Count.
Memory Usage: 11.7 MB, less than 5.88% of Python online submissions for Subdomain Visit Count.

Description:
        A website domain like "discuss.leetcode.com" consists of various subdomains. 
        At the top level, we have "com", at the next level, we have "leetcode.com", 
        and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
        we will also visit the parent domains "leetcode.com" and "com" implicitly.

        Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), 
        followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

        We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, 
        (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example:
Input: 
    ["9001 discuss.leetcode.com"]
    Output: 
    ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    Explanation: 
    We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" 
    and "com" will also be visited. So they will all be visited 9001 times.

'''

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        
        for i in range(len(cpdomains)):
            count = int(cpdomains[i][:cpdomains[i].index(' ')])
            domain = cpdomains[i][cpdomains[i].index(' ')+1:]
            dots = cpdomains[i].count('.')
            if dots == 1:
                if cpdomains[i][cpdomains[i].index('.')+1:] in dict:
                    dict[cpdomains[i][cpdomains[i].index('.')+1:]] += count
                else:
                    dict[cpdomains[i][cpdomains[i].index('.')+1:]] = count
                if domain in dict: 
                    dict[domain] += count
                else:
                    dict[domain] = count
            else:
                tmp = domain[domain.index('.')+1:]
                if tmp in dict:
                    dict[tmp] += count
                else:
                    dict[tmp] = count
                
                tmp = tmp[tmp.index('.')+1:]
                if tmp in dict:
                    dict[tmp] += count
                else:
                    dict[tmp] = count
                
                if domain in dict: 
                    dict[domain] += count
                else:
                    dict[domain] = count
            
        output = [str(dict[i]) + ' ' + i for i in dict]
        
        return output
        