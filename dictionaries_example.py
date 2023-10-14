my_dict = {
            'name': 'John', 
            'age': 25, 
            'city': 'New York'
          }

print(my_dict.keys())
# Output: dict_keys(['name', 'age', 'city'])

print(my_dict.values())
# Output: dict_values(['John', 25, 'New York'])

print(my_dict.items())
# Output: dict_items([('name', 'John'), 
# ('age', 25), ('city', 'New York')])

print(my_dict.get('name'))  
# Output: John

my_dict.pop('age')
# Remove the key-value pair with key 'age'

my_dict.update({'country': 'USA'})
# Add or update key-value pairs

my_dict.clear()
# Clear the entire dictionary
