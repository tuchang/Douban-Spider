 Douban-Spider
=====================
这是一只使用Python3编写的简易的豆瓣爬虫
-----------

### 简介：

* 使用[Requests](http://www.python-requests.org/en/master/)模拟HTTP请求/响应，[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)提取页面信息。

* ~~PIL库中的Image方法来获取验证码，且需要人工验证。~~
* 依照知乎上@笑虎的方法[随机生成Cookie](https://zhuanlan.zhihu.com/p/24035574)
* 用json文件存储数据。
* 该爬虫参考了一些大佬的代码！
* 还需要代理
## 环境依赖
* BeautifulSoup4
* Requests
* ~~Pillow~~

## 安装
``` shell
$ git clone https://github.com/cirno99/Douban-Spider.git
$ cd Douban-Spider
$ pip install -r requirements.txt
```
## 使用说明
* 先在代码中调用"login函数"生成名为cookie的pickle文件

* 注释login函数后，添加全局代理

例：
``` shell
export HTTPS_PROXY="https://60.182.238.242:35535"
```
* 再调用"getMovies_1函数"进行爬取
``` shell
$ python3 DoubanSpider.py
```
如果调用login函数报错，请删除文件夹里的cookie再登入！
