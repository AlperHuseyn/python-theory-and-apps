import datetime


def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def pryear(year, c=6):
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    grouped_month_names = [month_names[i:i+3] for i in range(0, len(month_names), 3)]

    month_ranges = [
            31, 29 if isleap(year) else 28, 31,
            30, 31, 30, 31, 31, 30, 31, 30, 31
    ]

    grouped_month_ranges = [month_ranges[i:i+3] for i in range(0, len(month_ranges), 3)]

    day_names = 'Mo Tu We Th Fr Sa Su'
    
    print('#' * (60 + 2 * c))
    print(f'{year}'.center(60 + 2 * c))
    print('#' * (60 + 2 * c))

    for i, month_groups in enumerate(grouped_month_names):
        print((' ' * c).join(month.center(20) for month in month_groups))
        print(day_names.ljust(20 + c) * 3)
        calendar_months = []
        for j, month in enumerate(month_groups, start=1):
            # Get the first day of the year's months
            first_day_of_the_year_months = datetime.date(datetime.date.today().year, j, 1)
            # Get Get the weekday index of the first day (0 - Monday, 6 - Sunday)
            weekday = first_day_of_the_year_months.weekday()
            # Get the number of days in the month
            num_days = grouped_month_ranges[i][j - 1]
            # Print leading spaces for the first week
            month_string = ' ' * 3 * weekday
            for day in range(1, num_days + 1):
                # Print the day with leading zero if necessary
                month_string += f'{day:2d}'.rjust(2) + ' '
                # Move the cursor to the next line if it's the end of the week
                if (day + weekday) % 7 == 0:
                    month_string += '\n'

            calendar_months.append(month_string)
        print(*calendar_months)
    print('#' * (60 + 2 * c))      
        
def main():
    year = int(input('Please enter a year in format "YYYY": '))
    pryear(year)


if __name__ == '__main__':
    main()
