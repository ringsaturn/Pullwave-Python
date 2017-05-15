# coding=utf-8
import requests
import time
import matplotlib.pyplot as plt
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
	xlabel = len(qushi)*['']
	x = range(len(qushi))
	y = len(qushi)*['']
	for i, v in enumerate(qushi):
		xlabel[i] = v['date']
		y[i] = v['v']
	y = [float(i) for i in y]
	plt.bar(range((len(y))), y)
	#plt.plot(x, y)
	plt.show()
	return xlabel, y
	
word = input('要查询的词汇： ')
pplot(word)