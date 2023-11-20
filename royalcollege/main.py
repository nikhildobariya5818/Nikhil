import requests
from bs4 import BeautifulSoup
import json
import undetected_chromedriver as uc
import psutil
import time


class ROYALCOLLAGE():

    def __init__(self, url):
        self.url = url
        self.cookies = {
    'JSESSIONID': 'c0cY3Uz6_oOXkmDLGlD_DLS8vFOEwhUQ5pDSj8K-4LYcKptrirgG!-1815329270',
    'oracle.adf.view.rich.automation.ENABLED': 'FULL',
    'LOGIN_NLS': 'en',
    '_ga_3PP85V2VM8': 'GS1.1.1696929244.1.0.1696929244.0.0.0',
    '_ga': 'GA1.2.425431206.1696929244',
    '_gid': 'GA1.2.1891468872.1696929245',
    '_gat_gtag_UA_29215260_1': '1',
}

        self.headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Adf-Ads-Page-Id': '1',
    'Adf-Rich-Message': 'true',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=c0cY3Uz6_oOXkmDLGlD_DLS8vFOEwhUQ5pDSj8K-4LYcKptrirgG!-1815329270; oracle.adf.view.rich.automation.ENABLED=FULL; LOGIN_NLS=en; _ga_3PP85V2VM8=GS1.1.1696929244.1.0.1696929244.0.0.0; _ga=GA1.2.425431206.1696929244; _gid=GA1.2.1891468872.1696929245; _gat_gtag_UA_29215260_1=1',
    'Origin': 'https://rclogin.royalcollege.ca',
    'Referer': 'https://rclogin.royalcollege.ca/webcenter/portal/rcdirectory_en/RCDirectorySearch',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

        self.params = {
    'Adf-Window-Id': 'w151wefksnn',
    'Adf-Page-Id': '0',
    '_afrECID': '0061p^YI48eApIYjLpINOA0002uG00029k',
}


    def make_request(self, url, cookies):
        while True:
            try:
                res = requests.get(url, headers=self.headers,
                                   cookies=cookies)
                break
            except Exception as e:
                print(e, 'make request')
                time.sleep(3)
                pass
        return res

    def scrape_page(self, start, end):
        data = f'wc.contextURL=%2Fspaces%2Frcdirectory_en&T:j_idt4:wcs_previouslySetPageTemplate=gsr5194f25d_51f5_4f30_a4fd_3ba3b8403962&T:dclay:oc_1588338513reijia1:sf1:inputText1=&T:dclay:oc_1588338513reijia1:sf1:selectOneChoice1=0&T:dclay:oc_1588338513reijia1:sf1:selectOneChoice2=0&T:dclay:oc_1588338513reijia1:sf1:selectOneChoice3=0&T:dclay:oc_1588338513reijia1:sf1:inputText2=&org.apache.myfaces.trinidad.faces.FORM=f1&Adf-Window-Id=w151wefksnn&Adf-Page-Id=0&javax.faces.ViewState=!12dijtox3j&oracle.adf.view.rich.RENDER=T%3Adclay%3Aoc_1588338513reijia1%3Asf1%3ARCDSearchResultWideTable&oracle.adf.view.rich.monitoring.UserActivityInfo=%3Cm+xmlns%3D%22http%3A%2F%2Foracle.com%2FrichClient%2Fcomm%22%3E%3Ck+v%3D%22pr0%22%3E%3Cm%3E%3Ck+v%3D%22cid%22%3E%3Cs%3E0061p%5EZio6UApIYjLpINOA0006Zy0001Mo%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22cst%22%3E%3Cs%3E1696929293273%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22cet%22%3E%3Cs%3E1696929293724%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22rrt%22%3E%3Cs%3E1696929293717%3C%2Fs%3E%3C%2Fk%3E%3C%2Fm%3E%3C%2Fk%3E%3Ck+v%3D%22prm%22%3E%3Cm%3E%3Ck+v%3D%22cst%22%3E%3Cs%3E1696929655893%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22eif%22%3E%3Cm%3E%3Ck+v%3D%22ety%22%3E%3Cs%3ErangeChange%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22cld%22%3E%3Cs%3ET%3Adclay%3Aoc_1588338513reijia1%3Asf1%3ARCDSearchResultWideTable%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22cty%22%3E%3Cs%3Eoracle.adf.RichTable%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22rvd%22%3E%3Cs%3E%2FrcdirectoryTF%2FadvancedSearch%3C%2Fs%3E%3C%2Fk%3E%3C%2Fm%3E%3C%2Fk%3E%3Ck+v%3D%22ppr%22%3E%3Cs%3ET%3Adclay%3Aoc_1588338513reijia1%3Asf1%3ARCDSearchResultWideTable%3C%2Fs%3E%3C%2Fk%3E%3C%2Fm%3E%3C%2Fk%3E%3C%2Fm%3E&event=T%3Adclay%3Aoc_1588338513reijia1%3Asf1%3ARCDSearchResultWideTable&event.T:dclay:oc_1588338513reijia1:sf1:RCDSearchResultWideTable=%3Cm+xmlns%3D%22http%3A%2F%2Foracle.com%2FrichClient%2Fcomm%22%3E%3Ck+v%3D%22oldStart%22%3E%3Cs%3E0%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22oldEnd%22%3E%3Cs%3E19%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22newStart%22%3E%3Cs%3E{start}%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22newEnd%22%3E%3Cs%3E{end}%3C%2Fs%3E%3C%2Fk%3E%3Ck+v%3D%22type%22%3E%3Cs%3ErangeChange%3C%2Fs%3E%3C%2Fk%3E%3C%2Fm%3E&oracle.adf.view.rich.PROCESS=T%3Adclay%3Aoc_1588338513reijia1%3Asf1%3ARCDSearchResultWideTable'
        while True:
            response = requests.post(
                self.url,
                params=self.params,
                cookies=self.cookies,
                headers=self.headers,
                data=data,
            )
            # print(response.status_code)
            if response.status_code == 403:
                print("Received 403 Forbidden. Updating cookies and retrying.1")
                self.cookies = self.get_cookies()  # Update cookies
                response = self.make_request(
                    self.url, self.headers, self.cookies)
                time.sleep(3)
            else:
                break
        soup = BeautifulSoup(response.content, 'lxml')
        divs = soup.find('div', {'class': 'af_table_data-body'})
        # print(divs)
        table = divs.find(
            'table', {'class': 'af_table_data-table af_table_data-table-VH-lines'})
        table_data = table.find_all('tr', {'class': 'af_table_data-row'})

        scraped_data = []

        for row in table_data:
            data_cells = row.find_all('td')

            data_dict = {
                'Name': data_cells[0].text.strip(),
                'Title': data_cells[1].text.strip(),
                'Qualification': data_cells[2].text.strip(),
                'Location': data_cells[3].text.strip(),
                'Specialization': data_cells[4].text.strip(),
            }

            scraped_data.append(data_dict)

        return scraped_data

    def get_collagedata(self):
        start = 1
        end = 20
        all_data = []
        i = 1
        # while True:
        for i in range(1, 2950):
            print("pages:", i)
            scraped_data = self.scrape_page(start, end)
            if not scraped_data:
                break

            all_data.extend(scraped_data)
            with open("data.json", "w") as json_file:
                json.dump(all_data, json_file)
            start += 20
            end += 20
            i += 1

        print(json.dumps(all_data))
        print(len(all_data))

    def get_cookies(self):
        while True:
            try:
                driver = uc.Chrome()
                driver.get('https://rclogin.royalcollege.ca/webcenter/portal/rcdirectory_en/RCDirectorySearch')
                cookies = driver.get_cookies()
                time .sleep(3)
                cookies_dict = {}
                for cookie in cookies:
                    cookies_dict[cookie['name']] = cookie['value']

                # cookies_dict['experimentSessionId'] = 'd65288be-4d37-4965-8973-8831ea2ccd2e'
                # print(cookies_dict)
                self.cookies = cookies_dict
                # print(json.dumps(self.cookies))
                driver.quit()

                try:
                    # Iterate through all running processes
                    for process in psutil.process_iter(attrs=['pid', 'name']):
                        # Check if the process is Chrome
                        if "chrome.exe" in process.info['name']:
                            pid = process.info['pid']
                            process_obj = psutil.Process(pid)
                            process_obj.terminate()  # Terminate the Chrome process
                            print(f"Terminated Chrome process with PID {pid}")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                return cookies_dict
            except Exception as e:
                time.sleep(3)
                try:
                    driver.quit()
                except:
                    pass
                print('Error in selenium', e)
                pass


if __name__ == "__main__":
    url = 'https://rclogin.royalcollege.ca/webcenter/portal/rcdirectory_en/RCDirectorySearch'
    obj = ROYALCOLLAGE(url)
    obj.get_collagedata()
