import json, os, sys

# reading json file
file = open(os.path.join(sys.path[0], "4-friends_json.txt"), "r")
file_contents = json.loads(file.read()) # reads file and turns it to dictionary

file.close()

print(file_contents['friends'][0])


# writing json file with dictionary
cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('4-cars-json.txt', 'w')
json.dump(cars, file)
file.close()

# json string to a dictionary
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
my_car = json.loads(my_json_string)
print(my_car[0]['name'])