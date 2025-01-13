import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)

def calculate_future_date():
    number_of_days = int(input('Please enter number of days (integer number): '))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days = number_of_days)
    print(future_date)
