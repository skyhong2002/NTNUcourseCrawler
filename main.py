import requests
from bs4 import BeautifulSoup

ck = '''fr=0dzkDfFURgFedp85U.AWXhHadKDMgMCJm16XKIztJVhWY.Bh19fG.eZ.AAA.0.0.Bh19ft.AWU2C_WZeE0; sb=xtfXYd3Z-tdBaoqEw8Ie3m-7; wd=1280x713; dpr=2; datr=xtfXYYX9BpUC1eUwGD20kvtM; locale=en_US; c_user=100000852003681; xs=5%3AB_xRB7PR5Q00bg%3A2%3A1641535471%3A-1%3A11327; spin=r.1004918612_b.trunk_t.1641535486_s.1_v.2_'''
rs = requests.session()
url = 'https://mbasic.facebook.com/groups/143704482352660/'
url = 'https://mbasic.facebook.com/groups/143704482352660?bacr=1638025090%3A4927134114009649%3A4927134114009649%2C0%2C2%3A7%3AKw%3D%3D&multi_permalinks&refid=18'
rs.headers.update({
    'Cookie':ck 
})
res = rs.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(res.text)

with open('test.html', 'wb') as f:
    f.write(res.content)