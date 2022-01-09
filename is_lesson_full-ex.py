import requests
from time import sleep
import random
import webbrowser
import os

## author: c0xffee


cookie = input('cookie:')
code = input('lesson_code:')

url = 'https://cos3s.ntnu.edu.tw/AasEnrollStudent/CourseQueryCtrl?action=showGrid&_dc=1632452672757'

def req(u, code, cookie):
	s = requests.Session()
	s.headers.update({'Host':'cos3s.ntnu.edu.tw',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
                      'Accept':'*/*',
                      'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                      'Accept-Encoding':'gzip, deflate, br',
                      'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                      'X-Requested-With':'XMLHttpRequest',
                      'Content-Length':'1904',
                      'Origin':'https://cos3s.ntnu.edu.tw',
                      'Connection':'keep-alive',
                      'Referer':'https://cos3s.ntnu.edu.tw/AasEnrollStudent/CourseQueryCtrl?action=add',
                      'Cookie':cookie,
                      'Sec-Fetch-Dest':'empty',
                      'Sec-Fetch-Mode':'cors',
                      'Sec-Fetch-Site':'same-origin'})
	data = "serialNo=%s&chnName=&teacher=&deptCode=&formS=&class1=&generalCore=&notFull=0&courseCode=&validQuery=&checkWkSection10=0&checkWkSection11=0&checkWkSection12=0&checkWkSection13=0&checkWkSection14=0&checkWkSection15=0&checkWkSection16=0&checkWkSection17=0&checkWkSection18=0&checkWkSection19=0&checkWkSection110=0&checkWkSection111=0&checkWkSection112=0&checkWkSection113=0&checkWkSection114=0&checkWkSection20=0&checkWkSection21=0&checkWkSection22=0&checkWkSection23=0&checkWkSection24=0&checkWkSection25=0&checkWkSection26=0&checkWkSection27=0&checkWkSection28=0&checkWkSection29=0&checkWkSection210=0&checkWkSection211=0&checkWkSection212=0&checkWkSection213=0&checkWkSection214=0&checkWkSection30=0&checkWkSection31=0&checkWkSection32=0&checkWkSection33=0&checkWkSection34=0&checkWkSection35=0&checkWkSection36=0&checkWkSection37=0&checkWkSection38=0&checkWkSection39=0&checkWkSection310=0&checkWkSection311=0&checkWkSection312=0&checkWkSection313=0&checkWkSection314=0&checkWkSection40=0&checkWkSection41=0&checkWkSection42=0&checkWkSection43=0&checkWkSection44=0&checkWkSection45=0&checkWkSection46=0&checkWkSection47=0&checkWkSection48=0&checkWkSection49=0&checkWkSection410=0&checkWkSection411=0&checkWkSection412=0&checkWkSection413=0&checkWkSection414=0&checkWkSection50=0&checkWkSection51=0&checkWkSection52=0&checkWkSection53=0&checkWkSection54=0&checkWkSection55=0&checkWkSection56=0&checkWkSection57=0&checkWkSection58=0&checkWkSection59=0&checkWkSection510=0&checkWkSection511=0&checkWkSection512=0&checkWkSection513=0&checkWkSection514=0&checkWkSection60=0&checkWkSection61=0&checkWkSection62=0&checkWkSection63=0&checkWkSection64=0&checkWkSection65=0&checkWkSection66=0&checkWkSection67=0&checkWkSection68=0&checkWkSection69=0&checkWkSection610=0&checkWkSection611=0&checkWkSection612=0&checkWkSection613=0&checkWkSection614=0&action=showGrid&actionButton=add&page=1&start=0&limit=999999"
	data = data%code
	res = s.post(u, data=data)
	return res


def proc(res):
	j           = res.json()
	lesson_name = j['List'][0]['v_chn_name']
	total_num   = j['List'][0]['limitCountH']
	is_it_full  = j['List'][0]['v_is_Full']

	return [lesson_name, total_num, is_it_full]


def ringing(n):  
	for i in range(n):
		print('\x07')
		sleep(1)


def notify_ending(chat_id, message, pic):
    
	with open('bot_token', 'r') as f:
		token = f.read()
        
	bot = telegram.Bot(token=token)
	for chat_id in chat_ids:
		#bot.sendMessage(chat_id=chat_id, text=message)#, photo='https://cryptor.at/128/4a6e198afb9fdfab0483d02e3e22d53ce7a02644b6df02cfb4de117e9f002f26.png')
		bot.send_photo(chat_id, pic, caption=mes)


c = 0
while True:
	flag = 0
	failed = 0
	for i in range(120):
		c += 1
		print('######### %d #########'%c)
		try:
			res = req(url, code, cookie)
			if "不合法執行選課系統" in res.text:
				print("ERROR: plz relogin into NTNU Enrollment System and copy the new cookie again")
				webbrowser.open('https://cos3s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl')
				failed = 1

			data = proc(res)
			schema = ['Lesson\t', 'Total_limit', 'is_it_full']
			for i in range(len(data)):
				print(schema[i]+"\t: "+str(data[i]))


			if data[-1] != '1':
				print('GOGOGOGOGOGOGOGOGOGOGOGOGOGOGOGGOGOGOGO\n'*10)
				webbrowser.open('https://cos3s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl')
				ringing(10)
				#notify_ending(978681917, 'https://cos3s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW', 'https://cryptor.at/128/4a6e198afb9fdfab0483d02e3e22d53ce7a02644b6df02cfb4de117e9f002f26.png')
				flag = 1
				break


		except Exception as e:
			print(e)


		if failed == 1:
			exit()


		delay = random.randint(5, 25)
		print('waiting for %d seconds'%delay)
		sleep(delay)


	if flag == 1:
		break

	delay = random.randint(500, 1200)
	print('long sleep for %d seconds'%delay)
	sleep(delay)
