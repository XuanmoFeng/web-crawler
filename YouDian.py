#-*-coding:utf-8-*-
import string
import urllib
from bs4 import BeautifulSoup
from lxml import etree
import urllib2
import os
import re
import requests
import sys
import predict
from collections import OrderedDict
#设置编码
reload(sys)
sys.setdefaultencoding( "utf-8" )
#初始参数
def Grade(RE):
    str=r'<span id="xhxm">(.*?)</span>'
    name=re.findall(str,RE.content)
    str=name[0]#.encode('utf8')
    str=str.decode('gb2312')
    user=str.partition('同学')
    print user[0]
    return user[0]

def Str(studentnumber,password):
    s = requests.session()
    url = 'http://222.24.19.201/default2.aspx'        #this is the login page for xupt
    response = s.get(url)
    __VIEWSTATE = re.findall("name=\"__VIEWSTATE\" value=\"(.*?)\"",response.content)[0]
    imgUrl="http://222.24.19.201/CheckCode.aspx?"
    imgresponse = s.get(imgUrl, stream=True)
    image = imgresponse.content
    DstDir = os.getcwd()+"/"
    try:
        with open(DstDir+"code.png" ,"wb") as jpg:
            jpg.write(image)
    except IOError:
        print("IO Error\n")
    finally:
        jpg.close()
    code = predict.verify("code",save=True)
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
    response = s.post(url,data=data,headers=headers)
    userna=Grade(response)
    username= userna.encode('gb2312','replace')
    urlG='http://222.24.19.201/xscjcx.aspx'
    getdata=urllib.urlencode({
        'xh':studentnumber,
        'xm':username,
        'gnmkdm':'N121605'})
    kburl = "http://222.24.19.201/xscjcx.aspx?xh="+studentnumber+"&xm="+username+"&gnmkdm=N121605#"
    headers ={
        "Referer":"http://222.24.19.201/xs_main.aspx?xh=%s"%studentnumber,
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
    }
    headerss ={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encodingi':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'222.24.19.201',
        'Origin':'http://222.24.19.201',
        "Referer":"http://222.24.19.201/xscjcx.aspx?xh="+studentnumber+"&xm="+username+"&gnmkdm=N121605",
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
    }
    response = s.get(kburl,headers=headers)
    html = response.content.decode("gb2312")
    print html
    __VIEWSTATE = re.findall("name=\"__VIEWSTATE\" value=\"(.*?)\"",html)[0] 
    sdata = OrderedDict()
    sdata['__EVENTTARGET']=''
    sdata['__EVENTARGUMENT']=""
    sdata['__VIEWSTATE']=__VIEWSTATE
    sdata['hidLanguage']=""
    sdata['ddlXN']=""
    sdata['ddlXQ']=""
    sdata['ddl_kcxz']=""
    CH = u"历年成绩".encode('gb2312','replace')
    sdata['btn_zcj']=CH
    sdata=urllib.urlencode(sdata);
    str=r'<td>(.*?)</td>'
    resonse = s.post(kburl,sdata,headers=headerss)
    pattern = re.compile(str.encode('gb2312'))
    name=re.findall(pattern,resonse.content)
    j=0
    Mag=userna+'\n'
    m=0
    for i in name:
        i=i.decode('gb2312')
        if i=='&nbsp;':
            j+=1
            if j==3:
                pass
            elif(j==2):
                Mag=Mag+'\n'
        elif i!='':
            j=0
            if  i!='1' and i !='必修课' and i.count('选修课')!=1 and i[0]!='<':
                if i[0]!='2'and i[0]!=' 'and i[0]!='0':
                    if i.count('学院')!=1 and i!='武装部' and i!='体育部'and i!='学工部':
                         str=i[2:]
                         if str.isdigit()!=True:
                            m=m+1
                            if m>10:
                                Mag=Mag+i+':'
    print Mag
    return Mag
