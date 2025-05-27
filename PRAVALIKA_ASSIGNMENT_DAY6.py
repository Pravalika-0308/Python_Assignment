class Department:
    Department_count=0
    def __init__(self,deptid,deptname,deptloc,hod):
        self.deptid=deptid
        self.deptname=deptname
        self.deptloc=deptloc
        self.hod=hod
        Department.Department_count += 1

    def display_department_info(self):
        print("Enter the Department information: ")
        print("-------------")
        print(f"Department ID : {self.deptid}")
        print(f"Department Name : {self.deptname}")
        print(f"Department location : {self.deptloc}")
        print(f"head of department : {self.hod}")

    @classmethod
    def get_total_departments(cls):
        return cls.Department_count
    

departments = []


no_of_dept = int(input("Enter the number of Departments: "))\


for i in range(no_of_dept):
    print(f"\nEnter details for Department {i+1}")
    dept_id = input("Enter Department ID: ")
    dept_name = input("Enter Department Name: ")
    dept_loc = input("Enter Department Location: ")
    hod = input("Enter Head of Department: ")

    dept = Department(dept_id, dept_name, dept_loc, hod)
    departments.append(dept)


print("Department Details:")
for dept in departments:
    dept.display_department_info()



print(f"Total Departments in Organization: {Department.get_total_departments()}")



search_id = input("\nEnter Department ID to search: ")
found = False
for dept in departments:
    if dept.deptid == search_id:
        print("Department found:")
        dept.display_department_info()
        found = True
        break
if not found:
    print("Department ID not found.")


search_name = input("\nEnter Department Name to search: ")
found = False
for dept in departments:
    if dept.deptname.lower() == search_name.lower():
        print("Department found:")
        dept.display_department_info()
        found = True
        break
if not found:
    print("Department Name not found.")