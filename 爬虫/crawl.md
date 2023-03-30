# 爬虫

## 一.基础

### 1/HTTP协议

- Hypertext Transfer Protocol
  - 超文本传输协议
- HTTP是一个基于"请求与响应"模式的,无状态的应用层协议
- URL格式
  - http://host:port/path/
- HTTP协议对资源的操作
  - GET
  - HEAD
  - POST
  - PUT
  - PATCH
  - DELETE

### 2/Robots协议

- 爬虫限制协议
- robots.txt
  - User-agent
  - disallow

## 二.Requests库

### 1/Response对象

#### 1.属性

| 属性              | 说明                                            |
| ----------------- | ----------------------------------------------- |
| status_code       | HTTP请求的返回状态,三位数字表示,200表示成功.... |
| text              | HTTP相应内容的字符串形式,即,url对应的页面内容   |
| encoding          | 从HTTP header中猜测的响应内容编码方式           |
| apparent_encoding | 从内容中分析出的响应内容编码方式(备选编码方式)  |
| content           | HTTP响应内容的二进制形式                        |

#### 2.方法

| 方法               | 说明                                |
| ------------------ | ----------------------------------- |
| raise_for_status() | 如果状态码不是200,产生异常HTTPError |

### 2/Request

#### 1.主要方法

| 方法               | 说明                                    |
| ------------------ | --------------------------------------- |
| requests.request() | 构造一个请求,支撑一下各种方法的基础方法 |
| requests.get()     | GET                                     |
| requests.head()    | HEAD                                    |
| requests.post()    | POST                                    |
| requests.put()     | PUT                                     |
| requests.patch()   | PATCH                                   |
| requests.delete()  | DELETE                                  |

#### 2.request()

- 参数
  - method
  - url
  - **kwargs
    - params
      - 类型:字典或字节序列
      - 作为参数增加到url中
    - data
      - 类型:字典,字节序列或文件对象
      - Request中的内容
    - json
      - 类型:JSON格式的数据(字典)
      - Request中的内容
    - header
      - 类型:字典
      - Request-header
    - cookies
      - 类型:字典或CookieJar
      - cookie
    - auth
      - 类型:元祖
      - HTTP认证功能
    - files
      - 类型:字典
      - 传输文件
    - timeout
      - 类型:数字
      - 超时时间,单位为秒
    - proxies
      - 类型:字典
      - 设定访问代理服务器,可以增加登录认证
    - allow_redirects
      - 类型:布尔值
      - 重定向开关,默认为True
    - stream
      - 类型:布尔值
      - 获取内容立即下载开关,默认为True
    - verify
      - 类型:布尔值
      - 认证SSL证书开关,默认True
    - cert
      - 本地SSL证书路径

### 3/异常

| 异常                      | 说明                                      |
| ------------------------- | ----------------------------------------- |
| requests.ConnectionError  | 网络连接错误异常,如DNS查询失败,拒绝链接等 |
| requests.HTTPError        | HTTP错误异常                              |
| requests.URLRequired      | URL缺失异常                               |
| requests.TooManyRedirects | 超过最大重定向次数,产生重定向异常         |
| requests.ConnectTimeout   | 连接远程服务器超时异常                    |
| requests.Timeout          | 请求URL超时,产生超时异常                  |



### 4/实例

- 设置headers,params
- 下载并储存至本地

```python
import requests

# params
# ?keyword=ddd&enc=utf-8&wq=ddd&pvid=e2577d5466f547338c242cb370300eb1
params = {
    "keyword": "ddd",
    "enc": "utf-8",
    "wq": "ddd",
    "pvid": "e2577d5466f547338c242cb370300eb1",
}

r = requests.get("https://search.jd.com/Search", headers={"user-agent": "Mozilla/5.0"}, params=params)

with open("jd.html", "wb")as f:
    f.write(r.content)
print(r.request.headers)
print(r.status_code)
```

### 5/

## 三.BeautifulSoup

demo页面:https://python123.io/ws/demo.html

### 1/基础

- 安装

```
pip install beautifulsoap4
```

- 导入

```python
from bs4 import BeautifulSoup
```

