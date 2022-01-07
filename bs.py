import requests
from bs4 import BeautifulSoup
payload = {
'from': '/bbs/Gossiping/index.html',
'yes': 'yes'
}
rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18',data=payload)
res = rs.get('http://www.ptt.cc/bbs/Gossiping/index.html')

soup = BeautifulSoup(res.text, 'html.parser') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析

# 使用 .select() 
for entry in soup.select('div.r-ent'):
    print(entry.select('div.title')[0].text,entry.select('div.date')[0].text)

# 使用 find_all()
div_tags = soup.find_all('div', {'class': 'title'}) #找到網頁中全部的 <div class="title">
for div_tag in div_tags:
    a_tag = div_tag.find('a') #找到 <div class="title"> 下的 <a>
    if a_tag is not None: #或文章被刪除會是None，所以要排除None
        print(a_tag.text) 
        # print(a_tag.get('href')) 