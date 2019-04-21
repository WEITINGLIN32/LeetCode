'''
Title: 841. Keys and Rooms (Medium) https://leetcode.com/problems/keys-and-rooms/

Runtime: 76 ms, faster than 22.86% of Python online submissions for Keys and Rooms.
Memory Usage: 12.3 MB, less than 5.55% of Python online submissions for Keys and Rooms.

Description:
        There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, 
        and each room may have some keys to access the next room. 

        Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] 
        where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

        Initially, all the rooms start locked (except for room 0). 

        You can walk back and forth between rooms freely.

        Return true if and only if you can enter every room.

Example:
    Input: [[1],[2],[3],[]]
    Output: true
    Explanation:  
    We start in room 0, and pick up key 1.
    We then go to room 1, and pick up key 2.
    We then go to room 2, and pick up key 3.
    We then go to room 3.  Since we were able to go to every room, we return true.

    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.

'''

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = []
        keys.append(0)
        
        
        for j in keys:
            for k in rooms[j]:
                if k not in keys:
                    keys.append(k)
        
        if len(keys) == len(rooms):
            return True
        else:
            return False
        