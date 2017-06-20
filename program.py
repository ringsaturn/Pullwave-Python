#!/usr/bin/python
import requests

from pullwave_class import Pullwave

def pullword(string, debug = 1, bias = 0):
	url = 'http://api.pullword.com/get.php?source='+string+'&param1='+str(debug)+'&param2='+str(bias)
	resp = requests.get(url) 
	words = resp.text
	words = words.split()
	return words
	
def multiselect():
	pass

def ask2input():
	print("请输入要查询的句子")
	string = input()
	word = pullword(string)
	response = None
	a = word
	print("请从一下选择词汇")
	print(a)
	while response not in a:
		response = input("Please enter yes or no: ")
	
	
k = ask2input()
"""	
import sys
if len(sys.argv) <= 3:
	if len(sys.argv) == 3:
		word1 = str(sys.argv[1])
		word2 = str(sys.argv[2])
		Pullwave(word1, word2).pplot()
	else:
		word1 = sys.argv[1]
		word2 = ''
		Pullwave(word1, word2).pplot()
else:
	print('输入参数过多，最多输入两个词，用空格隔开')
"""