- demo

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>P标签</p>", "html.parser")
# prettify()
print(soup.prettify())
```

### 2/BS库解析器

| 解析器           | 使用方法                         | 条件                 |
| ---------------- | -------------------------------- | -------------------- |
| bs4的HTML解析器  | BeautifulSoup(mk, "html.parser") | 安装bs4库            |
| lxml的HTML解析器 | BeautifulSoup(mk, "lxml")        | pip install lxml     |
| lxml的XML解析器  | BeautifulSoup(mk, "xml")         | pip install lxml     |
| html5lib的解析器 | BeautifulSoup(mk, "html5lib")    | pip install html5lib |

### 3/基本元素

| 基本元素        | 说明                                         |
| --------------- | -------------------------------------------- |
| Tag             | 标签,最基本的信息组织单元                    |
| Name            | 标签的名字, 格式: <tag>.name                 |
| Attributes      | 标签的属性, 格式: <tag>.attrs                |
| NavigableString | 标签内的非属性字符串,格式 <tag>.string       |
| Comment         | 标签内字符串的注释部分,一种特殊的Comment类型 |

### 4/HTML内容遍历

- 下行遍历

| 属性         | 说明                                                  |
| ------------ | ----------------------------------------------------- |
| .contents    | 子节点的列表,将<tag>所有儿子节点存入列表              |
| .children    | 子节点的迭代类型,与.contents类似,用于循环遍历儿子节点 |
| .descendants | 子孙节点的迭代类型,包含所有子孙节点,用于循环遍历      |

- 上行遍历

| 属性     | 说明                                        |
| -------- | ------------------------------------------- |
| .parent  | 节点的父亲标签                              |
| .parents | 节点先辈标签的迭代类型,用于循环遍历先辈节点 |

- 平行遍历
  - 发生在同一个父节点下的各节点间

| 属性               | 说明                                                |
| ------------------ | --------------------------------------------------- |
| .next_sibling      | 返回按照HTML文本顺序的下一个平行节点标签            |
| .previous_sibling  | 返回按照HTML文本顺序的上一个平行节点标签            |
| .next_siblings     | 迭代类型,返回按照HTML文本顺序的后续所有平行节点标签 |
| .previous_siblings | 迭代类型,返回按照HTML文本顺序的前续所有平行节点标签 |

### 5/信息标记

#### 1.HTML/XML

- <name></name>
- <name />
- <!-- -->

#### 2.JSON

- {"key": "value"}
- {"key": ["value1", "value2"]}
- {"key": {"key": "value"}}

#### 3.YAML

```YAML
key: value
key: #comment
-value1
-value2
key:
	subkey: subvalue
```

#### 4.三种信息标记的比较

- XML
  - 最早的通用信息标记语言,可扩展性好,但繁琐
  - Internet上的信息交互与传递
- JSON
  - 信息有类型,适合程序处理,较XML简洁
  - 移动应用云端和节点的信息通信,无注释
- YAML
  - 信息无类型,文本信息比例最高,可读性好
  - 各类系统的配置文件,有注释易读

### 6/信息提取

- 方法一
  
- 完整解析信息的标记形式,再提取关键信息
  
- 方法二
  
- 无视标记形式,直接搜索关键信息
  
- bs4内容提取方法

  - soup.find_all(name,attrs,recursive,string,**kwargs)

    - 返回一个列表类型,存储查找的结果
    - name:对标签名称的检索字符串
    - attr:对标签属性值的检索字符串,可标注属性检索
    - recursive:是否对子孙全部检索,默认为True
    - string:<>....</>中字符串区域的检索字符串

  - 其他方法

    | 方法                     | 说明                                                      |
    | ------------------------ | --------------------------------------------------------- |
    | find()                   | 搜索且只返回一个结果,字符串类型,同.find_all()参数         |
    | find_parents()           | 在先辈节点中搜索,返回列表类型.find_all()参数              |
    | find_parent()            | 在先辈节点中只返回一个结果,字符串类型,同.find_all()参数   |
    | find_next_siblings()     | 在后续平行节点中搜索,列表类型,同.find_all()参数           |
    | find_next_sibling()      | 在后续平行节点中返回一个结果,字符串类型,同.find_all()参数 |
    | find_previous_siblings() | 在前续平行节点中搜索,列表类型,同.find_all()参数           |
    | find_previous_sibling()  | 在前续平行节点中返回一个结果,字符串类型,同.find_all()参数 |

### 7/实例

