import requests
from bs4 import BeautifulSoup
from time import sleep
import re
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

def GetPostContent(result):
  soup = BeautifulSoup(result.text, 'html.parser')
  for br in soup.find_all("br"):
    br.replace_with("\n")
  post = soup.find('div', class_='bm')
  article = post.find('div', style = True).text

  reaction = [s for s in soup.find_all("a", href=True) if "/ufi/reaction/profile/browser" in s['href']][0].text

  return article, reaction

def GetPostComment(result):
  base = 'https://mbasic.facebook.com'
  # if View previous comments… is found
  # find result and rerun
  soup = BeautifulSoup(result.text, 'html.parser')
  soup = soup.find('div', id=re.compile('^ufi_*'))
  comments = soup.find('div').find_all('div', id=re.compile('^\d'))
  for comment in comments:
    main_comment = comment.find('div').find('div').text
    print(main_comment)
    replied_comment_link = comment.find('div').find_all('a', id=re.compile('^u_0_*'))
    for link in replied_comment_link:
      print(base+link['href'])
  return 0

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

def load_links():
  with open('articles_links.txt', 'r') as f:
    return [i for i in f.read().split() if i]

next_page = "https://mbasic.facebook.com/groups/143704482352660"

fn = 'cookie.txt'
cookie = load_cookie(fn)
fn_links = 'next_pages.txt'
fn_arts = 'articles.txt'
fn_arts_links = 'articles_links.txt'

count = 0
links = load_links()
for link in links[87:90]:
  sleep(5)
  print(link)
  result = req(link, cookie)
  with open("post.html", "wb") as f:
    f.write(result.content)
  # post_content, post_reaction = GetPostContent(result)
  # print(post_content, post_reaction)
  post_comment = GetPostComment(result)

