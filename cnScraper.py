from bs4 import BeautifulSoup
import requests

source = requests.get('https://cybernations.lyricalz.com/war_list?page=1').text
soup = BeautifulSoup(source, 'lxml')

table = soup.find('table', class_='table-striped')
#print(table.prettify())

rows = table.find_all('tr')[1:]  # skip header row

for row in rows:
    cells = row.find_all('td')
    if len(cells) < 11:
        continue

    receiving_nation = cells[0].text.strip()
    receiving_alliance = cells[1].text.strip()
    declaring_nation = cells[2].text.strip()
    declaring_alliance = cells[3].text.strip()
    total_destruction = cells[4].text.strip()
    status = cells[8].text.strip()
    start = cells[9].text.strip()
    end = cells[10].text.strip()
    reason = cells[7].text.strip()

    #print(f"{declaring_nation} → {receiving_nation} | Destruction: {total_destruction} | {start} to {end} | Reason: {reason}")
    #Figure out how to post new wars to X
    #import tweepy
    
