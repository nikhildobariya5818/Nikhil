import requests
from bs4 import BeautifulSoup
from helper_class import *

class Screper():

    def __init__(self):

        self.helper = Helper()
        
        self.cookies = {
            '_gid': 'GA1.2.1186956354.1695809887',
            '_gcl_au': '1.1.1554912318.1695809888',
            'ln_or': 'eyIyNTAxNTMwIjoiZCJ9',
            '__hstc': '172847676.422c19bb9b2716e62a7fbfbce82fe916.1695809891577.1695809891577.1695809891577.1',
            'hubspotutk': '422c19bb9b2716e62a7fbfbce82fe916',
            '__hssrc': '1',
            '_ga_R16905N8HJ': 'GS1.1.1695809886.1.1.1695812778.60.0.0',
            '_ga': 'GA1.2.1362039215.1695809887',
            '__hssc': '172847676.15.1695809891577',
        }

        self.headers = {
            'authority': 'franchisegrade.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': '_gid=GA1.2.1186956354.1695809887; _gcl_au=1.1.1554912318.1695809888; ln_or=eyIyNTAxNTMwIjoiZCJ9; __hstc=172847676.422c19bb9b2716e62a7fbfbce82fe916.1695809891577.1695809891577.1695809891577.1; hubspotutk=422c19bb9b2716e62a7fbfbce82fe916; __hssrc=1; _ga_R16905N8HJ=GS1.1.1695809886.1.1.1695812778.60.0.0; _ga=GA1.2.1362039215.1695809887; __hssc=172847676.15.1695809891577',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }
        
        self.all_data = []

    def get_Companies(self,link):
            obj = {
                'Source Website (URL)':'',
                'Source (Legal Name)':'Franchise Grade',
                'Trade':'',
                'Company Legal Name':'',
                'Company Website (URL)': '',
                'Company Description':'',
                'Company Units':'',
            }
            response = requests.get(
                link,headers=self.headers,cookies=self.cookies)
            soup = BeautifulSoup(response.content,'lxml')
            
            obj['Source Website (URL)']=  link

            obj['Company Legal Name'] = self.helper.get_text_from_tag(soup.find('h1',{'class':'small-12 cell'}))

            obj['Company Description'] = self.helper.get_text_from_tag(soup.find('h2').find_next('p'))

            obj['Trade'] = self.helper.get_text_from_tag(soup.find('div',{"class":"grid-x top-line"}).find_all('p')[-1]).replace('Category:','').strip()

            obj['Company Units'] = self.helper.get_text_from_tag(soup.find_all('div',{'class':'panel-body main cell'})[-1]).strip()

            self.all_data.append(obj)
            with open ('data.json','w') as json_file:
                 json.dump(self.all_data,json_file,indent=4)
            print(len(self.all_data))

    def run_multiThread(self, function, max_workers, args):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(function, args)

    def scraper(self):
        with open ('Output_Final.json','r') as json_file:
            listing = json.load(json_file)
        self.run_multiThread(
            self.get_Companies,
            10,
            listing
        )

if __name__ == "__main__":
    obj = Screper()
    obj.scraper()
