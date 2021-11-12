from bs4 import BeautifulSoup
import requests
import shutil

page = requests.get('https://www.justwatch.com/us/provider/netflix')
soup = BeautifulSoup(page.content, 'html.parser')

main_page_lists = soup.find('div', class_='title-list-grid')
imgs = main_page_lists.find_all('img')
shows_grid = main_page_lists.find_all('div', 'title-list-grid__item')

for img in imgs:
  img_url = ''
  try:
    img_url = img['data-src']
  except:
    img_url = img['src']
  r = requests.get(img_url)
  r.raw.decode_content = True
  with open(img['alt'].replace(' ', '-')+'.jpeg', 'wb') as f:
    f.write(r.content)

for div in shows_grid:
  r = requests.get('https://www.justwatch.com'+ div.find('a')['href'])
  soup2 = BeautifulSoup(r.content, 'html.parser')
  rating_div = soup2.find('div', class_='jw-scoring-listing__rating')
  print(rating_div.find('a').get_text())
