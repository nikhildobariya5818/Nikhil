import csv
import json

with open('Output.json','r',encoding='utf-8') as json_file:
    data = json.load(json_file)

rows = []
for entry in data:
    languages = entry.get("Languages", "")
    specialties = entry.get("Specialties", "")
    practice_disciplines = entry.get("Practice Disciplines", "")
    registration_number = entry.get("Registration Number", "")
    gender = entry.get("Gender", "")
    location = entry.get("Location", "")
    contact_number = entry.get("Number", "")

    qualifications = ", ".join(entry.get("Qualifications", []))
    conditions_on_practice_permit = entry.get(
        "Conditions on Practice Permit", "")

    reg_history = entry.get("regHistory", [])

    start_dates = []
    end_dates = []
    Type = []
    Explanation = []
    for history_entry in reg_history:
        start_dates.append(history_entry.get("Start Date", ""))
        end_dates.append(history_entry.get("End Date", ""))
        Type.append(history_entry.get("Type", ""))
        Explanation.append(history_entry.get("Explanation for Change", ""))

    # Append the extracted data to the rows list
    rows.append([
        entry["Url"], entry["Name"], entry["Preferred Name"], registration_number, languages, gender,
        location, contact_number, ", ".join(entry.get(
            "Extra Deatils", [])), practice_disciplines, specialties, entry['Membership Status'],
        conditions_on_practice_permit, qualifications, entry['CPSA Approvals'], entry['Upcoming Hearings'], entry['Disciplinary Actions'], ", ".join(
            start_dates), ", ".join(end_dates), ", ".join(Type), ", ".join(Explanation)
    ])

csv_file_path = 'Final_Output.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    header = ["Url", "Name", "Preferred Name", "Registration Number", "Languages",
              "Gender", "Location", "Contact Number", "Extra Deatils", "Practice Disciplines", "Specialties", "Membership Status",
              "Conditions on Practice Permit", "Qualifications", "CPSA Approvals", "Upcoming Hearings", "Disciplinary Actions", "Start Dates", "End Dates", "Type", "Explanation for Change"]
    csv_writer.writerow(header)

    csv_writer.writerows(rows)

print(f"CSV file '{csv_file_path}' created successfully.")
