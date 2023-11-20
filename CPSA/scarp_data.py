import requests
from bs4 import BeautifulSoup
from helper_class import *
from interface_class import *
from database_interface import *
from proxy_interface import *

class CPSA():
    def __init__(self):
        self.all_data= []
        self.helper = Helper()
        self.details = []
        with open('listings.json', 'r') as input:
            self.urls = json.load(input)
        
        with open('done.json', 'r') as done:
            self.done = json.load(done)

    def get_data(self,url):
        if url not in self.done:
            scraped_data = {
                "Url": "",
                "Name": "",
                "Preferred Name": "",
                "Registration Number": "",
                "Languages": "",
                "Gender": "",
                "Location": "",
                "Number": "",
                "Extra Deatils": [],
                "Practice Disciplines": "",
                "Specialties": "",
                "Membership Status": "",
                "Conditions on Practice Permit": "",
                "Qualifications": [],
                "CPSA Approvals": "",
                "Upcoming Hearings": "",
                "Disciplinary Actions": "",
                "regHistory": []
            }

            response = requests.get(url)
            print(url)
            soup = BeautifulSoup(response.content,'lxml')
            scraped_data['Url'] = url

            table_head = soup.find('div',{'class':'tabHeader'}).find('h2')
            color_tag = table_head.find('span', {'style': 'color: Red'})
            color_tag.decompose()
            prefName = table_head.find('span', {'class': 'prefName'})
            scraped_data['Preferred Name'] = self.helper.get_text_from_tag(prefName).replace('(Preferred Name:','').replace(')','').strip()
            prefName.decompose()
            scraped_data['Name'] = self.helper.get_text_from_tag(table_head)

            table_container = soup.find('div', {'class': 'tabContentWrapper'})
            all_table = table_container.find_all('div', {'class': 'tabContent'})

            for table in all_table:
                rows = table.find_all('div', {'class': 'row'})

                for row in rows:
                    regHistory = row.find('table', {'class': 'regHistory'})
                    map_canvas = row.find('div', {'id': 'map-canvas'})
                    if regHistory:
                        data_list = []
                        headers = [header.text.strip() for header in regHistory.find_all('tr')[0].find_all('th')]
                        for r in regHistory.find_all('tr')[1:]:
                            columns = r.find_all('td')
                            values = [column.text.strip() for column in columns]
                            date_parts = [part.strip() for part in columns[0].text.strip().split('\n\n') if part.strip()]
                            date_range = date_parts[0].strip().replace('\n', ' ')
                            end_date = date_parts[1].strip().replace('\n', ' ')
                            entry = {
                                'Start Date': date_range,
                                'End Date': end_date,
                                headers[1]: values[1],
                                headers[2]: values[2]
                            }
                            data_list.append(entry)
                        scraped_data['regHistory'] = data_list

                    elif map_canvas:
                        scraped_data['Number'] = self.helper.get_url_from_tag(row.find('a', class_='phInfo')).replace('tel:', '')
                        if (row.find('a', class_='phInfo')):
                            (row.find('a', class_='phInfo')).decompose()
                        address_lines = [line.strip() for line in row.find('div', class_='addressFormat').get_text().splitlines() if line.strip()]
                        scraped_data['Location'] = '\n'.join(address_lines).replace('\n', ' ')
                        scraped_data['Extra Deatils'] = [self.helper.get_text_from_tag(item) for item in row.find_all('p', class_='profileIco')]

                    else:
                        header = row.find('h3').text.strip()
                        if 'Location' in header:
                            continue
                        if 'CPSA Approvals?' in header:
                            row.find('div', {'aria-hidden': 'true'}).decompose()
                            header = header.replace('?', '')
                        if 'Qualifications' in header:
                            qualifications_list = [qualification.strip() for qualification in row.find('p').stripped_strings]
                            qualifications_list = [q for q in qualifications_list if q]
                            scraped_data['Qualifications'] = qualifications_list
                        else:
                            data = row.find('p').text.strip()
                            scraped_data[header] = data
            self.details.append(scraped_data)
            self.done.append(url)
            print(len(self.details))
            with open('Output.json', 'w', encoding='utf-8') as outfile:
                json.dump(self.details, outfile, indent=4)
            with open('done.json', 'w', encoding='utf-8') as outfile1:
                json.dump(self.done, outfile1, indent=4)


    def run_multiThread(self,function,max_workers,args):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(function, args)

    def main(self):
        self.run_multiThread(self.get_data, 20, self.urls)

if __name__ == "__main__":
    CPSA().main()