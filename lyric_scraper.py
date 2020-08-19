import requests
from bs4 import BeautifulSoup
class LyricScraper: 
    URL = 'https://lyrics.fandom.com/wiki/Bob_Dylan:The_Times_They_Are_A-Changin\''
    page = requests.get(URL)



    def scrape_lyrics(url): 
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        job_elems = soup.findAll("div", class_='lyricbox')
        for job_elem in job_elems:
            print(job_elem, end='\n'*2)
            
    #test 
    scrape_lyrics(URL) 