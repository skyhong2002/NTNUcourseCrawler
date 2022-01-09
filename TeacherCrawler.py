# encoding:utf-8
import requests
from time import sleep
import random
import webbrowser
import os

## author: c0xffee, skyhong2002


url = 'https://courseap2.itc.ntnu.edu.tw/acadmOpenCourse/CofopdlCtrl?'

def req(u):
	s = requests.Session()
	s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',})
	res = s.get(u)
	return res


'''
def notify_ending(chat_id, message, pic):
    
	with open('bot_token', 'r') as f:
		token = f.read()
        
	bot = telegram.Bot(token=token)
	for chat_id in chat_ids:
		#bot.sendMessage(chat_id=chat_id, text=message)#, photo='https://cryptor.at/128/4a6e198afb9fdfab0483d02e3e22d53ce7a02644b6df02cfb4de117e9f002f26.png')
		bot.send_photo(chat_id, pic, caption=mes)'''

deptCode = ['GU 通識', 'CU 共同科', 'EU 師培學院', 'PE 普通體育', 'VS 全人中心', '9UAA 校際學士班(臺大)', '9MAA 校際碩士班(臺大)', '9DAA 校際博士班(臺大)', '9UAB 校際學士班(臺科大)', '9MAB 校際碩士班(臺科大)', 'E 教育學院', 'EU00 教育系', 'EM00 教育碩', 'ED00 教育博', 'EU01 心輔系', 'EM01 心輔碩', 'ED01 心輔博', 'EU02 社教系', 'EM02 社教碩', 'ED02 社教博', 'EU05 衛教系', 'EM05 衛教碩', 'ED05 衛教博', 'EU06 人發系', 'EM06 人發碩', 'ED06 人發博', 'EU07 公領系', 'EM07 公領碩', 'ED07 公領博', 'EM08 資訊碩', 'ED08 資訊博', 'EU09 特教系', 'EM09 特教碩', 'ED09 特教博', 'EU11 學習科學學位學程', 'EM15 圖資碩', 'ED15 圖資博', 'EM16 教政碩', 'EM17 復諮碩', 'EU13 教院不分系', 'EM03 課教碩', 'ED03 課教博', 'L 文學院', 'LU20 國文系', 'LM20 國文碩', 'LU21 英語系', 'LM21 英語碩', 'LD21 英語博', 'LU22 歷史系', 'LM22 歷史碩', 'LU23 地理系', 'LM23 地理碩', 'LD23 地理博', 'LM25 翻譯碩', 'LU26 臺文系', 'LM26 臺文碩', 'LM27 臺史碩', 'SU40 數學系', 'SM40 數學碩', 'SU41 物理系', 'SM41 物理碩', 'SU42 化學系', 'SM42 化學碩', 'SD42 化學博', 'SU43 生科系', 'SM43 生科碩', 'SD43 生科博', 'SU44 地科系', 'SM44 地科碩', 'SD44 地科博', 'SM45 科教碩', 'SD45 科教博', 'SM46 環教碩', 'SD46 環教博', 'SU47 資工系', 'SM47 資工碩', 'SD50 生物多樣學位學程', 'SU51 營養科學學位學程', 'SM51 營養碩', 'SM52 生醫碩', 'T 藝術學院', 'TU60 美術系', 'TM60 美術碩', 'TD60 美術博', 'TM67 藝史碩', 'TU68 設計系', 'TM68 設計碩', 'TD68 設計博', 'H 科技學院', 'HU70 工教系', 'HM70 工教碩', 'HD70 工教博', 'HU71 科技系', 'HM71 科技碩', 'HD71 科技博', 'HU72 圖傳系', 'HM72 圖傳碩', 'HU73 機電系', 'HM73 機電碩', 'HD73 機電博', 'HU75 電機系', 'HM75 電機碩', 'HU76 車能學位學程', 'HU77 光電工程學位學程', 'HM77 光電碩', 'A 運休學院', 'AU30 體育系', 'AM30 體育碩', 'AD30 體育博', 'AM31 休旅碩', 'AD31 休旅博', 'AU32 競技系', 'AM32 競技碩', 'IM82 歐文碩', 'IU83 東亞系', 'IM83 東亞碩', 'ID83 東亞博', 'IU84 華語系', 'IM84 華語碩', 'IM86 人資碩', 'IM88 大傳碩', 'IM89 社工碩', 'MU90 音樂系', 'MM90 音樂碩', 'MD90 音樂博', 'MM91 民音碩', 'MU92 表演學位學程', 'MM92 表演碩', 'O 管理學院', 'OM55 管理碩', 'OM56 全營碩', 'OU57 企管系', 'ZU56 國際外交學程', 'ZU59 音樂輔教學程', 'ZU60 音樂科技學程', 'ZU61 天文重力學程', 'ZU62 理工實作學程', 'ZU63 科技藝術學程', 'ZU64 知識轉譯學程', 'ZU65 中英翻譯學程', 'ZU66 戶外探索領導學程', 'ZU67 科學計算學程', 'ZU68 太陽能源與工程學程', 'ZU69 文物保存修復學分學程', 'ZU71 學習與資訊學程', 'ZU72 數位人文與藝術學程', 'ZU73 運動傷害防護學程', 'ZU74 國際教師學程-華語文', 'ZU75 國際教師學程-數學', 'ZU76 國際教師學程-物理', 'ZU77 資訊科技應用學程', 'ZU78 人工智慧技術與應用學', 'ZU79 PASSION偏鄉教育學程', 'ZU83 基礎管理學程', 'ZU84 財金學程', 'ZU89 環境監測學程', 'ZU92 榮譽英語學程', 'ZU93 歐洲文化學程', 'ZU94 文學創作學程', 'ZU97 日語學程', 'ZU98 高齡學程', 'ZU9A 區域學程', 'ZU9B 空間學程', 'ZU9C 學校心理學學程', 'ZU9E 社會與傳播學程', 'ZU9K 大數據學程', 'ZU9O 室內設計學程', 'ZU9P 韓語學程', 'ZU9Q 社團領導學程', 'ZU9U 原民教育學程', 'ZU9V 大師創業學程', 'ZU9W 金牌書院', 'ZU9X 哲學學程', 'ZU9Y 藝術產業學程', 'ZU9Z 國際教師學程-國際']
dir = 'teachers'
teachers = {}
temp = []
c = 0
for dCode in deptCode:
	c += 1
	print('######### %d #########'%c)
	post_url = url + '_dc=1641709974859&acadmYear=110&acadmTerm=2&chn=&engTeach=N&moocs=N&remoteCourse=N&digital=N&adsl=N&zuDept=&classCode=&kind=&generalCore=&teacher=&serial_number=&course_code=&language=chinese&action=showGrid&start=0&limit=99999&page=1&deptCode=' + dCode.split(' ')[0]
	res = req(post_url)
	j = res.json()
	tmp = [i['teacher'] for i in j["List"]]
	tmp = list(set(tmp))
	teachers[dCode] = tmp
	temp += tmp
	print(dCode)
	print(url)
	print(tmp)
	
	with open(dir + os.sep + dCode.replace(' ', '_') + '.txt', 'w', encoding='utf-8') as f:
		f.write('\n'.join(tmp))

	
	'''data = proc(res)
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


	delay = random.randint(5, 25)
	print('waiting for %d seconds'%delay)
	sleep(delay)

	delay = random.randint(500, 1200)
	print('long sleep for %d seconds'%delay)
	sleep(delay)
	'''
print(teachers)
with open(dir + os.sep + 'all_teachers.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(temp))
