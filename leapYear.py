#returns true if input is a leap year, returns false otherwise
def is_leap_year(year):
    if(year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False