# coding=utf-8
import requests
import time
import json

from pullwave_class import Pullwave

import sys
if len(sys.argv) <= 3:
	if len(sys.argv) == 3:
		word1 = str(sys.argv[1])
		word2 = str(sys.argv[2])
		Pullwave(word1, word2).plot()
	else:
		word1 = sys.argv[1]
		word2 = ''
		Pullwave(word1, word2).plot()
else:
	print('输入参数过多，最多输入两个词，用空格隔开')
