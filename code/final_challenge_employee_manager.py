"""
Final Challenge:
Create a small Python class `EmployeeManager` that:
- Loads employee data from a JSON string  
- Allows adding, updating, and deleting employees  
- Saves the updated data back to a JSON file  

Bonus: Add error handling for missing keys.
"""
import json
import pprint

emp_data = {
    "employees": [
        {"employee_id": "E001", "name": "Alice Johnson", "tech": "Python"},
        {"employee_id": "E002", "name": "Bob Smith", "tech": "JavaScript"},
        {"employee_id": "E003", "name": "Carol White", "tech": "Java"}
    ]
}


class EmployeeManager:
    def __init__(self,name,employee_id,tech):
        data=json.load(emp_data)
        self.name=data["employees"]["name"]
        self.employee_id=data["employees"]["employee_id"]
        self.tech=data["employees"]["tech"]

    def add_employee(self, employee_id, name, tech):
        new_employee = {"employee_id": employee_id, "name": name, "tech": tech}
        self.employees.append(new_employee)

    def update_employee(self, employee_id, **kwargs):
        for emp in self.employees:
            if emp["employee_id"] == employee_id:
                for key, value in kwargs.items():
                    if key in emp:
                        emp[key] = value
                    else:
                        raise KeyError(f"Key '{key}' not found in employee record")
                return
        raise ValueError(f"Employee with ID '{employee_id}' not found")

    def delete_employee(self, employee_id):
        for emp in self.employees:
            if emp["employee_id"] == employee_id:
                self.employees.remove(emp)
                return
        raise ValueError(f"Employee with ID '{employee_id}' not found")

    def save_to_file(self, filepath):
        with open(filepath, "w") as f:
            json.dump({"employees": self.employees}, f, indent=4)
def __init__(self, json_string):
        try:
            data = json.loads(json_string)
            self.employees = data["employees"]
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Invalid employee data: {e}")
        