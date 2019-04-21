'''
Title: 599. Minimum Index Sum of Two Lists (Easy) https://leetcode.com/problems/minimum-index-sum-of-two-lists/

Runtime: 300 ms, faster than 25.03% of Python online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 12.1 MB, less than 5.13% of Python online submissions for Minimum Index Sum of Two Lists.

Description:
        Suppose Andy and Doris want to choose a restaurant for dinner, 
        and they both have a list of favorite restaurants represented by strings.

        You need to help them find out their common interest with the least list index sum. 
        If there is a choice tie between answers, output all of them with no order requirement. 
        You could assume there always exists an answer.

Example:
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".

    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

'''

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        output = []
        cnt = []
        name = []
        mini = 10000
        for index,i in enumerate(list2):
            if i in list1:
                tmp = index + list1.index(i)
                cnt.append(tmp)
                name.append(i)
                if mini > tmp:
                    mini = tmp
        
        for index,i in enumerate(name):
            if cnt[index] == mini:
                output.append(i)
            
        return output