import requests
from bs4 import BeautifulSoup
from time import sleep
import random




def load_cookie(fn):
	with open(fn, 'r') as f:
		return f.read()



def req(u, cookie):
  
  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0', 
                    'Cookie':cookie})
  res = s.get(u)
  
  return res



def beauti4(res):

  tmp = []
  dates = []

  base = 'https://mbasic.facebook.com'
  soup = BeautifulSoup(res.text, 'html.parser')
  for br in soup.find_all("br"):
    br.replace_with("\n")
  articles = soup.find_all('article', class_='db dd dn')
  for a in articles[1:]:
    art = a.find('div', class_='dt').text
    date = a.footer.div.text
    #print(date)
    tmp.append(art)
    dates.append(date)

  	#print(art, end='\n\n')
  #print((articles[6].find('div', class_='dt').text))
  #title = soup.find('h1', class_='entry-title').text

  return dates, tmp



def beauti5(res):
  base = 'https://mbasic.facebook.com'
  soup = BeautifulSoup(res.text, 'html.parser')
  next_page = base + soup.find('div', id='m_group_stories_container').find_all('div')[-1].a['href']  
  print((next_page))
  #title = soup.find('h1', class_='entry-title').text

  return next_page



def beauti6(res):
  soup = BeautifulSoup(res.text, 'html.parser')
  next_page = base + soup.find('div', id='m_group_stories_container').find_all('div')[-1].a['href']  
  print((next_page))
  #title = soup.find('h1', class_='entry-title').text

  return next_page





next_page = "https://mbasic.facebook.com/groups/143704482352660"
fn = 'cookie.txt'
cookie = load_cookie(fn)
fn_links = 'next_pages.txt'
fn_arts = 'articles.txt'

count = 0

while True:
  count += 1
  print('#'*10, count, '#'*10)
  if count%30 == 0:
    n = random.randint(60, 180)
    #sleep(30)
  try:
    n = random.randint(0, 5)
    sleep(n)
    res = req(next_page, cookie)
    dates, articles = beauti4(res)
    data = ''
    for i in range(len(articles)):
      data += articles[i] + "\n-----------------%s-----------------\n"%(dates[i])
    print(data)
    with open(fn_arts, 'a', encoding='utf-8') as f:
      f.write(data)
    with open(fn_links, 'a', encoding='utf-8') as f:
      f.write(next_page+'\n')
    next_page = beauti5(res)
  except:
    sleep(10)
    continue


























