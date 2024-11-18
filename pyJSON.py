# Import the JSON module, which allows us to write, read, and manipulate JSON data.
import json

# Initial data
data = {
    'name': 'Victor Ulloa',
    'age': 30,
    'city': 'Denver, CO',
    'interests': ['Traveling', 'Hiking', 'Photography', 'Running', 'Music', 'Working out'],
    'is_student': True   
}

# Write the initial data to the file.
# As per the documentation, using "with open" ensures the file is properly closed after the operation. 
# The open() function is used to open a file, taking two parameters:
# File path ('data.json') and mode ('w'), and it is stored in the variable 'json_file'.
with open('data.json', 'w') as json_file:
    # json.dump converts the Python dictionary 'data' into a JSON string
    # and writes the JSON string into 'json_file'.
    json.dump(data, json_file, indent=4)
# After this block, the file is automatically closed since we are using 'with open'.

# Confirm that the data has been written to the file.
print('You have successfully written to data.json')

# Open the file in read mode ('r') to visualize and access its content.
with open('data.json', 'r') as json_file:
    # Convert the JSON file back into a Python dictionary and store it 
    # in a variable named 'loaded_data'.
    loaded_data = json.load(json_file)

# Confirm that the data was successfully read.
print('Successfully able to read data.json')
# Print 'loaded_data' to the console.
print(loaded_data)

# Update the data using bracket notation, successfully changing the value of 'age' from 30 to 11.
loaded_data['age'] = 11
# Append a new interest to the list of interests.
loaded_data['interests'].append("Kayaking")

# Write the updated data back to the file.
with open('data.json', 'w') as json_file:
    # Convert 'loaded_data' into a JSON string and write it back into the file.
    json.dump(loaded_data, json_file, indent=4)  

# Confirm the data has been rewritten.
print('You have successfully rewritten to data.json')

# Display the updated data in the console to verify the changes.
print(loaded_data)