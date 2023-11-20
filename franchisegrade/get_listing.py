import requests 
from bs4 import BeautifulSoup
from helper_class import *

class franchisegrade():

    def __init__(self):
        
        self.helper = Helper()
        self.listing =[]
        self.cookies = {
            '_gid': 'GA1.2.1186956354.1695809887',
            '_gcl_au': '1.1.1554912318.1695809888',
            '__hstc': '172847676.422c19bb9b2716e62a7fbfbce82fe916.1695809891577.1695809891577.1695809891577.1',
            'hubspotutk': '422c19bb9b2716e62a7fbfbce82fe916',
            '__hssrc': '1',
            'ahoy_visitor': 'dfcf8ccc-2ad2-413b-bb83-6ff39df310a7',
            'ahoy_visit': '48ab5c0d-f1b0-44fd-8f54-d65026ba4cf2',
            '_session_id': '3d3952ceeba8f1a41821bcc9b050930b',
            'ln_or': 'eyIyNTAxNTMwIjoiZCJ9',
            '_ga': 'GA1.2.1362039215.1695809887',
            '_ga_R16905N8HJ': 'GS1.2.1695809886.1.1.1695811467.16.0.0',
            '__hssc': '172847676.13.1695809891577',
            '_gali': 'main',
        }

        self.headers = {
            'authority': 'www.franchisegrade.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': '_gid=GA1.2.1186956354.1695809887; _gcl_au=1.1.1554912318.1695809888; __hstc=172847676.422c19bb9b2716e62a7fbfbce82fe916.1695809891577.1695809891577.1695809891577.1; hubspotutk=422c19bb9b2716e62a7fbfbce82fe916; __hssrc=1; ahoy_visitor=dfcf8ccc-2ad2-413b-bb83-6ff39df310a7; ahoy_visit=48ab5c0d-f1b0-44fd-8f54-d65026ba4cf2; _session_id=3d3952ceeba8f1a41821bcc9b050930b; ln_or=eyIyNTAxNTMwIjoiZCJ9; _ga=GA1.2.1362039215.1695809887; _ga_R16905N8HJ=GS1.2.1695809886.1.1.1695811467.16.0.0; __hssc=172847676.13.1695809891577; _gali=main',
            'referer': 'https://www.franchisegrade.com/search?page=1&results=36',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }

    def get_listing(self):
        for i in range(13):
            print("pages==========>",i)
            params = {
                'page': str(i),
                'results': '36',
            }
            response = requests.get("https://www.franchisegrade.com/search?page=1&results=36&sector=3",headers=self.headers,cookies=self.cookies,params=params)
            soup = BeautifulSoup(response.content,'lxml')
            for i in soup.find_all('a',{'class':'listing-tile '}):
                self.listing.append(self.helper.get_url_from_tag(i))
            print(len(list(set(self.listing))))
            with open ('Output\listing.json','w') as json_file:
                json.dump(self.listing,json_file,indent=4)

    def json_in_output(self):
        data = []
        x = os.listdir("Output")
        print(len(x))
        for filename in x:
            with open('Output/' + filename, encoding='utf-8') as json_data:
                data += json.load(json_data)
        listing_urls = []
        for url in data:
            listing_urls.append(url)
        listing_urls = list(set(listing_urls))
        print(len(listing_urls))
        with open('Output_Final.json', 'w', encoding='utf-8') as outfile:
            json.dump(listing_urls, outfile, indent=4)

if __name__ == "__main__":
    object = franchisegrade()
    object.get_listing()
    object.json_in_output()

