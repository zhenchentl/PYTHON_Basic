__author__ = 'xiaolin'

def is_leap_year(y):
    if y % 4==0 and y % 400 ==0 or y % 100 != 0:
        return True
    else:
        return False


def get_num_of_days_in_month(y,m):
    if m in (1,3,5,7,8,10,12):
        return 31
    elif m in (4,6,9,11):
        return 30
    elif is_leap_year(y):
        return 29
    else:
        return 28

def get_total_num_of_day(y,m):
    days=0
    for y in range(1800,y):
        if is_leap_year(y):
            days+=366
        else:
            days+=365
    for m in range(1,m):
        days+=get_num_of_days_in_month(y,m)
    return days

def get_start_day(y,m):
    return((9+get_total_num_of_day(y,m)) % 7)


print get_start_day(2015,1)






