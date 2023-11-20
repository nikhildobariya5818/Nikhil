import csv
import json

all_data =[]

with open ('data.json','r') as json_file:
    data = json.load(json_file)
    for i in data:
        if i['Company Units'] == 'N/A':
            i['Company Units'] = '0'
        all_data.append(i)
csv_file = "franchisegrade_data.csv"
csv_header = all_data[0].keys()
with open(csv_file, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_header)
    writer.writeheader()
    for row in all_data:
        writer.writerow(row)

print(f"CSV file '{csv_file}' has been created.")
