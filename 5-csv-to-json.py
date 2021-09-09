import os, sys, json

with open(os.path.join(sys.path[0], "5-csv-file.csv"), "r") as csv_file:
    csv_data =  csv_file.readlines()

headers = csv_data[0].strip().split(',')
print(headers)

club_list = []
for line in csv_data[1:]:
    club_list.append(dict(zip(headers, line.strip().split(','))))

print(club_list)

with open(os.path.join(sys.path[0], "5-json-file.json"), "w") as json_file:
    json.dump(club_list, json_file)
