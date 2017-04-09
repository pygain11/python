#从网络上获取网页内容
#getHTMLText()

#提取网页内容信息到合适的数据结构
#fillUnivList()

#利用数据结构展示并输出结果
#printUnivList()
#使用二维列表
#匹配中文字符串[\u4e00-\u9fa5]
#ip (([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])
import bs4
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:	
		return "error"
	return
def fillUnivList(ulist,html):
	soup=BeautifulSoup(html,"html.parser")
	for tr in soup.tbody.children:#NeigitivalTage
		if isinstance(tr, bs4.element.Tag):#判断是否为Tag
			tds=tr('td')#检索TR下的TD标签
			#三类信息装入列表
			ulist.append([tds[0].string,tds[1].string,tds[3].string])
def printUnivList(ulist,num):
	tplt="{:^10}\t{:^6}\t{:^10}"
	print(tplt.format("排名","学校名称","分数"))#使用中文字符填充

	for i in range(num):
		u=ulist[i]
		print(tplt.format(u[0],u[1],u[2]))
		# print(u[0],u[1],u[2]
def main():
	uinfo=[]
	url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
	html=getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,30)

if __name__ == '__main__':
	main()