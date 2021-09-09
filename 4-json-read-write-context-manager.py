  
import json
import os, sys

# read json file
with open(os.path.join(sys.path[0], '4-friends_json.txt'), 'r') as file:
    file_contents = json.load(file)  # reads file and turns it to dictionary

print(file_contents['friends'][0])



# write json file
cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
    {'make': 'Honda', 'model': 'Accord'}
]

with open(os.path.join(sys.path[0], '4-cars-json.txt'), 'w') as file:
    json.dump(cars, file)