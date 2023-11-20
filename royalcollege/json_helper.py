import json
import csv

# def merge_and_deduplicate(json_files):
#     merged_data = []

#     for json_file in json_files:
#         with open(json_file, 'r', encoding='utf-8') as file:  
#             data = json.load(file)
#             merged_data.extend(data)
#     deduplicated_data = {json.dumps(entry, sort_keys=True) for entry in merged_data}
#     merged_data = [json.loads(entry) for entry in deduplicated_data]

#     return merged_data

# json_files = ['data - Copy.json', 'data.json', 'data1.json']
# merged_data = merge_and_deduplicate(json_files)
# print("Length of merged and deduplicated data:", len(merged_data))
# with open('merged_data.json', 'w', encoding='utf-8') as outfile:  
#     json.dump(merged_data, outfile, indent=4)


with open('data.json', 'r', encoding='utf-8') as outfile:  
    merged_data = json.load(outfile)

csv_file = 'medical_data.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:  
    fieldnames = merged_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in merged_data:
        writer.writerow(item)

print(f"CSV file '{csv_file}' has been created with UTF-8 encoding.")
