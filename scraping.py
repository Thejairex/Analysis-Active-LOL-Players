from bs4 import BeautifulSoup
import requests
import pandas as pd

class Scraper:
    def __init__(self) -> None:
        self.dataset = {
            "month": [],
            "avg_month": [],
            "monthly_change": [],
            "monthly_change_pct": [],
            "peak_players": [],
        }
        self.soup = self.get_soup("https://activeplayer.io/league-of-legends/")
        
    def get_soup(sefl, url):
        return BeautifulSoup(requests.get(url).text, 'html.parser')


    def get_data(self):
        
        def clean_text(text):
            return text.replace('\n', '').replace(',', '')
        
        for i in range(0,49):
            datas = self.soup.find('tr', attrs={'id': f'table_70_row_{i}'}).find_all('td')
            
            self.dataset["month"].append(datas[0].text)
            self.dataset["avg_month"].append(eval(clean_text(datas[1].text)))
            self.dataset["monthly_change"].append(eval(clean_text(datas[2].text))) 
            self.dataset["monthly_change_pct"].append(eval(clean_text(datas[3].text))) 
            self.dataset["peak_players"].append(eval(clean_text(datas[4].text)))
            

        pd.DataFrame(self.dataset).to_csv('Data/data.csv', index=False)

if __name__ == "__main__":
    scraper = Scraper()
    scraper.get_data()