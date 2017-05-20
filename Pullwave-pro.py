# coding=utf-8
import requests
import time
import json

class Pullwave(object):

	def __init__(self, word):
		self.word = word

	def get_data(self):
		date = time.strftime("%Y-%m-%d", time.localtime())
		url = 'http://www.pullwave.com/get.php?json=1&auth_usr=free_vip&w1='+str(self.word)+'&w2=&end_date='+str(date)
		resp = requests.get(url)
		data_json = resp.text
		return data_json

	def pplot(self):
		data_raw = self.get_data()
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

		# 用于保存图片
		#import matplotlib
		#matplotlib.use('Agg')

		import matplotlib.pyplot as plt

		plt.rcParams['font.sans-serif'] = ['SimHei']

		plt.bar(x, y)
		plt.xlabel(u'年-月-日')
		plt.ylabel(u'讨论量')
		plt.title(u' %s 在社交网络上的讨论量趋势图' %self.word)
		plt.show()
		#plt.savefig('/Users/[username]/Desktop/%s.png' %word,dpi = 720)
		return x, y

def find_in_weibo(word, start_date, end_date):
	s = requests.session()
	#date = time.strftime("%Y-%m-%d", time.localtime())
	url = 'http://s.weibo.com/weibo/'+str(word)+'&xsort=hot&suball=1&timescope=custom:'+str(start_date)+':'+str(end_date)
	headers = {'User-Agent': 'MMozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30'}
	search = s.get(url,headers=headers)
	search.encoding = 'utf-8'
	search_as_bytes = str.encode(search.text)
	u = search_as_bytes.decode('unicode_escape')

	import re
	import jieba.analyse

	def cut(content, method=1):
		if method == 0:
			import thulac
			thu1 = thulac.thulac(seg_only=True,filt=True)
			words = thu1.cut(content, text=True)
		else:
			words = content
		return words

	def filter_chinese(text):
		r = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\：\。\，\“\“\_\-\”\▃\？\、\/n\─\;\'\,\[\]\.\<\>\/\?\~\"\《\》\）\\\（\\！\@\#\\\&\*\%]", "", text)
		r = r.replace(' ', '')
		p=re.compile('\s+')
		r=re.sub(p,'',r)
		return r

	def get_key_words(content):
		content = filter_chinese(content)
		text_length = len(content)
		words_num_max = int(text_length/2)
		words = cut(content,method=1)
		keywords = jieba.analyse.extract_tags(words, topK=words_num_max, withWeight=True, allowPOS=( ))
		final_keywords = filter_keywords(keywords)
		final_keywords = str(final_keywords).replace('\'','')
		final_keywords = str(final_keywords).replace('[','')
		final_keywords = str(final_keywords).replace(']','')
		return final_keywords

	def filter_keywords(keywords):
		final_keywords = []
		loop_times = len(keywords)
		count = 0
		bias = 0
		for words in keywords:
			if count+4 <= len(keywords)/2:
				k = -(keywords[count+4][1]-words[1])/3
				if k < 0.01:
					bias = words[1]
					break
			count = count + 4
		for item in keywords:
			if item[1]>bias:
				final_keywords.append(item[0])
		return final_keywords

	u = filter_chinese(u)
	#from pyquery import PyQuery
	#u = PyQuery(u)
	u = get_key_words(u)
	return u

if __name__ == '__main__':
	word = input('要查询的词汇： ')
	a = Pullwave(word).pplot()

	logic = input('是否微博搜索当天关键词 y/n  ')
	if logic == 'y':
		start_date = input('起始日期： ')
		end_date = input('截止日期： ')
		return_words = find_in_weibo(word, start_date, end_date)
		print(return_words)
