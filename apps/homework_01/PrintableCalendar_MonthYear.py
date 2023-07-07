# import calendar
import datetime


def prmonth(year, month):
    # Get the first day of the month
    first_day = datetime.date(year, month, 1)
    
    # Get the weekday index of the first day (0 - Monday, 6 - Sunday)
    weekday = first_day.weekday()
    
    # Get the number of days in the month
    def get_month_range(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return ValueError('Invalid month...')
    
    """
    num_days = calendar.monthrange(year, month)[1]
    """
    num_days = get_month_range(year, month)
    
    # Get the month name and year
    month_name = first_day.strftime('%B')
    year_str = str(year)
    
    # Calculate the lenghth of the header line
    day_names = 'Mo Tu We Th Fr Sa Su'
    header_lenght = len(day_names)
    
    # Create the centered header line
    header_line = f'{month_name} {year_str}'.center(header_lenght)
    
    # print the centered header line
    print(header_line)
    
    # Print the day names
    print(day_names)
    
    # Print leading spaces for the first week
    print("   " * weekday, end="")
    
    # Iterate over each day in the month
    for day in range(1, num_days + 1):
        # Print the day with leading zero if necessary
        print(f'{day:2d}'.rjust(2) + ' ', end='')
        # Move the cursor to the next line if it's the end of the week
        if (day + weekday) % 7 == 0:
            print()
    
    # Print a new line after last week
    print()
    
def main():
    prmonth(2018, 8)
    
    
if __name__ == '__main__':
    main()
    