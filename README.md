# **Programming-Exercise-ioet**
This is the programming exercise solicited by ioet Ecuador S.A. as part of their candidate selection process.

<br />

***Exercise***:

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:


| Hour range | Monday to Friday | Saturday and Sunday |
| :---: | :---: | :---: |
| 00:01 - 09:00 | 25 USD | 30 USD |
| 09:01 - 18:00 | 15 USD | 20 USD |
| 18:01 - 00:00 | 20 USD | 25 USD |

<br />

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

| Code | Day |
| :---: | :---: |
| MO | Monday |
| TU | Tuesday |
| WE | Wednesday |
| TH | Thursday |
| FR | Friday |
| SA | Saturday |
| SU | Sunday |

<br />

***Input:*** the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

***Output:*** indicate how much the employee has to be paid.


*For example:*

| INPUT | OUTPUT |
| --- | --- |
| RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 | `The amount to pay RENE is: 215 USD` |
| ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 | `The amount to pay ASTRID is: 85 USD`

<br />

## Solution Overview

The programming language chosen to solve this exercise is `Python`.

It makes use of the `datetime` module, and has four functions defined:

* `convert_dates()`
* `check_hours()`
* `amount_to_pay()`
* `read_file()`

As input data comes from a `.txt` file, the global variable `FILE` is declared at the top of the program to ease the process of changing the name and/or path of the file. 

It is worth mentioning that, due to the simple nature of this exercise, I did not declare any classes for the employees or the schedules. However, if this program would require the addition of any functionality, or if there was any additional complexity associated with it, I would have opted for an OOP (Object Oriented Programming) approach. Perhaps the declaration of a `class Employee` would facilitate the maintenance and scalability of the program, as it would facilitate the inclusion of possible changes or additional features.

<br />

## Architecture

This program has a *Monolithic application* architecture, as it is self-contained and independent. This program performs every step needed to complete the whole task by itself, and has no modularity defined to delegate functions to other programs.

As mentioned in the previous section, the simplicity of this exercise did not require a more sophisticated approach, like *Microservices* delegation or a *Database* integration.

<br />

## Aproach and Methodology

The approach I took to complete this task was quite simple, yet effective.

First of all, I made a graph with all of the combinations possible for different hour ranges, as this was the main problem to solve in order to calculate the final payment for each employee.

Secondly, I defined the number of functions that were going to be needed to complete the task, taking into account that I wanted the program to be easy to read and easy to understand. This led me to define four functions, which will be explained below.

Finally, I wrote adecuate docstrings and comments throughout the program to explain its functionallity and to make it understandable not only for me, but for any other programmer. I find this to be very helpful when trying to work with large teams and different people.

Let's take a look into every function defined:

1. `convert_dates()`: This function recieves the data read from a `.txt` file as a single string. It then splits the data into different lines and creates a dictionary whose keys are the names of the employees and whose values are another dictionaries. These dictionaries have the codes for the days of the week as keys, and a list of strings (ranges of hours worked) as values.
2. `check_hours()`: This function recieves as arguments two lists, one of the hours worked and another of the payment ranges. With this information the function determines the total of hours worked per day and calculates the proper amount to be paid in US dollars.
3. `amount_to_pay()`: This function recieves a dictionary (returned by `convert_dates()`) as argument. The function checks for the days worked and then calls `check_hours()` to calculate the hours per day. If there are problems with the input data, it displays a message in the console, indicating where was the problem found. Finally, it prints the payment message into the console.
4. `read_file()`: This last function simply reads the `.txt` file and calls the other functions in order to solve the problem. 

<br />

## Instructions - How to run the program locally

As stated above, this program is written in `Python` so it is necessary to install Python 3 in your computer to run it.

You can simply clone this repository or download the files as a `.zip` folder into your machine. Then you need to open the console within the local directory and run de following command:

`python solution.py`

*Note:* If you have installed both `Python2` and `Python3`, then you need to run the command: `python3 solution.py`.

This should run the program and display the output in the same console.

*Note:* As Python is an *interpeted* and not a *compiled* language, you do not need to compile the program in order to run it.