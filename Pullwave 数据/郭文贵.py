data_dic = {
	"qushi" : [
		{
			"date" : "2017-05-02",
			"v" : "5"
		},
		{
			"date" : "2017-05-03",
			"v" : "5"
		},
		{
			"date" : "2017-05-04",
			"v" : "38"
		},
		{
			"date" : "2017-05-05",
			"v" : "5"
		},
		{
			"date" : "2017-05-06",
			"v" : "5"
		},
		{
			"date" : "2017-05-07",
			"v" : "45"
		},
		{
			"date" : "2017-05-08",
			"v" : "37"
		},
		{
			"date" : "2017-05-09",
			"v" : "5"
		},
		{
			"date" : "2017-05-10",
			"v" : "5"
		},
		{
			"date" : "2017-05-11",
			"v" : "5"
		},
		{
			"date" : "2017-05-12",
			"v" : "5"
		},
		{
			"date" : "2017-05-13",
			"v" : "5"
		},
		{
			"date" : "2017-05-14",
			"v" : "38"
		},
		{
			"date" : "2017-05-15",
			"v" : "5"
		},
		{
			"date" : "2017-05-16",
			"v" : "5"
		},
		{
			"date" : "2017-05-17",
			"v" : "5"
		},
		{
			"date" : "2017-05-18",
			"v" : "5"
		},
		{
			"date" : "2017-05-19",
			"v" : "5"
		},
		{
			"date" : "2017-05-20",
			"v" : "27"
		},
		{
			"date" : "2017-05-21",
			"v" : "22"
		},
		{
			"date" : "2017-05-22",
			"v" : "1203"
		},
		{
			"date" : "2017-05-24",
			"v" : "357"
		},
		{
			"date" : "2017-05-25",
			"v" : "563"
		},
		{
			"date" : "2017-05-26",
			"v" : "238"
		},
		{
			"date" : "2017-05-27",
			"v" : "138"
		},
		{
			"date" : "2017-05-28",
			"v" : "78"
		},
		{
			"date" : "2017-05-29",
			"v" : "61"
		},
		{
			"date" : "2017-05-30",
			"v" : "98"
		}
	]
}

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
plt.title(u'郭文贵 在社交网络上的讨论量趋势图')
plt.show()
#return x, y

