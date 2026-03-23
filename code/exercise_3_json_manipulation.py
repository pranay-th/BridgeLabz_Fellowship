"""
Exercise 3:
Using the above JSON:
1. Add a new skill to the `skills` list.  
2. Update the city name.  
3. Convert it back to a JSON string using `json.dumps()`.  
4. Pretty print the updated JSON.
"""

# Write your code here
import json

# Example JSON string
json_data = '''
{
  "employee": {
    "name": "John",
    "age": 30,
    "skills": ["Python", "ML", "SQL"],
    "address": {"city": "Mumbai", "zip": 400001}
  }
}
'''

# Parse JSON to Python dict
data = json.loads(json_data)

data["employee"]["address"]["city"]="Pune"
data["employee"]["skills"].append("OOPS")
json_data1 = json.dumps(data)
import pprint
pprint.pprint(data)
