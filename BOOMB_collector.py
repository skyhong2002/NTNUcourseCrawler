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
  print(soup.find('span', text="查看更多貼文"))
  try:
    next_page = base + soup.find('div', id='m_group_stories_container').find_all('div')[-1].a['href']  
  except:
    next_page = base + soup.find('a', href=True, text="查看更多貼文")['href']  
  print((next_page))
  #title = soup.find('h1', class_='entry-title').text

  return next_page



def beauti6(res):

  soup = BeautifulSoup(res.text, 'html.parser')
  articles = soup.find_all('article', class_='db dd dn')
  links = [a.footer.find('a', text="完整動態")['href'].split('/?')[0] for a in articles[1:]]
  #print(links)
    #print(art, end='\n\n')
  #print((articles[6].find('div', class_='dt').text))
  #title = soup.find('h1', class_='entry-title').text

  return links





next_page = "https://mbasic.facebook.com/groups/143704482352660"
next_page = "https://mbasic.facebook.com/groups/143704482352660?bacr=1393691877%3A669118679811235%3A669118679811235%2C0%2C750%3A7%3AKw%3D%3D&multi_permalinks&refid=18"

fn = 'cookie_TW.txt'
cookie = load_cookie(fn)
fn_links = 'next_pages.txt'
fn_arts = 'articles.txt'
fn_arts_links = 'articles_links.txt'

count = 0

while True:
  count += 1
  print('#'*10, count, '#'*10)
 
  if count%30 == 0:
    n = random.randint(60, 180)
    sleep(n)
  n = random.randint(5, 15)
  sleep(n) #######
  res = req(next_page, cookie)
  with open("test.html", "wb") as f:
    f.write(res.content)
  dates, articles = beauti4(res)
  data = ''
  for i in range(len(articles)):
    data += articles[i] + "\n-----------------%s-----------------\n"%(dates[i])
  print(data)

  with open(fn_arts, 'a', encoding='utf-8') as f:
    f.write(data)

  links = beauti6(res)

  data = "\n".join(links)+"\n"
  print(data)
  with open(fn_arts_links, 'a', encoding='utf-8') as f:
    f.write(data)
  with open(fn_links, 'a', encoding='utf-8') as f:
    f.write(next_page+'\n')
    
  next_page = beauti5(res)
  '''
  try:
    n = random.randint(5, 20)
    sleep(n)
    res = req(next_page, cookie)
    with open("test.html", "w", encoding="latin-1") as f:
      f.write(res.text)

    dates, articles = beauti4(res)
    data = ''
    for i in range(len(articles)):
      data += articles[i] + "\n-----------------%s-----------------\n"%(dates[i])
    print(data)

    with open(fn_arts, 'a', encoding='utf-8') as f:
      f.write(data)

    links = beauti6(res)

    data = "\n".join(links)+"\n"
    print(data)
    with open(fn_arts_links, 'a', encoding='utf-8') as f:
      f.write(data)
    with open(fn_links, 'a', encoding='utf-8') as f:
      f.write(next_page+'\n')
    
    next_page = beauti5(res)
  except:
    sleep(10)
    continue
  '''


























