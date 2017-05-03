# web-crawler
西*邮电教务网，方正教务网成绩爬虫

import urllib
import os
import re
import requests
import sys

from collections import OrderedDict    
***************这个库处理form表单里的数据时用的*****
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
直接使用字典的话，在进行字符串转化时，参数就会乱序，而使用这个就会依次转化，不会乱序
要建立一次session,因为那样的的cookie访问一次，
进入了教务网，自己就可以编写自己想要的模块来实现自己想要的模板
