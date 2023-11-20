import concurrent.futures
import json
import math
import time
import requests
from bs4 import BeautifulSoup
from helper_class import *


class Scraper:
    def __init__(self):
        self.helper = Helper()
        self.lastpage = 1
        self.listing = []
        self.url = "https://www.cpsbc.ca/public/registrant-directory/search-result"
        self.cookies = {
            'SSESS46e5ac66c3cb256f0a441094408a6223': '1ZgbHBh0BFtQjiJP27EuwDFVtbyN%2CSbuDtVCJOCG1kINQvGj',
            'HASH_SSESS46e5ac66c3cb256f0a441094408a6223': '040531FB5A19A0A1472B2FE180F34E29319AB83B',
            '_pk_id.1.3ae9': 'a9494f833e61216b.1695710517.',
            '_gid': 'GA1.2.571827558.1695710518',
            '_pk_ses.1.3ae9': '1',
            '_hjSessionUser_283045': 'eyJpZCI6ImM0NjQ0N2JmLTQwZTMtNTFmOC1iODY5LTQxMjhjYWM0MzJkMSIsImNyZWF0ZWQiOjE2OTU3MTA1MTgzNTYsImV4aXN0aW5nIjp0cnVlfQ==',
            '_hjIncludedInSessionSample_283045': '1',
            '_hjSession_283045': 'eyJpZCI6IjA5NWI1ZTg1LTg0NjUtNGI3Yy1iZWJjLTI4ZDY3ZDM2MWIxOCIsImNyZWF0ZWQiOjE2OTU3MjMzNzMzODEsImluU2FtcGxlIjp0cnVlfQ==',
            '_hjAbsoluteSessionInProgress': '0',
            '_gat_UA-30790406-1': '1',
            '_ga_GD17PFQCL8': 'GS1.1.1695723373.2.1.1695723806.0.0.0',
            '_ga': 'GA1.1.1014721132.1695710518',
        }

        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'SSESS46e5ac66c3cb256f0a441094408a6223=1ZgbHBh0BFtQjiJP27EuwDFVtbyN%2CSbuDtVCJOCG1kINQvGj; HASH_SSESS46e5ac66c3cb256f0a441094408a6223=040531FB5A19A0A1472B2FE180F34E29319AB83B; _pk_id.1.3ae9=a9494f833e61216b.1695710517.; _gid=GA1.2.571827558.1695710518; _pk_ses.1.3ae9=1; _hjSessionUser_283045=eyJpZCI6ImM0NjQ0N2JmLTQwZTMtNTFmOC1iODY5LTQxMjhjYWM0MzJkMSIsImNyZWF0ZWQiOjE2OTU3MTA1MTgzNTYsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_283045=1; _hjSession_283045=eyJpZCI6IjA5NWI1ZTg1LTg0NjUtNGI3Yy1iZWJjLTI4ZDY3ZDM2MWIxOCIsImNyZWF0ZWQiOjE2OTU3MjMzNzMzODEsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _gat_UA-30790406-1=1; _ga_GD17PFQCL8=GS1.1.1695723373.2.1.1695723806.0.0.0; _ga=GA1.1.1014721132.1695710518',
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

        self.data = {
            'form_build_id': 'form-1sufcB-SK_msryAOCqm4YRt6SSsdtSulq6BaJRHtAJY',
            'form_id': 'cpsbc_directory_form',
            'ps_last_name': 'A',
            'ps_first_name': '',
            'ps_ci_to': '',
            'PracticeTypeSearch': 'A',
            'CertificationTypes': '0',
            'status': 'A',
            'gender': 'M',
            'Languages': '0',
            'msp_number': '',
            'pagination_info': '1',
            'form_build_id': 'form-1sufcB-SK_msryAOCqm4YRt6SSsdtSulq6BaJRHtAJY',
            'form_id': 'cpsbc_directory_form',
            'results_per_page': '20',
            'results_per_page_mobile': '20',
            'footer_results_per_page': '20',
            'footer_results_per_page_mobile': '20',
            '_triggering_element_name': 'op',
            '_triggering_element_value': 'Search',
            '_drupal_ajax': '1',
            'ajax_page_state[theme]': 'college',
            'ajax_page_state[theme_token]': '',
            'ajax_page_state[libraries]': 'addtoany/addtoany.front,big_pipe/big_pipe,classy/base,classy/messages,college/bootstrap,college/global-theming,core/drupal.ajax,core/drupal.autocomplete,core/internal.jquery.form,core/normalize,cpsbc_directory/cpsbc_directory,matomo/matomo,search_api_autocomplete/search_api_autocomplete,system/base,views/views.module',
        }

    def get_links(self, combination):
        count = 0
        listing = []

        print(combination)

        self.data['pagination_info'] = 1
        ps_last_name_value = combination['ps_last_name']
        gender_value = combination['gender']
        filename = '{}{}'.format(ps_last_name_value, gender_value)

        self.data['ps_last_name'] = ps_last_name_value
        self.data['gender'] = gender_value

        json_data = self.make_request(self.data)
        html = json_data[2]['data']
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.find_all(
            'div', {'class': 'shadow shadow-hover rounded result-item'})

        for div in divs:
            a_tags = div.find_all('a', href=True)
            listing.extend(["https://www.cpsbc.ca" + a['href']
                           for a in a_tags])

        print(filename)
        print(self.helper.get_text_from_tag(
            soup.find('span', {'class': 'text-mid-blue'})))

        lastpages_text = self.helper.get_text_from_tag(
            soup.find('span', {'class': 'text-mid-blue'}))
        if lastpages_text:
            lastpages = int(lastpages_text)
            lastpage = math.ceil(lastpages / 20)
        else:
            lastpage = 1

        numbers = [i for i in range(2, lastpage + 1)]
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            arguments = zip(numbers, [listing] *
                            len(numbers), [filename] * len(numbers))
            executor.map(lambda args: self.get_link_data(*args), arguments)

        count += 1
        time.sleep(5)

    def get_link_data(self, numbers, listing, filename):
        link = []
        print("===========================", numbers)
        data = self.data
        data['pagination_info'] = str(numbers)
        json_data = self.make_request(data)
        html = json_data[2]['data']
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.find_all(
            'div', {'class': 'shadow shadow-hover rounded result-item'})

        for div in divs:
            a_tags = div.find_all('a', href=True)
            link.extend(["https://www.cpsbc.ca" + a['href'] for a in a_tags])

        listing.extend(link)
        print(len(listing))
        self.save_links_to_json(
            "Output/listings_{}.json".format(filename), listing)

    def save_links_to_json(self, filename, listing):
        with open(filename, "w") as json_file:
            json.dump(listing, json_file, indent=4)

    def make_request(self, data):
        while True:
            try:
                res = requests.post(
                    self.url, headers=self.headers,
                    cookies=self.cookies,
                    params=self.params, data=data)
                json_data = res.json()
                html = json_data[2]['data']
                soup = BeautifulSoup(html, 'lxml')
                lastpages_text = self.helper.get_text_from_tag(
                    soup.find('span', {'class': 'text-mid-blue'}))
                if lastpages_text:
                    return res.json()

            except Exception as e:
                print(e, 'make request')
                pass


