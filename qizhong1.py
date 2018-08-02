import requests,re,threading

def get_pic(pagenum=1):

    url = 'https://www.qiushibaike.com/imgrank/page/%d/'%(pagenum)
    result = requests.get(url)
    data = result.text
    #print(data)
    pic = re.findall(r'img src="(//\S+)" alt="糗事',data)
    #print(pic)
    for i in pic:
        url_pic = 'https:' + i
        #print(i)
        picname = re.findall(r'/(\w+\.\w+)$',i)[0]
        #print(picname)
        try:
            with open(picname,'wb') as f:
                picb = requests.get(url_pic).content
                f.write(picb)
            print('%s 下载成功'% picname)
        except:
            print('%s 下载失败'% picname)

print('请输入起始页：',end='')
stapage = int(input())
print('请输入终止页：',end='')
endpage = int(input())
print('开始下载')
for i in range(stapage,endpage+1):
    tx = threading.Thread(target=get_pic,args=(i,))
    tx.start()

