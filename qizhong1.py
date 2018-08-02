import requests,re,threading

def get_piclist(pagenum=1):
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'%(pagenum)
    result = requests.get(url)
    data = result.text
    #print(data)
    pic = re.findall(r'img src="(//\S+)" alt="糗事',data)
    #print(pic)
    for x in pic:
        tx = threading.Thread(target=get_pic,args=(x,),name=x)
        tx.start()

def get_pic(i):
    url_pic = 'https:' + i
    #print(i)
    picname = re.findall(r'/(\w+\.\w+)$',i)[0]
    #print(picname)
    try:
        picb = requests.get(url_pic).content
        with open(picname,'wb') as f:
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
    ti = threading.Thread(target=get_piclist,args=(i,),name=i)
    ti.start()
    
