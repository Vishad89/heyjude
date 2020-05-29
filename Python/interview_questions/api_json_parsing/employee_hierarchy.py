"""
Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information The employee information endpoint is "/employee/<id>" Each employee record you retrieve will be a JSON object with the following keys:
   - 'name'  refers to a String that contains the employee's first and last name
   - 'title' refers to a String that contains the employee's job title
   - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports

i.e. 
# Sample JSON
# # GET /employee/A123456789
# {
#  "name": "Flynn Mackie",
#  "title": "Senior VP of Engineering",
#  "reports": ["A123456793", "A1234567898"]
# }


Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. If you provide 'A123456789' as input to your function, you will see the sample output below.
 
-----------Begin Sample Output--------------
Flynn Mackie - Senior VP of Engineering
  Wesley Thomas - VP of Design
    Randall Cosmo - Director of Design
      Brenda Plager - Senior Designer
  Nina Chiswick - VP of Engineering
    Tommy Quinn - Director of Engineering
      Jake Farmer - Frontend Manager
        Liam Freeman - Junior Software Engineer
      Sheila Dunbar - Backend Manager
        Peter Young - Senior Code Cowboy
-----------End Sample Output--------------
"""
import requests

def employee_hierarchy(emp_id,depth):
    reports = []
    url = "http://www.linkedin.corp/api/employee/"
    result = requests(url + emp_id).json()
    
    reports = results["reports"]
    nt = '-'.join(result["name"],result["title"])
    t = depth * " "
    print(t,nt)
    depth += 1
    if reports is None:
        return 0
    for report in reports:
        employee_hierarchy(report,depth)


d = 0
eid = "A123242234"
employee_hierarchy(eid,int(d))

    






def find_reports(emp_id):
    r = requests.get("URL/" + emp_id).json()
    if reports not in r.keys():
        return None 
    return r["reports"]




def employee_hierarchy(emp_id):
    final = {}
    start_emp_id= emp_id
    reports = find_reports(start_emp_id)
    while report in reports is not None:
        final[start_emp_id] = report





    
