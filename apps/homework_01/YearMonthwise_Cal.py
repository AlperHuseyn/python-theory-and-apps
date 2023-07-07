import datetime

def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def pryear(year, c=6):
    months = [31, 29 if isleap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(1, len(months) + 1):
        if i in [4, 7, 10]:
            print(end='\n\n')
        # Get the first day of the year's months
        first_day_of_the_year_months = datetime.date(datetime.date.today().year, i, 1)
        
        # Get Get the weekday index of the first day (0 - Monday, 6 - Sunday)
        weekday = first_day_of_the_year_months.weekday()
        
        # Get the number of days in the month 
        num_days = months[i - 1]
        
        # Get the month name
        month_name = first_day_of_the_year_months.strftime('%B')
        
        # Calculate the lenghth of the header line
        day_names = 'Mo Tu We Th Fr Sa Su'
        header_lenght = len(day_names)
        
        # Create the centered header line
        header_line = f'{month_name}'.center(header_lenght)
        
        # print the centered header line
        print(header_line)
        
        # Print the day names
        print(day_names)
        
        # Print leading spaces for the first week
        print('   ' * weekday, end='')
        
        # Iterate over each day in the month
        for day in range(1, num_days + 1):
            # Print the day with leading zero if necessary
            print(f'{day:2d}'.rjust(2) + ' ', end='')
            # Move the cursor to the next line if it's the end of the week
            if (day + weekday) % 7 == 0:
                print()
        # Print a new line after last week
        print(' ' * c)

def main():
    year = int(input('Please enter a year in format "YYYY": '))
    pryear(year)
    
    
if __name__ == '__main__':
    main()
    