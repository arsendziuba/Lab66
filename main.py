import time
import datetime

# Set clock count for checking script execution time
start_time = time.time()

# Print current time in the specified format
current_time = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
print("Current Time:", current_time)

# Print the current year
current_year = datetime.datetime.now().year
print("Current Year:", current_year)

# Print the day of the year from the beginning
current_day_of_year = datetime.datetime.now().timetuple().tm_yday
print("Day of the Year:", current_day_of_year)

# Use time tuple conversion into string
custom_time_str = time.strftime('%d %b %Y %H:%M', time.strptime('24 Mar 2015 12:14', '%d %b %Y %H:%M'))
print("Custom Time String:", custom_time_str)

# Use time conversion from string into time tuple
custom_time_tuple = time.strptime('19 Sep. 2012 10:15', '%d %b. %Y %H:%M')
print("Custom Time Tuple:", custom_time_tuple)

# Create a datetime tuple with the current day minus one day
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
print("Yesterday:", yesterday)

# Check the difference with datetime delta
difference = datetime.datetime.now() - yesterday
print("Difference:", difference)

# Print script execution time
end_time = time.time()
execution_time = end_time - start_time
print("Script Execution Time (seconds):", execution_time)
