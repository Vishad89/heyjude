"""

https://yumminhuang.github.io/note/sreinterview/

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
import json

report = []

def employee_hierarchy(employee_id):
  
  reports = []
  employee =  requests.get("http://www.linkedin.corp/api/employee/%s"  %employee_id)
  if employee.status == 200:
    print (employee['Name'], "-" , employee['title'])
    reports = json.reads(employee['reports'])
    for report in reports:
      employee_hierarchy(report)
    return 0

employee_hierarchy(employee_id="A12345678")

# class Solutions:

#   #retrieve reports for an employee
#   def get_reports(self, emp_id):
#       id = emp_id
#       url = "http://www.linkedin.corp/api/employee/%s" id
#       result = requests(url).json()
#       if result is None:
#           return 0
#       return result["reports"]

#   #Retrieve name and title of the employee
#   def get_name_title(self, emp_id):
#       self.get_reports(emp_id):
#       id = emp_id
#       url = "http://www.linkedin.corp/api/employee/%s" id
#       result = requests(url)
#       return '-'.join(result["name"],result["title"])

#   def employee_hierarchy(self, emp_id,depth):
#       reports = self.get_reports(emp_id)
#       nt = self.get_name_title(emp_id)
#       tab = depth * " "
#       print(tab,nt)
#       for report in reports:
#           self.employee_hierarchy(report,depth + 1)
  
#   def find_reports(self, emp_id):
#       r = requests.get("URL/" + emp_id).json()
#       if reports not in r.keys():
#           return None 
#       return r["reports"]

#   def employee_hierarchy(self, emp_id):
#       final = {}
#       start_emp_id= emp_id
#       reports = self.find_reports(start_emp_id)
#       while report in reports is not None:
#           final[start_emp_id] = report


# s = solution()
# depth = 0
# emp_id = "A12345678"
# s.employee_hierarchy(emp_id,depth))




    
