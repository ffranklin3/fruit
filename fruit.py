# Initialize fruit list
fruit_list = ['Apples', 'Bananas', 'Carrots', 'Dates']
    
found = False
# Get fruit
fruit = input('Search for a fruit: ')
    
# Check for fruit
for f in fruit_list:
    if f == fruit:
      found = True
      break
if found: 
    print('found!')
else:
    print('No match!')
