# coding=utf-8

import requests
import time
import json

def pullwave(word):
	date = time.strftime("%Y-%m-%d", time.localtime())
	url = 'http://www.pullwave.com/get.php?json=1&auth_usr=free_vip&w1='+str(word)+'&w2=&end_date='+str(date)
	resp = requests.get(url)
	data_json = resp.text
	return data_json

def pplot(word):
	data_raw = pullwave(word)
	data_dic = json.loads(data_raw)
	d = data_dic
	qushi = data_dic['qushi']

	x= len(qushi)*['']
	y = len(qushi)*['']

	for i, v in enumerate(qushi):
		x[i] = v['date']
		y[i] = v['v']

	from datetime import datetime
	x = [datetime.strptime(i, '%Y-%m-%d') for i in x]
	y = [float(i) for i in y]

	#import matplotlib
	#matplotlib.use('Agg')

	import matplotlib.pyplot as plt

	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus']=False
	#plt.rcParams['font.sans-serif']# = ['Hiragino Sans GB']

	plt.bar(x, y)
	plt.xlabel(u'年-月-日')
	plt.ylabel(u'讨论量')
	plt.title(u' %s 在社交网络上的讨论量趋势图' %word)
	plt.show()
	#plt.savefig('/Users/[username]/Desktop/%s.png' %word,dpi = 720)
	return x, y

#word = input("要查询的词汇： ") 
word = '微信'
x, y = pplot(word)
