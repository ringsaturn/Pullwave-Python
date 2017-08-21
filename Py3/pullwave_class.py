# coding=utf-8

# [Pullwave](pullwave.com) Python3 SDK
# by ringsaturn
# ringsaturn.me@gmail.com
# 2017-08

# 3rd moudles
# requests + matplotlib

"""
# [Pullwave:关键词在社交网络的讨论量查询服务](http://www.pullwave.com/)

## 网站介绍
Pullwave是为金融、投资人士和社会学研究人士提供的趋势分析工具，数据主要来自社交媒体。
Pullwave展现的数据自由引用，无需授权，对数据有疑问和进一步商业合作请联系梁斌（新浪微博@梁斌penny)。

## 使用简介
可以查询一个词，也可以查询两个词。
查询一个词的时候，关键词2置空即可。
查询两个词表示同一篇社交讨论中同时提到这两个词的文章总量，看做是讨论量。
同一篇文章出现多次关键词，只计算一次，因此可以看做是关键词或者关键词对的文档频率
英文请输入全小写，例如查询CEO，请输入ceo进行查询

## API调用方法
在查询语句中增加json=1，必须作为第一个参数加入，例如：http://www.pullwave.com/get.php?json=1&auth_usr=free_vip&w1=%E9%98%B4%E9%98%B3%E5%B8%88&w2=&end_date=2016-12-27

## 使用限制
本产品基础服务部分永久免费
每天独立IP查询次数超过1000次需要发邮件（bayoukeji@gmail.com）报备，报备不收费，登记个IP即可，否则可能会永久封禁IP
看一个月及其以上数据趋势只提供给内部大客户使用，购买请联系梁斌的微博账号 @梁斌penny 谢谢。
"""

import requests
import time
from datetime import datetime
import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

class Pullwave(object):
	def __init__(self, Word1, Word2 = ''):
		self.Word1 = Word1.lower()
		self.Word2 = Word2.lower()
		self.x = None
		self.y = None
		
	def pullwave(self):
		Date = time.strftime("%Y-%m-%d", time.localtime())
		URL = 'http://www.pullwave.com/get.php?json=1&auth_usr=free_vip&w1='+ str(self.Word1) + '&w2='+ str(self.Word2) + '&end_date='+ Date
		
		data_str = requests.get(URL).text
		
		# 调试数据 debug data
		# 调试时注释掉上面	 data_str = requests.get(URL).text
		# 把下面的 #data_str 去掉 #
		#data_str = """{"qushi":[{"date":"2017-07-20","v":"882"},{"date":"2017-07-21","v":"582"},{"date":"2017-07-22","v":"616"},{"date":"2017-07-23","v":"487"},{"date":"2017-07-24","v":"566"},{"date":"2017-07-25","v":"634"},{"date":"2017-07-26","v":"701"},{"date":"2017-07-27","v":"607"},{"date":"2017-07-28","v":"565"},{"date":"2017-07-29","v":"507"},{"date":"2017-07-30","v":"565"},{"date":"2017-07-31","v":"391"},{"date":"2017-08-01","v":"501"},{"date":"2017-08-02","v":"788"},{"date":"2017-08-03","v":"634"},{"date":"2017-08-04","v":"549"},{"date":"2017-08-05","v":"673"},{"date":"2017-08-06","v":"1617"},{"date":"2017-08-07","v":"867"},{"date":"2017-08-08","v":"2894"},{"date":"2017-08-09","v":"1368"},{"date":"2017-08-10","v":"528"},{"date":"2017-08-11","v":"747"},{"date":"2017-08-12","v":"607"},{"date":"2017-08-13","v":"662"},{"date":"2017-08-14","v":"444"},{"date":"2017-08-15","v":"507"},{"date":"2017-08-16","v":"562"},{"date":"2017-08-17","v":"527"},{"date":"2017-08-18","v":"747"}]}"""
		
		return json.loads(data_str)['qushi']
	
	def data(self):
		qushi = self.pullwave()
		
		def parse(qushi_item, method):
			return qushi_item[method]
			
		self.x  = [parse(qushi_item, 'date') for qushi_item in qushi]	
		self.y  = [parse(qushi_item, 'v') for qushi_item in qushi]	
		return self.x, self.y
	
	# 用于生成 plt 的原始数据
	# plot(), plotSaver() 共用这部分代码
	def pltGen(self):
		self.x, self.y = self.data()
		
		# 需要把 x,y  数据转换成 matplotlib 能识别的数据格式
		x_plot = [datetime.strptime(i, '%Y-%m-%d') for i in self.x]
		y_plot = [float(i) for i in self.y]
		plt.bar(x_plot, y_plot)
		plt.xlabel(u'年-月-日')
		plt.ylabel(u'讨论量')
		plt.title(u' %s %s 在社交网络上的讨论量趋势图' %(self.Word1, self.Word2))
		return plt
				
	def plot(self):
		self.pltGen().show()
		return self.x, self.y
			
	def plotSaver(self):
		plt = self.pltGen()
		if self.Word2 == '':
			plt.savefig('%s.png' %(self.Word1),dpi = 720)
		else:
			plt.savefig('%s-%s.png' %(self.Word1, self.Word2),dpi = 720)
		return plt


# 用法

# 支持双词查询，第二个默认留空

# 返回 json 数据
# [{'date': '2017-07-20', 'v': '882'}, {'date': '2017-07-21', 'v': '582'}, {'date': '2017-07-22', 'v': '616'}, {'date': '2017-07-23', 'v': '487'}, {'date': '2017-07-24', 'v': '566'}, {'date': '2017-07-25', 'v': '634'}, {'date': '2017-07-26', 'v': '701'}, {'date': '2017-07-27', 'v': '607'},......]
"""
data_json = Pullwave('python').pullwave()
print(data_json)
"""
# 返回数据列表 
#		-> x: 	YYYY-MM-dd 
#					['2017-07-20', '2017-07-21', '2017-07-22', '2017-07-23', ......]
#		-> y: 12345 
#					['882', '582', '616', '487', ......]						
"""
x, y = Pullwave('python').data()
print(x,y)
"""

# 绘制图像（依旧返回数据列表）
"""
x, y = Pullwave('python').plot()
print(x, y)
"""
# 保存图像
# 返回 <module 'matplotlib.pyplot' ......>
"""
plt = Pullwave('python').plotSaver()
"""