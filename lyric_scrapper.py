import requests
from bs4 import BeautifulSoup
URL = 'https://lyrics.fandom.com/wiki/Bob_Dylan:The_Times_They_Are_A-Changin\''
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

def test():

