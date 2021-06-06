"""
This is the solution program for the proposed exercise by ioet Ecuador S.A.
Summary: 
The program takes as input a .txt file containing the data from the employee's working schedule.
The program outputs a message in the console, indicating the amount to be paid for each individual employee.
All of the calculations are based on the day of the week and time of day, according to the table provided.
This program uses the datetime module to express and operate the hours worked.

Created by: Santiago Andrade.
Date: 05-June-2021.
"""

from datetime import datetime
FILE = 'example.txt'

def convert_dates(file_data):
    """
    This function converts a string into a dictionary of dictionaries, where the main key is
    the name of the employee, and the value is another dictionary.

    Args:
        file_data (str): data read from a .txt file

    Returns:
        dictionary: contains another dictionary whose keys are the codes for the days of the week,
        and the values are lists of strings, corresponding to the hours worked.
        {NAME: {MO: ["10:00", "12:00"]}}
    """

    split_data = file_data.split('\n')
    
    # Create a dictionary with "names" as keys
    employees = {}
    for line in split_data:
        split_line = line.split("=", 1)
        employees[split_line[0]] = split_line[1].split(",")

    # Reassign the content of the dictionary to a second dictionary (schedule)
    for name, data in employees.items():
        day = list(map(lambda x: x[0:2], data))
        hours = list(map(lambda x: x[2:].split("-"), data))
        schedule = dict(zip(day, hours))
        employees[name] = schedule

    return employees
    
def check_hours(hour_list, pay_list):
    """
    This function calculates the total amount of hours worked and
    multiplies them by the proper hour rate, based on the table provided.

    Args:
        hour_list (list): list of two strings (starting-hour & ending-hour)
        pay_list (list): list of three integers (hour rates)

    Returns:
        int: total amount to be paid to the employee
    """
    
    # fixed time ranges (datetime objects)
    hour_0 = datetime(1900,1,1,0,0)
    hour_9 = datetime(1900,1,1,9,0)
    hour_18 = datetime(1900,1,1,18,0)
    hour_24 = datetime(1900,1,2,0,0)    # next day
    
    # validation check
    # assign the input hours (str) into datetime (obj)
    try:
        format_time = "%H:%M"
        hour_s = datetime.strptime(hour_list[0], format_time)
        hour_e = datetime.strptime(hour_list[1], format_time)
    except ValueError:
        print("There is an error with the input data. Wrong format!")
        return 0

    # if the ending hour is 00:00, it reasigns it to the next day
    if hour_e == hour_0:
        hour_e = hour_24
    
    # calculate the total amount to pay from the hours ranges
    if hour_s < hour_e:
        difference = (hour_e - hour_s).seconds//3600
        if (hour_s > hour_18) and (hour_e <= hour_24):
            return (difference*pay_list[2])
        elif hour_s > hour_9:
            if hour_e <= hour_18:
                return (difference*pay_list[1])
            elif hour_e > hour_18:
                difference_1 = (hour_e - hour_18).seconds//3600
                difference_2 = (hour_18 - hour_s).seconds//3600
                return (difference_1*pay_list[2] + difference_2*pay_list[1])
        else:
            if hour_e <= hour_9:
                return (difference*pay_list[0])
            elif hour_e <= hour_18:
                difference_1 = (hour_e - hour_9).seconds//3600
                difference_2 = (hour_9 - hour_s).seconds//3600
                return (difference_1*pay_list[1] + difference_2*pay_list[0])
            else:
                difference_1 = (hour_e - hour_18).seconds//3600
                difference_2 = (hour_18 - hour_9).seconds//3600
                difference_3 = (hour_9 - hour_s).seconds//3600
                return (difference_1*pay_list[2] + difference_2*pay_list[1] + difference_3*pay_list[0])
    else: 
        # indicates an error in the input data
        return 0       

def amount_to_pay(employees):
    """
    This function prints out the final message in the console.


    Args:
        employees (dictionary): dictionary of dictionaries (generated by the 
        first function).
    """
    
    # Day abbreviations
    week_days = ["MO", "TU", "WE", "TH", "FR"]
    week_ends = ["SA", "SU"]
    # Hour rates
    week_days_pay = [25, 15, 20]
    week_ends_pay = [30, 20, 25]
    
    # Check for day in abbreviations list, calls the function check_hours() 
    # to determine the proper amount to be paid.
    amount = 0
    for name, worked_days in employees.items():
        for day, hours in worked_days.items():
            if day in week_days:
                if check_hours(hours, week_days_pay) == 0:
                    print("There is an error in {}'s schedule, on day: {}.".format(name, day))
                amount += check_hours(hours, week_days_pay)
            elif day in week_ends:
                if check_hours(hours, week_ends_pay) == 0:
                    print("There is an error in {}'s schedule, on day: {}.".format(name, day))
                amount += check_hours(hours, week_ends_pay)
            else:
                # Day was not in abbreviations list
                print("Wrong day code: {}.".format(day))
        print('The amount to pay {} is: {} USD \n'.format(name, amount))
        amount = 0

    
def read_file(filename):
    """
    This function reads a .txt file. Then calls the corresponding functions to print the final 
    message in the console.

    Args:
        filename (file (.txt)): file containing the information about each employee and their 
        worked hours (str).
    """

    with open(filename, 'r') as file:
        data = file.read()

    # Dictionary of dictionaries
    employees = convert_dates(data)
    # Print the amount to pay in the console
    amount_to_pay(employees)


read_file(FILE)