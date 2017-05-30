# [Pullwave](http://www.pullwave.com) 的 简单可视化 Python 实现

![](一带一路.png)

## 依赖

1. 对于 macOS 内置的 python2 ，无需安装任何模块。
2. 对于自行安装的 python3，`matplotlib`, `requests`
3. pro 需要结巴分词 `jieba` - 2017-05-30

## 用法

* Alfred: 直接下载 [Alfred Workflow](https://raw.githubusercontent.com/ringsaturn/Pullwave-Python/master/Pullwave.alfredworkflow)，并安装。输入关键词 `pw`，再输入词语，最多两个，用空格隔开即可。
* python2 version: Alfred Workflo 代码
* pullwave-pro ：直接运行程序，会提示输入 词语，然后会绘制柱状图。会提示是否使用微博高级搜索功能（代码复用自 [Devonthink-Chinese-Seach](https://github.com/ringsaturn/DEVONthink-Chinese-Search) 项目）
* pullwave-class: 利用 API 绘图的关键模块，参考


## TODO

- [x] 支持多词检索 `2017-05-24 完成`
- [x] 改进横坐标轴显示方式 `2017-05-15 完成`
- [x] 改进绘制图像的显示 `2017-05-15 完成`
- [x] 增加保存图片的功能 `2017-05-24 完成`
- [ ] 争取做个比官网更强大的 GUI 程序出来 `2017-05-30 部分完成，利用了 Alfred 的交互方式`
- [ ] 增加检测峰值点
- [x] 利用 Weibo 高级搜索检索尝试检索相关新闻事件。`2017-05-18 完成`
- [ ] 优化微博搜索方式，能抓取微博正文

感谢 [Pullwave](http://www.pullwave.com) 提供的接口，让我可以直接得到感兴趣的词的趋势。

## 备注
* 为了加快程序启动速度，部分模块一直到使用时才 `import`
* 之所以增加搜索功能，是因为如用Pullwave检索`ios`时，在4月20日有一个峰值。在微博中高级搜索很容易得知是苹果让微信关闭文章打赏功能
