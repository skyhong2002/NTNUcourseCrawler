from cgitb import text
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
from xml.dom import minidom
import os
import random

def load_links(link_filename):
  with open(link_filename, 'r') as f:
    return [i for i in f.read().split() if i]

def req(url):
  print('loading', url)
  fn = 'cookie_EN.txt'
  with open(fn, 'r') as f:
    cookie = f.read()
  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0', 
                    'Cookie':cookie})
  res = s.get(url)
  with open("last.html", "wb") as f:
    f.write(res.content)
  sleep(random.randint(5,10))
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


def data2xml(permaID, post_content, post_reaction, post_comment):
  xmlfile = minidom.Document()
  node = xmlfile.createElement('d')
  node.setAttribute('n'  , 'post_' + permaID)
  node.setAttribute('book'  , permaID)
  node_text = xmlfile.createTextNode(post_content)
  node.appendChild(node_text)
  xmlfile.appendChild(node)
  return xmlfile

if __name__ == '__main__':
  group_page = "https://mbasic.facebook.com/groups/143704482352660"
  fn_arts_links = 'articles_links.txt'
  links = load_links(fn_arts_links)
  i = 0
  for link in links:
    i = i+1
    print(i, end=' ')
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
      with open('post_content' + os.sep + permaID + '.txt', 'w') as f:
        f.write(post_content.replace('\n', ' ') + '\n')
        f.write(post_reaction + '\n')
        for comment in post_comment:
          f.write(comment.replace('\n', ' ') + '\n')
      '''xmlfile = data2xml(permaID, post_content, post_reaction, post_comment)
      with open('post_content' + os.sep + permaID + '.xml', 'w') as f:
        xmlfile.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')'''
    except:
      print("failed with loading ", link)
      sleep(5)