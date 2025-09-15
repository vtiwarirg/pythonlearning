def is_leap_year(year):
    """
    Determines if a given year is a leap year according to the Gregorian calendar rules.
    
    A leap year occurs:
    - Every year that is divisible by 4 with no remainder
    - EXCEPT every year that is evenly divisible by 100 with no remainder
    - UNLESS the year is also divisible by 400 with no remainder
    
    Args:
        year (int): The year to check (must be a positive integer)
        
    Returns:
        bool: True if the year is a leap year, False otherwise
        
    Examples:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2023)
        False
    
    Note:
        Leap years have 366 days instead of 365, with February having 29 days.
        This system helps keep our calendar year synchronized with the solar year.
    """    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2024))

