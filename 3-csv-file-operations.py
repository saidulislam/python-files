import os, sys

with open(os.path.join(sys.path[0], "3-iris.csv"), "r") as iris_file:
    iris_data =  iris_file.readlines()

irises = []

# skip the first row. first row has column titles
for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(',')

    # create a dictionary from each row
    irises.append({
		"sepal_length": sepal_length,
		"sepal_width": sepal_width,
		"petal_length": petal_length,
		"petal_width": petal_width,
		"species": species
	})

print(irises)
print()
print()

# let's match each header item to an value in a given row using zip
with open(os.path.join(sys.path[0], "3-iris.csv"), "r") as iris_file:
    iris_data =  iris_file.readlines()

headers = iris_data[0].strip().split(",")
print(headers)
print()
print()

irises = []

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers, iris))
    irises.append(irises)

print(irises)