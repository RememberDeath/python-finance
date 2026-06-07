from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.wsaz.com/weather/').text
soup = BeautifulSoup(source, 'lxml')

#article = soup.find('div', class_ = 'forecast-teaser | w-100 d-none d-md-block') #Text Summary
article = soup.find('div', class_ = 'forecast-detailed | weather card mb-3') # find specific class in html

print(article.prettify())
#headline = article.text
#print(headline)
