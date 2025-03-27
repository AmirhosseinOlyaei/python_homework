#!/usr/bin/env python3
import csv
import os
from datetime import datetime
import custom_module

# Task 2: Read a CSV File
def read_employees():
    employees_dict = {}
    rows = []
    
    try:
        with open('../csv/employees.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)
            employees_dict["rows"] = rows
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        exit(1)
    
    return employees_dict

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

sorted_rows = sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    result = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[i]
    return result

print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)
    return result

print(all_employees_dict())

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("my new secret")
print(custom_module.secret)

# Helper function for Task 12
def read_csv_to_dict(filename):
    result_dict = {}
    rows = []
    
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    result_dict["fields"] = row
                else:
                    rows.append(tuple(row))
            result_dict["rows"] = rows
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        exit(1)
    
    return result_dict

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = read_csv_to_dict('../csv/minutes1.csv')
    minutes2 = read_csv_to_dict('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    minutes_set = set(minutes1["rows"]).union(set(minutes2["rows"]))
    return minutes_set

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    converted_minutes = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minutes))
    
    try:
        with open('./minutes.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(minutes1["fields"])
            writer.writerows(converted_minutes)
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        exit(1)
    
    return converted_minutes

sorted_minutes = write_sorted_list()
print(sorted_minutes)
