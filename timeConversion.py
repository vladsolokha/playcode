'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''

def timeConversion(s):
    get_end = s[-2]
    get_first_hour = s[0]
    get_second_hour = s[1]
    if get_end == 'A' and get_first_hour == '1' and get_second_hour == '2':
        return '00' + s[2:8]
    elif get_end == 'A':
        return s[:8]
    elif get_end == 'P' and get_first_hour == '1' and get_second_hour == '2':
        return s[:8]
    elif get_end == 'P':
        hour_time = int(get_first_hour+get_second_hour)
        hour_time += 12
        return str(hour_time)+s[2:8]

tests = ['07:54:34PM', '10:30:12AM', '12:45:21AM', '12:00:23PM', '10:32:00PM']
def testing_function(tests):
    for test in tests:
        print(timeConversion(test))

testing_function(tests)