import json

# Initial data
data = {
    'name': 'Victor Ulloa',
    'age': 30,
    'city': 'Denver, CO',
    'interests': ['Traveling', 'Hiking', 'Photography', 'Running', 'Music', 'Working out'],
    'is_student': True   
}

# Write initial data to the file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('You have successfully written to data.json')

# Read the data back from the file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print('Successfully able to read data.json')
print(loaded_data)

# Update the data
loaded_data['age'] = 11
loaded_data['interests'].append("Kayaking")

# Write the updated data back to the file
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)  

print('You have successfully rewritten to data.json')

print(loaded_data)