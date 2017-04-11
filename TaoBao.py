#淘宝比价定向爬虫
#提交搜索商品请求,循环获取页面
#对于每个页面，提取商品名称和价格
#将信息输出到屏幕上
import requests
import re

def getHTMLText(url):#获取整个页面信息
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return ""
	# print("")
def parsePage(ilt,html):#正则匹配需要的信息
	try:
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		# print(plt)
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		# print(tlt)
		for i in range(len(plt)):
			price=eval(plt[i].split(':')[1])
			# print(price)
			title=eval(tlt[i].split(':')[1])
			# print(title)
			ilt.append([price,title])
			# print(ilt)in
	except:
		print("")
	# print("")
def printGoodList(ilt):#合理的打印出来
	tplt="{:4}\t{:8}\t{:16}"#槽函数
	print(tplt.format("序号","价格","商品名称"))
	count= 0
	for g in ilt:
		count = count +1
		print(tplt.format(count,g[0],g[1]))
	print("")
def main():
	goods="书包"
	depth=1
	infoList=[]
	start_url="https://s.taobao.com/search?q="+goods
	
	for i in range(depth):
		try:
			url=start_url+'&s='+str(44*i)#关于书包页面编号为44倍数
			html=getHTMLText(url)
			# print(html)
			parsePage(infoList,html)
		except:
			# print("error!")
			continue
	printGoodList(infoList)

if __name__ == '__main__':
	main()