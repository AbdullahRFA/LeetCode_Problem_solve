'''
1185. Day of the Week
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:  
Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"
Constraints:
The given dates are valid dates between the years 1971 and 2100.

Solution: Simulation
1. We can calculate the total number of days from a reference date (e.g., January 1, 1971) to the given date.
2. We can then use the total    number of days to determine the day of the week by taking the modulus with 7 (since there are 7 days in a week).
3. We need to account for leap years when calculating the total number of days, as they add an extra day to the month of February.
4. Finally, we can map the resulting index to the corresponding day of the week and return it.  

'''

class Solution:
    def isLeap(self, year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        days_of_week = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]

        days_in_month = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        total_days = 0

        for y in range(1971, year):
            total_days += 366 if self.isLeap(y) else 365

        for m in range(1, month):
            total_days += days_in_month[m - 1]
            if m == 2 and self.isLeap(year):
                total_days += 1

        total_days += day

        return days_of_week[((total_days + 4) % 7)-1]