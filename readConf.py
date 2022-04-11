import configparser
import os
import requests


class ReadConf():
    def __init__(self):
        curpath = os.path.dirname(os.path.relpath(__file__))
        #获取配置文件路径
        cfgpath = os.path.join(curpath, "config.ini")

        # 创建管理对象
        self.conf = configparser.ConfigParser()
        # 读ini文件
        self.conf.read(cfgpath, encoding="utf-8")

    def readConf(self,param):
        #获取所有的section
        # sections = self.conf.sections()
        # print(sections)
        #获取某个sections中的所有值,将其转化为字典
        items = dict(self.conf.items(param))
        return items

if __name__ == '__main__':
    test = ReadConf()
    t = test.readConf("section0")   #传入sections的值
    print('取section0下所有值 ',t)
    print(t['key0'])


if __name__ == '__main__':
    # UA伪装:将访问对象伪装为浏览器
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',#此条少了就会"Forbid spider access"
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',#此条少了就会"Forbid spider access"
        'Upgrade-Insecure-Requests': '1'
    }
    # 爬虫主体
    keyword=t['key0']
    current_path = os.path.dirname(__file__) #获取当前目录
    os.mkdir(current_path + '\\' + keyword)  # 新建文件夹
    for num in range(0,1):# 一次请求返回3张图，此处循环1次，爬取 3 张图片
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&z=&ic=0&word='+ keyword +'&face=0&istype=2&nc=1&pn='+str(num*3)+'&rn=3'
        response = requests.get(url=url, headers=headers).json()
        for index in range(len(response['data'])-1):
            print(response['data'][index]['thumbURL'])
            print(num*3+index)
            #从拿到的网址里下载图片
            img_data=requests.get(response['data'][index]['thumbURL']).content
            #存图
            with open(current_path+'\\'+keyword+'\\'+str(num*3+index)+'.jpg','wb',)as fp:
                fp.write(img_data)


