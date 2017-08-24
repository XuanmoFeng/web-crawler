# web-crawler
西*邮电教务网，方正教务网成绩爬虫

利用python语言抓取教务网成绩

抓包工具：CHrome自带的抓包工具

原理：

1.抓包工具抓包看需要提交哪些数据

2.将所要提交的数据，进行下面的字典排序

3.排序完成后将数据传送给后台

4.在此过程中，验证码的处理，即转换成文字，是一件难事

5.验证码利用机器学习，切割，去噪点，然后比对，得出数据

6.期间用一个session打开，访问其他网页时，防止冲突

7.利用一个session打开成绩所在的网页，

8.正则表达式提取出成绩，

9.将成绩分装成joson，提供给其他Api用

10.将学生的账号和密码保存在数据库里，记录下来，比如和我们的微信id绑定时，进行更快的查询

ps：

也可以利用，百度里的echarts库，对成绩进行图表化，将成绩进行分析，然后发送给用户，这样看起来非常的美观。

*****************************************

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
![image](https://github.com/XuanmoFeng/web-crawler/blob/master/IMG_20170824_210352.jpg?raw=true)
![image](https://github.com/XuanmoFeng/web-crawler/blob/master/IMG_20170708_174701.jpg?raw=true)
