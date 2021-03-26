# https://leetcode.com/problems/day-of-the-week/
# 1185. Day of the Week

# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day = datetime.datetime(year, month, day)
        
        return day.strftime("%A")