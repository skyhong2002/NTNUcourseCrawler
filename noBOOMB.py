import requests
from bs4 import BeautifulSoup




def beauti4(res):
  soup = BeautifulSoup(res.text, 'html.parser')
  last_page = soup.find('form', id='mbasic-composer-form', href=True)['action']
  title = soup.find('h1', class_='entry-title').text

  return title, int(last_page)



def req(u, cookie):
  

  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0', 
                    'Cookie':cookie})
  res = s.get(u)
  
  return res



def reqp(u, cookie, body):
  

  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0', 
                    'Cookie':cookie})
  res = s.post(u, data=body)
  
  return res



def req_img(u, cookie, body, img):
  

  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0', 
                    'Cookie':cookie})
  res = s.post(u, data=body, files={'file':open(img, 'rb')})
  
  return res



def load_cookie(fn):
	with open(fn, 'r') as f:
		return f.read()



def get_payload(res):

	body = {}

	base = 'https://mbasic.facebook.com'
	soup = BeautifulSoup(res.text, 'html.parser')
	form = soup.find('form', id='composer_form')
	url = base + form['action']
	inps = form.find_all('input', type="hidden")
	print(form)
	for inp in inps:
		try:
			#print(inp['name'], inp['value'])
			body[inp['name']] = inp['value']
		except:
			body[inp['name']] = ''

	body['send'] = '傳送'
	body['body'] = ''

	return url, body




def get_img_payload(res):

	body = {}

	soup = BeautifulSoup(res.text, 'html.parser')
	form = soup.find('form', action=True, method='post')
	url = form['action']
	inps = form.find_all('input')
	print(form)
	for inp in inps:
		try:
			#print(inp['name'], inp['value'])
			body[inp['name']] = inp['value']
		except:
			try:
				body[inp['name']] = ''
			except:
				pass

	# body['send'] = '傳送'
	body['body'] = ''
	#print('777777777777777', url)

	return url, body



def send_msg(to, msg, cookie):
	base = 'https://mbasic.facebook.com'
	u = 'https://mbasic.facebook.com/messages/read/?fbid=' + to
	res = req(u, cookie)
	url, body = get_payload(res)
	body['body'] = msg
	print(body)
	print(url)
	#body='fb_dtsg=AQGwcg_x6a1JB5Y%3A8%3A1641554647&jazoest=21930&body=999&send=%E5%82%B3%E9%80%81&tids=cid.c.100003609124739%3A100076970858707&wwwupp=C3&ids%5B100003609124739%5D=100003609124739&referrer=&ctype=&cver=legacy&csid=057ee8c8-5ee1-4b45-8807-201b2f799798'
	res = reqp(url, cookie, body)
	print(res)



def send_like(to, cookie):
	base = 'https://mbasic.facebook.com'
	u = 'https://mbasic.facebook.com/messages/read/?fbid=' + to
	res = req(u, cookie)
	url, body = get_payload(res)
	body['like'] = "讚"
	print(body)
	print(url)
	#body='fb_dtsg=AQGwcg_x6a1JB5Y%3A8%3A1641554647&jazoest=21930&body=999&send=%E5%82%B3%E9%80%81&tids=cid.c.100003609124739%3A100076970858707&wwwupp=C3&ids%5B100003609124739%5D=100003609124739&referrer=&ctype=&cver=legacy&csid=057ee8c8-5ee1-4b45-8807-201b2f799798'
	res = reqp(url, cookie, body)
	print(res)



def send_stk(to, sticker, cookie):
	base = 'https://mbasic.facebook.com'
	u = 'https://mbasic.facebook.com/messages/read/?fbid=' + to
	res = req(u, cookie)
	url, body = get_payload(res)
	body['sticker_id'] = sticker
	print(body)
	print(url)
	#body='fb_dtsg=AQGwcg_x6a1JB5Y%3A8%3A1641554647&jazoest=21930&body=999&send=%E5%82%B3%E9%80%81&tids=cid.c.100003609124739%3A100076970858707&wwwupp=C3&ids%5B100003609124739%5D=100003609124739&referrer=&ctype=&cver=legacy&csid=057ee8c8-5ee1-4b45-8807-201b2f799798'
	res = reqp(url, cookie, body)
	print(res)



def send_img(to, img, cookie):
	base = 'https://mbasic.facebook.com'
	u = 'https://mbasic.facebook.com/messages/read/?fbid=' + to
	res = req(u, cookie)
	url, body = get_payload(res)
	body["send_photo"] = "新增相片"
	#print(body)

	url = 'https://mbasic.facebook.com/messages/photo/?%s=%s&%s=%s&%s=%s'%('ids', to, 'tids[0]', body['tids'], 'cancel', u)
	print(body)
	print(url)
	res = reqp(url, cookie, body)
	print(res)
	url, body = get_img_payload(res)
	print(url)
	print(body)	
	res = req_img(url, cookie, body, img)
	print(res)






url = "https://mbasic.facebook.com/groups/143704482352660"
url = '	/home.php?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7'
img = 'C:\\Users\\User\\Pictures\\funny\\photo.php.jpg'


cookie = load_cookie("cookie.txt")
print(cookie)
send_img('100000852003681', img, cookie)
#send_img('100003609124739', img, cookie)
#send_stk('100000852003681', '144885185685748', cookie) # sky
#send_like('100000852003681', cookie) # sky
#send_msg('100000852003681', '不告訴你~~', cookie) # sky
#send_msg('100003609124739', '吃飯啦', cookie)

'''
res = req(url, cookie)

with open('skyyyy.html', 'wb') as f:
	f.write(res.content)
'''

