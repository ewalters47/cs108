"""
Modules and files
Created Spring 2019
Lab 09
@author: Ethan Walters (emw45)
"""

# Import class from employee module
from employee import Employee

employees = []

# Append employees to the list of employees using line
with open('employees.txt', 'r') as file:
    count = 0
    for line in file:
        employees.append(Employee(line))
        count += 1
    assert len(employees) == count
print(employees)

# Implementing dictionaries with values and keys
if employees == []:
    print('No employees found')
else:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    for employee in employees:
        if employee.get_rank() in totals:
            totals[employee.get_rank()] += employee.get_salary()
            counts[employee.get_rank()] += 1
        else:
            totals[employee.get_rank()] = employee.get_salary()
            counts[employee.get_rank()] = 1

        # Compare salaries for lowest and highest employees
        if employee.get_salary() > max_employee.get_salary():
            max_employee = employee
        elif employee.get_salary() < min_employee.get_salary():
            min_employee = employee


# Compute the average salary and output results to file
def print_averages(total_salaries_per_rank, number_per_rank, file):
    file.write('\nRank\t\t\tAverage Salary\n')
    for rank in totals:
        average = total_salaries_per_rank[rank] / number_per_rank[rank]
        file.write('%s\t\t\t%.2f\n' % (rank, average))

# Write data to a file
with open('employee_stats.txt', 'w') as file:
    file.write(str('The employee with the highest salary is: ' + str(max_employee)))
    file.write(str('\nThe employee with the lowest salary is: ' + str(min_employee)))
    print_averages(totals, counts, file)