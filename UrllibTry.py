import urllib.request
import urllib.parse

file = urllib.request.urlopen('https://www.baidu.com')#记住写网站要加http的
data = file.read()
fhandle=open("./1.html","wb")# ./应当是本地的意思,应该和下面的绝对路径是一样的
#handle=open("C:\\#格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
fhandle.write(data)
fhandle.close()
url = "https://www.baidu.com"

url2 = "https//www.sdu.edu.cn/"