if __name__ == "__main__":
    combinations = [
        {"ps_last_name": 'A', "gender": "M"}, {"ps_last_name": 'B', "gender": "M"}, {"ps_last_name": 'C', "gender": "M"}, {
            "ps_last_name": 'D', "gender": "M"}, {"ps_last_name": 'E', "gender": "M"}, {"ps_last_name": 'F', "gender": "M"},
        {"ps_last_name": 'G', "gender": "M"}, {"ps_last_name": 'H', "gender": "M"}, {"ps_last_name": 'I', "gender": "M"}, {
            "ps_last_name": 'J', "gender": "M"}, {"ps_last_name": 'K', "gender": "M"}, {"ps_last_name": 'L', "gender": "M"},
        {"ps_last_name": 'M', "gender": "M"}, {"ps_last_name": 'N', "gender": "M"}, {"ps_last_name": 'O', "gender": "M"}, {
            "ps_last_name": 'P', "gender": "M"}, {"ps_last_name": 'Q', "gender": "M"}, {"ps_last_name": 'R', "gender": "M"},
        {"ps_last_name": 'S', "gender": "M"}, {"ps_last_name": 'T', "gender": "M"}, {"ps_last_name": 'U', "gender": "M"}, {
            "ps_last_name": 'V', "gender": "M"}, {"ps_last_name": 'W', "gender": "M"}, {"ps_last_name": 'X', "gender": "M"},
        {"ps_last_name": 'Y', "gender": "M"},
        {"ps_last_name": 'Z', "gender": "M"},
        {"ps_last_name": 'A', "gender": "F"}, {"ps_last_name": 'B', "gender": "F"}, {"ps_last_name": 'C', "gender": "F"}, {
            "ps_last_name": 'D', "gender": "F"}, {"ps_last_name": 'E', "gender": "F"}, {"ps_last_name": 'F', "gender": "F"},
        {"ps_last_name": 'G', "gender": "F"}, {"ps_last_name": 'H', "gender": "F"}, {"ps_last_name": 'I', "gender": "F"}, {
            "ps_last_name": 'J', "gender": "F"}, {"ps_last_name": 'K', "gender": "F"}, {"ps_last_name": 'L', "gender": "F"},
        {"ps_last_name": 'M', "gender": "F"}, {"ps_last_name": 'N', "gender": "F"}, {"ps_last_name": 'O', "gender": "F"}, {
            "ps_last_name": 'P', "gender": "F"}, {"ps_last_name": 'Q', "gender": "F"}, {"ps_last_name": 'R', "gender": "F"},
        {"ps_last_name": 'S', "gender": "F"}, {"ps_last_name": 'T', "gender": "F"}, {"ps_last_name": 'U', "gender": "F"}, {
            "ps_last_name": 'V', "gender": "F"}, {"ps_last_name": 'W', "gender": "F"}, {"ps_last_name": 'X', "gender": "F"},
        {"ps_last_name": 'Y', "gender": "F"},
        {"ps_last_name": 'Z', "gender": "F"}
    ]

    scraper = Scraper()
    for combination in combinations:
        scraper.get_links(combination)
