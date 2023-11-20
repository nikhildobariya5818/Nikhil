import requests
from bs4 import BeautifulSoup
from helper_class import *
from database_interface import *
from proxy_interface import *
from interface_class import *
import math


class CPSBC():
    def __init__(self):
        self.helper = Helper()
        self.listing = []
        self.all_data = []
        self.lastpage = 0
        self.cookies = {
            '_pk_id.1.3ae9': 'a9494f833e61216b.1695710517.',
            '_hjSessionUser_283045': 'eyJpZCI6ImM0NjQ0N2JmLTQwZTMtNTFmOC1iODY5LTQxMjhjYWM0MzJkMSIsImNyZWF0ZWQiOjE2OTU3MTA1MTgzNTYsImV4aXN0aW5nIjp0cnVlfQ==',
            '_pk_ses.1.3ae9': '1',
            '_gid': 'GA1.2.25044513.1696927281',
            '_gat_UA-30790406-1': '1',
            '_hjIncludedInSessionSample_283045': '1',
            '_hjSession_283045': 'eyJpZCI6IjBjNWZhNmMwLTA4NTktNDk4Zi04NjUxLTc1YzlhODNmOGExMSIsImNyZWF0ZWQiOjE2OTY5MjcyODI3NjAsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=',
            '_hjAbsoluteSessionInProgress': '0',
            'SSESS46e5ac66c3cb256f0a441094408a6223': 'XgpEdzgSCb7pB0uCtHhYcmNKNFqyevIFdUdqUYs1MF%2C7VtPx',
            'HASH_SSESS46e5ac66c3cb256f0a441094408a6223': 'D6B378D97C3EF4A11807D1C6020FA381389006F1',
            '_ga_GD17PFQCL8': 'GS1.1.1696927280.10.1.1696927315.0.0.0',
            '_ga': 'GA1.1.1014721132.1695710518',
        }

        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': '_pk_id.1.3ae9=a9494f833e61216b.1695710517.; _hjSessionUser_283045=eyJpZCI6ImM0NjQ0N2JmLTQwZTMtNTFmOC1iODY5LTQxMjhjYWM0MzJkMSIsImNyZWF0ZWQiOjE2OTU3MTA1MTgzNTYsImV4aXN0aW5nIjp0cnVlfQ==; _pk_ses.1.3ae9=1; _gid=GA1.2.25044513.1696927281; _gat_UA-30790406-1=1; _hjIncludedInSessionSample_283045=1; _hjSession_283045=eyJpZCI6IjBjNWZhNmMwLTA4NTktNDk4Zi04NjUxLTc1YzlhODNmOGExMSIsImNyZWF0ZWQiOjE2OTY5MjcyODI3NjAsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; SSESS46e5ac66c3cb256f0a441094408a6223=XgpEdzgSCb7pB0uCtHhYcmNKNFqyevIFdUdqUYs1MF%2C7VtPx; HASH_SSESS46e5ac66c3cb256f0a441094408a6223=D6B378D97C3EF4A11807D1C6020FA381389006F1; _ga_GD17PFQCL8=GS1.1.1696927280.10.1.1696927315.0.0.0; _ga=GA1.1.1014721132.1695710518',
            'Origin': 'https://www.cpsbc.ca',
            'Referer': 'https://www.cpsbc.ca/public/registrant-directory/search-result',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        self.params = {
            'ajax_form': '1',
            '_wrapper_format': 'drupal_ajax',
        }

        self.data = [
            ('form_build_id', 'form-kMtQTyJ9SW23tRhvSWT_zyrkkahYto6BmUYjf7OSfxo'),
            ('form_id', 'cpsbc_directory_form'),
            ('ps_last_name', ''),
            ('ps_first_name', ''),
            ('ps_ci_to', ''),
            ('PracticeTypeSearch', 'A'),
            ('CertificationTypes', '0'),
            ('status', 'Y'),
            ('gender', 'M'),
            ('Languages', '0'),
            ('msp_number', ''),
            ('pagination_info', '1'),
            ('form_build_id', 'form-kMtQTyJ9SW23tRhvSWT_zyrkkahYto6BmUYjf7OSfxo'),
            ('form_id', 'cpsbc_directory_form'),
            ('_triggering_element_name', 'op'),
            ('_triggering_element_value', 'Search'),
            ('_drupal_ajax', '1'),
            ('ajax_page_state[theme]', 'college'),
            ('ajax_page_state[theme_token]', ''),
            ('ajax_page_state[libraries]', 'addtoany/addtoany.front,classy/base,classy/messages,college/bootstrap,college/global-theming,core/drupal.ajax,core/drupal.autocomplete,core/internal.jquery.form,core/normalize,cpsbc_directory/cpsbc_directory,matomo/matomo,search_api_autocomplete/search_api_autocomplete,system/base,views/views.module'),
        ]
        with open('done.json', 'r') as json_file:
            self.done = json.load(json_file)

    def make_request(self, url, data):
        while True:
            try:
                res = requests.post(
                    url, headers=self.headers, cookies=self.cookies, params=self.params, data=data)
                break
            except Exception as e:
                print(e, 'make request')
                time.sleep(3)
                pass
        return res

    def get_data(self, link):
        if link not in self.done:
            print(link)
            schama = {
                "Link": "",
                "MSP number": "",
                "Title": "",
                "Gender": "",
                "Languages": "",
                "Registration Status": "",
                "Registration Class": "",
                "Practice Type": "",
                "Certification": "",
                "Degree": "",
                "Year": "",
                "University": "",
                "details": []
            }
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'lxml')
            schama['Link'] = link

            schama['MSP number'] = self.helper.get_text_from_tag(
                soup.find('h5', {'class': 'mspNumber align-self-end'}))

            schama['Title'] = self.helper.get_text_from_tag(
                soup.find('h1', {'class': 'directory-profile--name'}))

            Summary_div = soup.find('div', {'id': 'summary'})
            gender_label = Summary_div.find('strong', text='Gender: ')
            schama['Gender'] = gender_label.find_next(
                'span').text if gender_label else None

            languages = []
            languages_div = Summary_div.find(
                'div', {'class': 'mb-2'}).find_all('span')
            for span in languages_div:
                languages.append(
                    self.helper.get_text_from_tag(span).replace(',', ''))
            schama['Languages'] = languages

            registration_div = soup.find('div', {'id': 'registration'})

            registration_status = registration_div.find(
                'strong', text='Registration status: ')
            if registration_status:
                schama['Registration Status'] = registration_status.find_next(
                    'span').text

            registration_class = registration_div.find(
                'strong', text='Registration class: ')
            if registration_class:
                schama['Registration Class'] = registration_class.find_next(
                    'span').text

            practice_type = registration_div.find(
                'strong', text='Practice type: ')
            if practice_type:
                schama['Practice Type'] = practice_type.find_next(
                    'span').text.strip()

            certification_label = soup.find('strong', text='Certification:')
            certification_details = []

            if certification_label:
                certification_span = certification_label.find_next('span')
                certification_items = certification_span.find_all('span')

                for item in certification_items:
                    certification_details.append(item.text.strip())

            schama['Certification'] = certification_details

            education_div = soup.find('div', {'id': 'education'})
            degree_details = education_div.find(
                'div', class_='directory-profile__degree')

            if degree_details:
                spans = degree_details.find_all('span')
                if len(spans) >= 2:
                    schama['Degree'] = spans[1].text.strip()
                else:
                    schama['Degree'] = 'null'

                if len(spans) >= 4:
                    schama['Year'] = spans[2].text.strip()
                    schama['University'] = spans[3].text.strip()
                else:
                    schama['Year'] = 'null'
                    schama['University'] = 'null'
            else:
                schama['Degree'] = 'null'
                schama['Year'] = 'null'
                schama['University'] = 'null'

            contact_div = soup.find('div', {'id': 'contact'})
            address_items = contact_div.find_all(class_='address-item')
            details = []
            for item in address_items:
                address_element = item.find('strong', string='Address: ')
                phone_element = item.find('strong', string='Phone: ')
                fax_element = item.find('strong', string='Fax: ')

                address = address_element.find_next('span').get_text(
                    strip=True) if address_element else ''
                phone = phone_element.find_next('span').get_text(
                    strip=True) if phone_element else ''
                fax = fax_element.find_next('span').get_text(
                    strip=True) if fax_element else ''
                details.append({
                    'Addresses': address,
                    'Contact Numbers': phone,
                    'Fax Number': fax
                })
            schama['details'] = details
            # print(json.dumps(schama))
            self.all_data.append(schama)
            self.done.append(link)
            with open("done.json", "w") as json_file:
                json.dump(self.done, json_file, indent=4)
            print(len(self.all_data))
            with open("data.json", "w") as json_file:
                json.dump(self.all_data, json_file, indent=4)
        # return self.all_data

    def run_multiThread(self, function, max_workers, args):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(function, args)

    def scarp(self):
        with open('All_listing.json', 'r') as input:
            listing = json.load(input)
        print(len(listing))
        self.run_multiThread(
            self.get_data,
            20,
            listing,
        )


if __name__ == "__main__":
    obj = CPSBC()
    obj.scarp()
    # obj.get_data('https://www.cpsbc.ca/public/registrant-directory/search-result/357625/Abdalvand%2CAli')
