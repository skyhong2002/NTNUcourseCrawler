import requests
from bs4 import BeautifulSoup
payload = {
'from': '/bbs/Gossiping/index.html',
'yes': 'yes'
}

ck = '''fr=0dzkDfFURgFedp85U.AWXhHadKDMgMCJm16XKIztJVhWY.Bh19fG.eZ.AAA.0.0.Bh19ft.AWU2C_WZeE0; sb=xtfXYd3Z-tdBaoqEw8Ie3m-7; wd=1280x713; dpr=2; datr=xtfXYYX9BpUC1eUwGD20kvtM; locale=en_US; c_user=100000852003681; xs=5%3AB_xRB7PR5Q00bg%3A2%3A1641535471%3A-1%3A11327; spin=r.1004918612_b.trunk_t.1641535486_s.1_v.2_'''
rs = requests.session()
url = 'https://mbasic.facebook.com/groups/143704482352660/'
rs.headers.update({
    'Cookie':ck 
})
res = rs.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(res.text)

with open('sky.html', 'wb') as f:
    f.write(res.content)