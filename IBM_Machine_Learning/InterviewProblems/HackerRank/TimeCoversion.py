"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
Return '12:01:00'.
Return '00:01:00'.
Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):
string s: a time in  hour format
Returns
string: the time in  hour format
"""


def timeConversion(s):
    # Write your code here
    hour = s[:-2]
    hour_suffix = s[-2:]
    if hour_suffix == "AM":
        if s[:2] == "12":
            new_hour = "00" + s[2:-2]
        else:
            new_hour = s[:-2]
    else:
        if s[:2] == "12":
            new_hour = s[:-2]
        else:
            new_hour = str(int(s[:2]) + 12) + s[2:-2]
    return new_hour
