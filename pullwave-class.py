# coding=utf-8
import requests
import time
import json

class Pullwave(object):

	def __init__(self, word1, word2):
		self.word1 = word1
		self.word2 = word2

	def get_data(self):
		date = time.strftime("%Y-%m-%d", time.localtime())
		url = 'http://www.pullwave.com/get.php?json=1&auth_usr=free_vip&w1='+str(self.word1)+'&w2='+str(self.word2)+'&end_date='+str(date)
		resp = requests.get(url)
		data_json = resp.text
		return data_json

	def pplot(self):
		data_raw = self.get_data()
		data_dic = json.loads(data_raw)
		d = data_dic

		qushi = data_dic['qushi']

		x = len(qushi)*['']
		y = len(qushi)*['']

		for i, v in enumerate(qushi):
			x[i] = v['date']
			y[i] = v['v']

		from datetime import datetime
		x = [datetime.strptime(i, '%Y-%m-%d') for i in x]
		y = [float(i) for i in y]

		# 用于保存图片
		#import matplotlib
		#matplotlib.use('Agg')

		import matplotlib.pyplot as plt

		plt.rcParams['font.sans-serif'] = ['SimHei']

		plt.bar(x, y)
		plt.xlabel(u'年-月-日')
		plt.ylabel(u'讨论量')
		# "%s %s" % ('hello', 'world')
		plt.title(u' %s %s 在社交网络上的讨论量趋势图' %(self.word1, self.word2))
		plt.show()
		#plt.savefig('/Users/[username]/Desktop/%s.png' %word,dpi = 720)
		return x, y

import sys
if len(sys.argv) <= 3:
	if len(sys.argv) == 3:
		word1 = sys.argv[1]
		word2 = sys.argv[2]
		Pullwave(word1, word2).pplot()
	else:
		word1 = sys.argv[1]
		word2 = ''
		Pullwave(word1, word2).pplot()
else:
	print('输入参数过多，最多输入两个词，用空格隔开')
