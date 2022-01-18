from cgitb import text
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
import xml.etree.cElementTree as ET
import os
import random

def req(url):
  print('loading', url)
  fn = 'cookie.txt'
  with open(fn, 'r') as f:
    cookie = f.read()
  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0', 
                    'Cookie':cookie})
  res = s.get(url)
  with open("last.html", "wb") as f:
    f.write(res.content)
  sleep(5)
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
  all_comment = []
  for comment in comments:
    main_comment = comment.find('div').find('div').text
    all_comment.append(main_comment)
    replied_comment_link = comment.find('div').find_all('a', id=re.compile('^u_0_*'), href=re.compile('^/comment*'))
    for link in replied_comment_link:
      all_comment = all_comment + GetCommentRepiles(base+link['href'])
  return all_comment

def GetCommentRepiles(url):
  comment_text = []
  if 'replies/' not in url:
    return comment_text
  result = req(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  comments = soup.find('div', id='root').find_all('div', id=re.compile('^\d'))
  for comment in comments[1:]:
    comment_text.append(comment.find('div').find('div').text)
  return comment_text

def load_links():
  with open('articles_links.txt', 'r') as f:
    return [i for i in f.read().split() if i]

if __name__ == '__main__':
  group_page = "https://mbasic.facebook.com/groups/143704482352660"
  fn_links = 'next_pages.txt'
  fn_arts = 'articles.txt'
  fn_arts_links = 'articles_links.txt'
  links = load_links()
  for link in links:
    permaID = link.split('/')[-1]
    if [filename for filename in os.listdir('post_content') if permaID in filename]: 
      print(permaID, 'exists. skip.')
      continue
    try:
      result = req(link)
      with open("post.html", "wb") as f:
        f.write(result.content)
      post_content, post_reaction = GetPostContent(result)
      post_comment = GetPostComment(result)
      # print(link, post_content, post_reaction, post_comment)
    except:
      print("failed with loading ", link)
      sleep(5)