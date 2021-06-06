# **Programming-Exercise-ioet**
This is the programming exercise solicited by ioet Ecuador S.A. as part of the selection process.

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

* ***Input:*** the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

* ***Output:*** indicate how much the employee has to be paid.
   
<br />

*For example:*

| INPUT | OUTPUT |
| --- | --- |
| RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 | `The amount to pay RENE is: 215 USD` |
| ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 | `The amount to pay ASTRID is: 85 USD`

<br />

---
## Solution Overview

The programming language used for solving this exercise is `Python`.

It makes use of the `datetime` module, and has four functions defined:

* `convert_dates()`
* `check_hours()`
* `amount_to_pay()`
* `read_file()`

The input data comes from a `.txt` file, which is read by the program. In order to read the file, the global variable `FILE` is declared at the top of the program. 

Additionally, the program calculates the proper amount to be paid for each employee and prints it to the console.

<br />

---
## Architecture

This program has a *Monolithic application* architecture, as it is self-contained and independent. This program performs every step needed to complete the whole task by it self, and has no modularity defined to delegate functions to other programs.

<br />

---
## Aproach and Methodology



<br />

---
## Instructions - How to run the program locally