import requests
#from bs4 import BeautifulSoup
#from os import remove
#from PIL import Image
import pickle
import json
import random
import string
#import http.cookiejar as cookielib
Session=requests.session()
"""
url = 'https://www.douban.com/'
login_url='https://www.douban.com/login'
data={
		'source':None,
		'remember':'on'
		}

headers = {
			'Host':'www.douban.com',
			'Referer': 'https://www.douban.com/',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding':'gzip, deflate, br'
			}

# 读取是否保存有cookie

try:
	with open('cookie','rb') as f:
		Session.cookies=pickle.load(f)
		#这里我将读到的cookie输出
#        print(Session.cookies)
		log = True
# 如果没有cookie，就读入用户输入
except:
	data['form_email']=input('请输入你的账户：')
	data['form_password']=input('请输入你的密码：')
	log = False

# 获得登陆界面的验证码
def get_captcha():
	req=Session.get(login_url)
	page_bf=BeautifulSoup(req.text,'html.parser')
	# 寻找验证码的图片（有可能不需要验证码 这时返回NULL）
	try:
		img_src=page_bf.find('img',id='captcha_image').get('src')
	except:
		return 'NULL','NULL'
	# 如果需要验证码下载该验证码并打开
	img=requests.get(img_src)
	if img.status_code==200:
		with open('captcha.jpg','wb') as f:
			f.write(img.content)
	image=Image.open('captcha.jpg')
	image.show()
	# 让用户根据验证码图片输入验证码
	captcha=input('请输入验证码：')
	remove('captcha.jpg')
	# 由于post-data里还要求captcha-id所以我从图片网址中截取id
	captcha_id=img_src[img_src.find('=')+1:]
	captcha_id=captcha_id[:captcha_id.find('&')]
	return captcha,captcha_id

def login():
	#获得验证码和验证码id
	if not log:
		captcha,captcha_id=get_captcha()
		if captcha!='NULL':
			data['captcha-solution']=captcha
			data['captcha-id']=captcha_id
			# 进行登陆
		page_login=Session.post(login_url,data=data,headers=headers)
		# 为了验证是否登陆成功我将登陆返回的页面html打印出来发现登陆失败
		#print(page_login.text)
	else:
		page_login=Session.get(url,headers=headers)
	page_login_bf=BeautifulSoup(page_login.text,'html.parser')
	# 如果登陆打印登录账号
	name=page_login_bf.find_all('a',class_='bn-more')
	print(name[0].text)
"""

	
def random_bid():
	cookie_name = 'bid'
	#随机bid
	cookie_value =  "".join(random.sample(string.ascii_letters + string.digits, 11))
	Session.cookies.clear()
	c = requests.cookies.RequestsCookieJar()  
	c.set(cookie_name, cookie_value, path='/', domain='.douban.com',)
	Session.cookies.update(c)
	print(set(Session.cookies))
		# 将此时的cookie保存方便下次登陆
	with open('cookie', 'wb') as f:
		pickle.dump(Session.cookies,f)
""""

def getMovies():
	#获取标签
	tags = []
	tags_url = 'https://movie.douban.com/j/search_tags?type=tv'
	tag_re = requests.get(tags_url,cookies=Session.cookies).json()
	tags = tag_re['tags']

	#获取详情页
	for tag in tags:
		i = 0
		j = 0
		movies = []
		#不返回空时继续爬取
		while True:
			detail_url = 'https://movie.douban.com/j/search_subjects?type=tv&tag='+ tag +'&sort=recommend&page_limit=20&page_start={}'.format(str(i))
			details = requests.get(detail_url,cookies = Session.cookies).json()		
			result = details['subjects']
			for item in result:
				movies.append(item)
			if len(details['subjects']) == 0:
				random_bid()
				break
			i += 20
		with open('./'+tag+'.json','w') as m:
			json.dump(movies, m)
"""

def getMovies_1():
	tag = input("输入爬取的分类：[电影|电视剧|综艺|动画|短片|纪录片]\n")
	i = 0
	movies = []
	#不返回空时继续爬取
	while True:
		detail_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags='+tag+'&start={}'.format(str(i))
		details = requests.get(detail_url, cookies = Session.cookies).json()		
		
		result = details['data']
		for item in result:
			movies.append(item)
		
		if len(details['data']) == 0:
			random_bid()
			break
		i += 20
		print(len(movies))
	with open('./'+tag+'.json','w') as m:
		json.dump(movies, m)
	
	#	print(details)
#random_bid()
if __name__=='__main__':
#	login()
#	getMovies_1()
	random_bid()

