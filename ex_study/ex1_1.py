#A program to determine whether the specified year is leap year

#%% 1
year = int(input("Enter the year "))
leap_year= year //  400 == 0 or year // 4 == 0 and year  // 100 != 0
print(year, 'is leap: ', leap_year )

#%% 2
year = int(input("Enter the year "))
leap_year= (year %  400 == 0)  or (year % 4 == 0) and (year  % 100 != 0)
print( f"{year} is leap: {leap_year}" )

