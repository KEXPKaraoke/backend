import requests
from bs4 import BeautifulSoup
class LyricScraper: 
sma    URL = 'https://lyrics.fandom.com/wiki/Bob_Dylan:The_Times_They_Are_A-Changin\''




    def scrape_lyrics(url): 
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        job_elems = soup.find("div", class_='lyricbox')
   
        print(job_elems.prettify())
        return job_elems   
    #test 
    scrape_lyrics(URL) 