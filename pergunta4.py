# Question 4
# Employee Benefits Calculation
# --------------------------------------------
# Task:
# Write a function that calculates how much an employee
# is entitled to receive from two benefits upon resignation:
# 1. Paid Vacation (proportional to months worked in the acquisition period)
# 2. Thirteenth Salary (proportional to months worked in the current year)
#
# Rules:
# - Vacation resets every work anniversary (12 months = 30 days).
# - The 13th salary resets every new year.
# - Both are calculated proportionally to the months worked.
#
# Author: Esther Mattos 

def calculate_employee_benefits(salary, months_current_year, months_vacation_period):
    vacation = (salary / 12) * months_vacation_period
    thirteenth_salary = (salary / 12) * months_current_year
    return vacation, thirteenth_salary

salary = 3000

# Example 1: Worked 8 months in vacation period, 5 months in current year
vacation, thirteenth = calculate_employee_benefits(salary, 5, 8)
print(f"Salary: {salary}, Vacation: {vacation}, 13th: {thirteenth}, Total: {vacation + thirteenth}")
# Expected → Vacation = 2000, 13th = 1250, Total = 3250

# Example 2: Worked full year (12 months each)
vacation, thirteenth = calculate_employee_benefits(salary, 12, 12)
print(f"Salary: {salary}, Vacation: {vacation}, 13th: {thirteenth}, Total: {vacation + thirteenth}")
# Expected → Vacation = 3000, 13th = 3000, Total = 6000

# Example 3: Worked 3 months in vacation period, 10 months in current year
vacation, thirteenth = calculate_employee_benefits(salary, 10, 3)
print(f"Salary: {salary}, Vacation: {vacation}, 13th: {thirteenth}, Total: {vacation + thirteenth}")
# Expected → Vacation = 750, 13th = 2500, Total = 3250
