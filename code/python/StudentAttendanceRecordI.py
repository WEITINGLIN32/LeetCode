'''
Title: 551. Student Attendance Record I (Easy) https://leetcode.com/problems/student-attendance-record-i/

Runtime: 20 ms, faster than 88.13% of Python online submissions for Student Attendance Record I.
Memory Usage: 11.8 MB, less than 6.52% of Python online submissions for Student Attendance Record I.

Description:
        You are given a string representing an attendance record for a student. The record only contains the following three characters:
        'A' : Absent.
        'L' : Late.
        'P' : Present.
        A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) 
        or more than two continuous 'L' (late).

        You need to return whether the student could be rewarded according to his attendance record.

Example:
    Input: "PPALLP"
    Output: True

    Input: "PPALLL"
    Output: False

'''

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt_A = 0
        cnt_L = 0
        init = s[0]
        if init == 'A':
            cnt_A += 1
        elif init == 'L':
            cnt_L = 1
            
        for i in range(1,len(s)):
            if s[i] == 'A':
                cnt_A += 1
                if cnt_A == 2:
                    return False
                cnt_L = 0
            elif s[i] == 'P':
                cnt_L = 0
            elif s[i] == 'L':
                if cnt_L == 1:
                    cnt_L += 1
                elif cnt_L == 0:
                    cnt_L += 1
                elif cnt_L == 2:
                    cnt_L += 1
                    return False

        return True