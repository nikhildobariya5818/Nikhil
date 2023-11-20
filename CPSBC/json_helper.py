import csv
import json

with open('data.json','r',encoding='utf-8') as json_file:
    data = json.load(json_file)

rows = []
for entry in data:
    languages = ', '.join(entry.get("Languages", []))
    certification = ', '.join(entry.get("Certification", []))

    # Extract details
    details_list = entry.get("details", [])
    addresses = ', '.join([detail.get("Addresses", "")
                          for detail in details_list])
    contact_numbers = ', '.join(
        [detail.get("Contact Numbers", "") for detail in details_list])
    fax = ', '.join([detail.get("Fax Number", "") for detail in details_list])


    rows.append([entry["Link"], entry["Title"],entry["MSP number"], entry["Gender"], languages, entry["Registration Status"],
                 entry["Registration Class"], entry["Practice Type"], certification, entry["Degree"],
                 entry["Year"], entry["University"], addresses, contact_numbers, fax])

csv_file_path = 'Final_Output.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    header = ["Link", "Title", "MSP number", "Gender", "Languages", "Registration Status", "Registration Class",
              "Practice Type", "Certification", "Degree", "Year", "University", "Addresses", "Contact Numbers", "Fax Number"]
    csv_writer.writerow(header)

    csv_writer.writerows(rows)

print(f"CSV file '{csv_file_path}' created successfully.")
