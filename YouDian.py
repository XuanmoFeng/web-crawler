 #author: FENGMO
#-*-coding:utf-8-*-
import urllib
import os
import re
import requests
import sys
from collections import OrderedDict
#设置编码
reload(sys)
sys.setdefaultencoding( "utf-8" )
studentnumber = ""#账号
password = ""#密码
s = requests.session()
url = 'http://222.24.19.201/default2.aspx'
response = s.get(url)
__VIEWSTATE = re.findall("name=\"__VIEWSTATE\" value=\"(.*?)\"",response.content)[0]
imgUrl="http://222.24.19.201/CheckCode.aspx"
imgresponse = s.get(imgUrl, stream=True)
image = imgresponse.content
DstDir = os.getcwd()+"/"
print("保存验证码到："+DstDir+"code.jpg"+"\n")
try:
    with open(DstDir+"code.jpg" ,"wb") as jpg:
        jpg.write(image)
except IOError:
    print("IO Error\n")
finally:
    jpg.close()
Xatu.DoPic("code.jpg")
code = raw_input("验证码是：")
RadioButtonList1 = u"学生".encode('gb2312','replace')
data = OrderedDict()
data['__VIEWSTATE']=__VIEWSTATE
data['txtUserName']=studentnumber
data['Textbox1']=""
data['TextBox2']=password
data['txtSecretCode']=code
data['RadioButtonList1']=RadioButtonList1
data['Button1']=""
data['lbLanguage']=""
data['hidPdrs']=""
data['hidsc']=""
data=urllib.urlencode(data);
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'222.24.19.201',
    'Origin':'http://222.24.19.201',
    'Pragma':'no-cache',
    'Referer':'http://222.24.19.201/default2.aspx',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
}
response = s.post(url,data=data,headers=headers)#.deconde('utf-8')
print response.content.decode('gb2312')
