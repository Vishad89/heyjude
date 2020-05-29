#!/usr/bin/python3

import json

def get_reports(emp_id):
    with open("eid1.json","r") as read_file:
        data = json.load(read_file)
    return data["reports"]

def get_details(emp_id):
    with open("eid1.json","r") as read_file:
        data = json.load(read_file)
    
    return " - ".join([data["name"], data["title"]])

def print_list(input):
    if input is None or input.empty():
        return None
    return input.values()

def main(start_employee_id):
    output = {}
    running_count = []
    emp_id = start_employee_id
    x = get_reports(emp_id) 
    if x is not None:
        output[emp_id] = x  # x = [123, 456]
        # running_count.push(x)  # runnig_count = [[123,456]] or [123,456]?
        for id in x:
            running_count.append(id)
        emp_id = running_count.pop()
    
    temp = output.keys()
    running_count = []
    x = print_list(temp) 
    if x is not None:
        print(x)
        print("\t")
        for id in x:
            running_count.push(id)
        x = running_count.pop()
        
    for x in output.keys():
        print("\t")
        print(get_details(emp_id))

id = 123
main(id)