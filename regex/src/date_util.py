import re

def init_month_dict():
    dic = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }
    for i in range(1,12):
        dic[str(i)] = i
    return dic

dic = init_month_dict()

def date_match(input_text):
    pattern = r'(?P<year>[1-9][0-9]{0,3})/(?P<month>[A-Z][a-z]*)/(?P<day>[1-9](|[0-9]))'
    mc = re.fullmatch(pattern, input_text)
    if mc is None:
        raise ValueError("Input text must be in format YYYY/MM/dd")

    year = mc.group('year')
    month = mc.group('month')
    day = mc.group('day')

    if not year.isdigit():
        raise ValueError("Year must be a valid number with not leading 0.")

    if not month in dic:
        raise ValueError("Month must be a valid string or number.")
    
    if not day.isdigit():
        raise ValueError("Day must be a valid number with not leading 0.")
    
    return (int(year), int(dic[month]), int(day))
