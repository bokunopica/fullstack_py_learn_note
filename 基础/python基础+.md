# 1Python基础+

## 一.面向对象 OOP

### 1/部分内置函数

```python
# dir 查看对象内的所有属性和方法
class Object:
    def __init__(self):
        self.name = "a"
obj = Object()
print(dir(obj))

# id 查看内存地址
print(id(obj))

# python是内存地址引用传递
obj1 = Object()
obj2 = Object()
obj3 = obj2
print(obj1==obj2) # False
print(obj2==obj3) # True

# __del__ 对象结束生命周期时调用
# __str__ 调用print()时打印出来的string
class Object1:
    def __init__(self):
    	self.name = "a"
    def __del__(self):
        print("这是__del__")
    def __str__(self):
        print("这是__str__")
# del关键字
obj11 = Object1()
del obj11


```

### 2/身份运算符

```python
# 身份运算符 比较两个对象的内存地址是否一致--是否是对同一个对象的引用
# is / is not
# ==/!= 判断值相等
A = ["str"]
B = A
C = ["str"]
A is B # True
A == B # True
A is C # False
A == C # True
```

### 3/伪私有属性和私有方法

- python中没有真正意义上的私有

```python
class Private:
    def __init__(self):
        self.name = "a"
        self.__password = "ddd"# 私有属性
    def __secret(self):# 私有方法
        print(self.__password)
        
# 外部不能直接访问私有属性和私有方法
a = Private()
print(a.__password) # 报错
print(a.__secret()) # 报错
# 访问需要在私有属性/方法前加上_类名
print(a._Private__password)# 运行成功
print(a._Private__secret())# 运行成功
```

### 4/继承

```python
# 对父类方法进行扩展
# 调用父类方法
# 1.使用super类
# super()就是使用super类创建出来的对象
# super调用顺序按照类.__mro__的元祖排序来
# super使用了c3算法
class Base:
    def test(self):
        print("a")
class Child(Base):
    def test(self):
        print("b")
        # super()完全写法如下:
        # super(Child,self).test()
        super().test()
print(Child().test)# 先打印b再打印a
# 2.使用父类名(不推荐)
# 多继承时可能会导致反复运行该类的某个父类的同一个方法
class Base:
    def test(self):
        print("a")
class Child(Base):
    def test(self):
        print("b")
        Base.test(self)
print(Child().test)# 先打印b再打印a
```

```python
# 多继承
# 多继承可以让子类对象,同时具有多个父类的属性和方法
# 若有相同属性或者方法,会继承自顺序在前的那个父类(尽量不要重复)
class BaseA:
    def test(self):
        print("BaseA-test")
class BaseB:
    def test(self):
        print("BaseB-test")
    def demo(self):
        print("BaseB-demo")
class Child(BaseA,BaseB):
    pass
child = Child()
child.test() # BaseA-test
child.demo() # BaseB-demo

# MRO -- 方法搜索顺序
# 类名.__mro__
Child.__mro__ #(<class '__main__.Child'>, <class '__main__.BaseA'>, <class '__main__.BaseB'>, <class 'object'>)
```

### 5/新式类/旧式(经典)类

- 新式类
  - 以object为基类的类
  - py3.+定义的类都是新式类
- 经典类
  - 不以object为基类的类
  - py2定义时不指定object作为基类,则默认定义经典类
- 方法搜索顺序两者不同!

### 6/多态

- 继承父类
- 重写父类的方法

### 7/类属性/类方法/静态方法

- 实例
  - 利用类创建的对象
  - 实例化
    - 利用类创建对象的过程
  - 实例属性
  - 实例方法
- 类对象
  - 不是实例,是创建实例的类的对象
  - 类属性
    - 类对象的属性
  - 类方法
    - 类对象的方法
- python属性获取机制
  - 向上查找机制

```python
class Tool(object):
    count=0　# 定义类属性
    def __init__(self,name):
        self.name=name
        Tool.count+=1 # 方法内对类对象的操作方法:类名.类对象
    @classmethod # 定义类方法
    def object_num(cls):
        print(cls.count)
    @staticmethod # 定义静态方法
    def demo():
        print("static_method")

# 调用类属性的两种方法
tool1 = Tool("锤子")
tool2 = Tool("镰刀")
tool2.count = 99
# 类名.类属性 直接查找类对象
print(Tool.count) # 2
# 对象.类属性 先查实例再查类对象
print(tool1.count) # 2
print(tool2.count) # 99
```

- 类方法
  - 只调用类属性时使用
- 实例方法
  - 既有实例属性,又有类属性时使用
- 静态方法
  - 既没有实例属性,又没有类属性时使用

### 8/单例设计模式

- 目的

  - 让类创建的对象,在系统中只有**唯一的一个实例**

  - 每一次执行[类名()]返回的对象,**内存地址是相同的**

    

- \__new__

  - 1.为对象分配空间
  - 2.返回对象引用

```python
# __new__
# 非单例
class MusicPlayer(object):
    def __new__(self,*args,**kwargs):
        return super.__new__(cls)
    def __init__(self):
        pass
# 单例 __new__
class MusicPlayer(object):
    
    instance = None
    
    def __new__(self,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super.__new__(cls)
        return instance
    def __init__(self):
        pass
    
# 单例 只执行一次初始化工作 __new__ __init__
class MusicPlayer(object):
    instance = None
    init_flag = False
    def __new__(self,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super.__new__(cls)
        return instance
    def __init__(self):
        if not MusciPlayer.init_flag:
            print("初始化动作")
            MusciPlayer.init_flag = True
```

### 9/魔术方法

| 方法                       | 功能                              |
| -------------------------- | --------------------------------- |
| \__doc__                   | 类的描述信息,三引号内容           |
| \__module__                | 当前操作的对象在哪个模块          |
| \__class__                 | 当前操作的对象的类是什么          |
| \__init__                  | 类初始化方法(构造方法的一环)      |
| \__new__                   | 类分配内存(构造方法的一环)        |
| \__del__                   | 对象在内存中被释放时,自动触发执行 |
| \__call__                  | 对象()--->调用call方法            |
| \__dict__                  | 类或对象中的所有属性              |
| \__str__                   | print(obj)时输出该方法的返回值    |
| getitem,setitem,delitem    | 用于索引操作,如字典               |
| getslice,setslice,delslice | 用于切片操作,如列表               |
| \__mro__                   | 方法搜索顺序                      |
| \__iter__                  | 迭代方法                          |
| \__next__                  | 迭代方法-下一个迭代               |
| \__enter__                 | 上下文管理器实现方法              |
| \__exit__                  | 上下文管理器实现方法              |

### 10/property属性

- 修饰器创建property属性
  - 创建
    - @property
  - 修改
    - @属性名.setter
  - 删除
    - @属性名.deleter

```python
class Goods(object):
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        return self.original_price * self.discount
    
    @price.setter
    def price(self,value):
        self.original_price = value
        
    @price.deleter
    def price(self):
        del self.original_price
        
obj = Goods()
obj.price		# 获取商品价格
obj.price = 200 # 修改商品原价
del obj.price	# 删除商品原价
```

- property()方法
  - 参数1:获取属性的方法
  - 参数2:修改属性的方法
  - 参数3:删除属性的方法
  - 参数4:文档说明

```python
class Foo(object):
    def get_bar(self):
        return 'wang'
    
    def set_bar(self,value)
    	return value
    
    def del_bar(self):
        return 'deleted'
    
    BAR = property(get_bar, set_bar, del_bar, "doc")

obj = Foo()
obj.BAR = 'alex'
desc = Foo.BAR.__doc__
del obj.BAR
```

- property的应用
  - 私有属性添加getter和setter方法

```python
# 装饰器写法
class Money(object):
    def __init__(self):
        self.__money = 0
	
    @property
    def money(self):
        return self.__money
    
    @money.setter(self):
    def money(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print("type error")
    
    @money.deleter(self):
    def money(self):
        del self.__money
        
# property()
class Money(object):
    def __init__(self):
        self.__money = 0
	
    def getMoney(self):
        return self.__money
    
    def setMoney(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print("type error")
    
	money = property(setMoney,getMoney)
        
a = Money()
a.money = 100
print(a.money) # 100
```



## 二.基础+1

### 1/异常捕获

```python
try:
    pass
except 错误类型1:
    pass
except 错误类型2:
    pass
except Exception as e:
    print(e)
else:
    # 没有异常才会执行的代码
    pass
finally:
    # 无论是否有异常,都会执行的代码
    print("无论是否有异常,都会执行的代码")
    
# 正常执行顺序: try->else->finally
# 发生异常执行顺序: try->except->finally
```

- 异常的传递
  - 只需要在主程序中进行异常处理

- 抛出异常
  - Exception 异常类
  - 创建Exception对象
  - raise关键字 抛出异常

```python
# 简单的抛出异常
e = Exception("异常类")
raise e
#
```

### 2/模块&包

#### 模块

- 导入模块
  - import 模块
  - 导入文件时,文件中所有没有任何缩进的代码都会被执行一遍

- 模块搜索顺序
  - 1.搜索当前目录指定模块名的文件,如果有就直接导入
  - 2.如果没有,再搜索系统目录
- 模块命名
  - 不要和系统的模块文件重名,否则系统模块失效
- 内置属性
  - \__file__
  - \__name__
  - \__main__

```python
# __file__
import random
print(random.__file__)
# __name__
print(__name__) # __main__
print(random.__name__)# random
# __main__
if __name__ == "__main__":
    print("main")
```

- 模块开发格式

```python
# 导入模块
# 定义全局变量
# 定义类
# 定义函数

# 代码最下方
def main():
    # ...
    pass

if __name__ == "__main__":
    main()
```

#### 包

- 概念
  - 包含多个模块的特殊附录
  - 有\__init__.py
  - 报名的命名方式和变量名一直,小写字母+_
  - 导入当前目录下的模块
    - from . import xxxxx

#### 发布

- 创建setup.py

```python
from distutils.core import setup

setup(name="package_name",
      version="1.0",
      description="描述信息",
      long_description="完整描述信息",
      author="作者",
      author_email="xxxx@xx.com",
      url="www.homepage.com",
      py_modules=["package_name.module_1",
                 "package_name.module_2"]
)
```



- 构建模块

```shell
python3 setup.py build
```

- 生成发布压缩包

```shell
python3 setup.py sdist
```

- 安装模块

```shell
tar -zxvf package_name-1.0.tar.gz
sudo python3 setup.py install
```

- 卸载
  - 把包和模块直接删了就行了

### 3/文件

- 文件指针
- 不同读取方法(指针操作不同)
  - read()
  - readline()

```python
# read()会使文件指针移动到文件末尾
# demo.txt
'''
hello world
hello pin
'''
file = open("demo.txt","r")
text = file.read()
print(text) 
# hello world
# hello pin
text = file.read()
print(text)
file.close()
#readline()文件指针移动到下一行,读取该行内容
file = open("demo.txt")
text = file.readline()
print(text)# hello world
text = file.readline()
print(text)# hello pin
```

- 打开文件的方式

| 访问方式 | 说明 |   指针   |
| :------: | :--: | :------: |
|    r     | 只读 | 文件开头 |
|    w     | 只写 |    /     |
|    a     | 追加 | 文件末尾 |
|    r+    | 读写 | 文件开头 |
|    w+    | 读写 |    /     |
|    a+    | 读写 | 文件结尾 |

### 4/os模块

**文件操作**

| 方法名 | 说明       | 示例                             |
| ------ | ---------- | -------------------------------- |
| rename | 重命名文件 | os.remove(源文件路径,目标文件名) |
| remove | 删除文件   | os.remove(源文件路径)            |

**目录操作**

| 方法名     | 说明               | 示例                    |
| ---------- | ------------------ | ----------------------- |
| listdir    | 目录列表           | os.listdir(目录名)      |
| mkdir      | 创建目录           | os.mkdir(目录名)        |
| rmdir      | 删除目录           | os.rmdir(目录名)        |
| getcwd     | 获取当前目录       | os.getcwd()             |
| chdir      | 修改工作目录       | os.chdir(目标目录)      |
| path.isdir | 判断是否是文件目录 | os.path.isdir(文件路径) |

### 5/编码

**ASCII编码**

- py2默认使用

**UNICODE编码**

- py3默认使用
- UTF-8

**python2中使用中文**

```python
# 头部添加下一行代码
# *-* coding:utf8 *-*
# 或者是下一行
# coding=utf8
# 中文前加上u表示utf8编码
text = u"hello 世界"
for letter in text:
    print(letter)

```

### 6/eval函数

```python
# 基本数学计算
print(eval("1+1"))# 2
# 字符串重复
print(eval("'*'*10"))# **********
# 字符串转换成列表
type(eval("[1,2,3,4]"))# list
# 字符串转换成字典
type(eval("{'name':'name'}"))# dict
```

**不要滥用eval**

- 不要用eval直接转换input

- 可以利用eval的输入进行其他操作

- 例如:

```python
# 输入
__import__('os').system('touch aaa')

# 等价代码
import os
os.system('touch aaa')
```

### 7/不可变/可变数据类型

- 不可变
  - 赋值
    - 对变量连续赋予相同的值，变量所指向的内存地址不变。
    - 对变量连续赋予不同的值，变量所指向的内存地址变化。
  - 数字,字符串,元祖
  - 不可变数据类型在第一次声明赋值声明的时候, 会在内存中开辟一块空间, 用来存放这个变量被赋的值, 而这个变量实际上存储的, 并不是被赋予的这个值, 而是存放这个值所在空间的内存地址, 通过这个地址, 变量就可以在内存中取出数据了. 所谓不可变就是说, 我们不能改变这个数据在内存中的值, 所以当我们改变这个变量的赋值时, 只是在内存中重新开辟了一块空间, 将这一条新的数据存放在这一个新的内存地址里, 而原来的那个变量就不在引用原数据的内存地址而转为引用新数据的内存地址了.
- 可变
  - 赋值
    - 对变量连续赋予相同的值，变量所指向的内存地址变化。
    - 对变量连续赋予不同的值，变量所指向的内存地址变化。
  - 列表,字典
  - 可变数据类型是指变量所指向的内存地址处的值是可以被改变的。

### 8/赋值,拷贝

- 赋值
  - 只是创建一个变量,该变量指向原来的内存地址,如下
  - n4 = n3 = n2 = n1 = "string"
- 浅拷贝
  - 在内存中只额外创建第一层数据
  - 下面几层的数据都是引用拷贝的母对象的数据
- 深拷贝
  - 将所有的数据重新创建一份（排除最后一层,python特有优化)

### 9/修改全局变量

- 函数中
  - global
    - 修改对象的内存指向
    - 或者对象是不可变数据类型
  - 不使用global
    - 修改对象内存指向的内容
    - 且对象是可变数据类型

### 10/list操作

| 方法                              | 描述                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| len()                             | 列表元素个数                                                 |
| max()                             | 列表元素最大值                                               |
| min()                             | 最小值                                                       |
| list(seq)                         | 元祖转list                                                   |
| list.append(obj)                  | 尾部添加新对象                                               |
| list.count(obj)                   | obj出现次数                                                  |
| list.extend(seq)                  | 尾部一次追加多个值                                           |
| list.index(obj)                   | 返回第一个=obj的元素的索引值                                 |
| list.pop([index=-1])              | 移除列表一个元素,默认index=-1                                |
| list.remove(obj)                  | 移除=obj的第一个元素                                         |
| list.reverse()                    | 翻转列表                                                     |
| list.sort(key=None,reverse=False) | 列表排序,key指定按什么元素排序,匿名函数可以使得按照元素的多个不同属性排序 |
| list.clear()                      | 清空列表                                                     |
| list.copy()                       | 复制列表                                                     |
| list.insert(index,obj)            | 将对象插入列表                                               |

### 11/dict操作

| 方法                              | 描述                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| len()                             |                                                              |
| str()                             |                                                              |
| type()                            |                                                              |
| dict.clear()                      | 清除元素                                                     |
| dict.copy()                       | 浅复制                                                       |
| dict.fromkeys()                   | 创建一个新字典                                               |
| dict.get(key,default = None)      | 返回指定键的值，如果值不在字典中返回default值                |
| dict.items()                      | 以列表返回可遍历的(键, 值) 元组数组                          |
| dict.keys()                       | 返回一个迭代器，可以使用 list() 来转换为列表                 |
| dict.setdefault(key,default=None) | 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| dict.update(dict2)                | 把字典dict2的键/值对更新到dict里                             |
| dict.values()                     | 返回一个迭代器，可以使用 list() 来转换为列表                 |
| pop(key[,default])                | 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| dict.popitem()                    | 随机返回并删除字典中的最后一对键和值。                       |

### 12/调用其他编程语言

- C
  - 编译成动态库
    - gcc xxx.c -shared -o libxxxx.so
  - python加载动态库
  - 创建子线程执行C语言编写的函数

```python
from ctypes import *
from threading import Thread

# 加载动态库
lib = cdll.LoadLibrary("./libxxx.so")

# 创建子线程,执行C
t = Thread(target = lib.FuncName)
t.start()

# 主线程
while True:
    pass
```

### 13/深浅拷贝

```python
import copy
'''可变类型拷贝'''
# 赋值 (仅仅复制内存指向)
a = [11,22]
b = a
print(id(a)==id(b))# True
# 深拷贝 (完全复制整个内存的对象)
c = copy.deepcopy(a)
print(id(c)==id(a))# False
# 浅拷贝 (只拷贝最外层对象,更里面的对象只复制引用)
d = copy.copy(a)
print(id(d)==id(a))# True
for i in range(len(a)):
    print(id(d[i])==id(a[i]))# True
'''不可变类型拷贝'''
# 浅拷贝 (等于赋值)
# 深拷贝 (如果不可变类型内部有可变类型,则执行深拷贝,否则等于赋值)
'''特殊情况'''
# 切片拷贝
c = [1,2,3,4]
d = c[:] # 浅拷贝
# 字典 copy()方法
e = dict(demokey="demovalue")
f = e.copy()# 浅拷贝
```

### 14/私有化

- xxxx
  - 公有变量
- _xxx
  - 私有化属性或方法
  - from module import * 无法导入
  - 类对象和子类可以访问
- __xxx
  - 类中的私有属性/方法
  - 子类中不会继承
  - 无法在外部直接访问
- \__xx__
  - 魔术方法/属性
  - 子类会继承
- xx_
  - 避免与关键词的冲突

### 15/导入模块

- 搜索模块顺序
  - sys.path
    - 搜索路径列表
    - 从列表头部搜索至列表尾部

- import重复导入
  - 直接import导入模块会检测模块是否重复导入
  - 重载模块
    - from imp import reload
    - reload(moduleName)
- 导入模块的变量
  - 尽量直接导入模块 import module
  - 尽量不要用from方法  from module import xxx

### 16/上下文 with

- 上下文目的
  - 系统资源(文件/数据库连接/socket)结束业务逻辑之后,一定要关闭
- 直接用类实现

```python
class File(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f
    
    def __exit__(self):
        self.f.close()
        
with File("test.txt","w"):
    f.write("hello with")
```

- context manager

```python
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close
    
with my_open("out.txt", 'w') as f:
    f.write("hello context manager")
```

### 17/装饰器

```python
import time

def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(t2-t1)
        return result
    return wrapper

@display_time
def calculate():
    time.sleep(5)
    return "test"
```



## 三.网络编程

### 1/创建socket

- AddressFamily
  - AF_INET
    - Internet进程间通信
  - AF_UNIX
    - 同一台机器进程间通信
- Type
  - 套接字类型
  - SOCK_STREAM
    - 流式套接字(主要用于TCP)
  - SOCK_DGRAM
    - 数据报套接字(主要用于UDP)

```python
import socket
# socket.socket(AddressFamily,Type)
# TCP socket
s_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_tcp.close()
# UDP socket
s_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_udp.close()
```

### 2/udp网络程序

```python
# 发送
from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)
dest_addr = ('192.168.1.2',8080)# 元祖(ip,端口号)
send_data = input("请输入要发送的数据:")
udp_socket.sendto(send_data.encode("utf-8"),dest_addr)
udp_socket.close()

# 接收
from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)
local_addr = ('',7788) # ip一般不写,表示本机的一个任意ip
udp_socket.bind(local_addr) # 绑定ip和端口
recv_data = udp_socket.recvfrom(1024) # 参数值为数据长度
recv_msg = recv_data[0] # recv_data 是个元祖,进行拆分处理
send_addr = recv_data[1]
print(str(recv_msg),recv_msg.decode("utf-8"))
# windows默认编码gbk
```

- sudo dhclient
  - ubuntu重新分配ip命令

### 3/tcp网络程序

**tcp客户端**

```python
from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)
dest_addr = ('192.168.1.2',8080)# 元祖(ip,端口号)
tcp_socket.connect(dest_addr)# 三次握手创建连接

send_data = input("请输入要发送的数据:")
tcp_socket.send(send_data.encode("utf-8"))
tcp_socket.close()
```

**tcp服务端**

```python
from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)# 监听套接字

tcp_socket.listen(128)# 转换模式为listen

client_socket,client_addr = tcp_socekt.accept()
recv_data = client_socket.recv(1024)# 建立与客户端稳定的连接套接字
print(recv_data)
client_socket.send("ok".encode("utf-8"),client_addr)

client_socket.close()
tcp_socket.close()
```

### 4/案例:文件下载器

**客户端**

- 1.创建套接字
- 2.获取服务器ip,port
- 3.连接服务器
- 4.获取下载的文件名字
- 5.将文件名字发送到服务器
- 6.接收文件中的数据
- 7.保存接收到的数据到一个文件中
- 8.关闭套接字

**服务端**

- 1.创建套接字
- 2.绑定服务器ip,port
- 3.监听
- 4.接收客户端连接
- 5.获取客户端传输的文件名
- 6.找到该文件,传输回客户端
- 7.关闭套接字

### 5/非堵塞

```python
from socket import *
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 非堵塞
tcp_server.setblocking(False)
```



## 四.多任务(线程/进程/协程)

- 并行
  - 真的多任务
- 并发
  - 任务数>cpu核心数目,存在并发
  - 假的多任务

### 1/线程

- 线程执行不分顺序
- 主/子线程共享全局变量

```python
import threading
import time

def test():
    print("a")
# 创建线程对象实例(函数方法)
t_func = threading.Thread(target=test,args=(arg1,))
# 创建线程并执行线程
t_func.start()
# 查看当前线程
threading.enumerate()


# 创建线程对象实例(类方法)
# 继承Thread类,需要重写run方法
class MyThread(threading.Thread):
    def run(self):
        print("类方法运行线程")

t_class = MyThread()
t_class.start()
```

### 2/线程同步

#### 1.互斥锁

```python
import threading
# 创建锁
mutex = threading.Lock()
# 锁定
mutex.acquire()
# 释放
mutex.release()
```

#### 2.死锁

- 多个锁互相冲突导致程序无法运行
- 解决方法:
  - 设计时尽量避免
  - 添加线程锁超时时间

### 3/进程

- 创建的子进程拥有主进程所有的内容
  - 子进程不复制主进程的代码,复制其他所有主进程的对象/内存
  - 存在浪费(计算资源/存储空间)的缺点
  - 写时拷贝
    - 如果子进程通过特殊手段修改了代码,则拷贝一份主进程的代码

```python
import multiprocessing

def test():
    print("test")
# 创建进程对象
p1 = multiprocessing.Process(target=test)
# 创建进程并运行
p1.start()
```

### 4/进程和线程的区别

- 进程
  - 例如:一台电脑运行多个QQ
  - 一个进程中至少有一个主线程
  - 进程之间资源独立
  - 执行过程中拥有独立的内存单元,而多个线程共享内存,从而极大地提高了程序的运行效率
  - 优缺点:执行开销大,但是利于资源的管理和保护
- 线程
  - 例如:一个QQ中的多个聊天窗口
  - 有进程才能有线程,线程依赖于进程
  - 同一个进程中的线程共享资源
  - 线程的划分尺度小于进程,使得多线程程序的并发性高
  - 优缺点:执行开销小,但是不利于资源的管理和保护

### 5/进程间通信

- 网络
  - socket套接字
    - TCP
    - UDP
- 硬盘
  - 文件
- 内存
  - Queue

**Queue**

```python
from multiprocessing import Queue
# 创建队列对象
q = Queue(3)# 长度为3的队列
q.put("消息1")
q.put("消息2")
print(q.full()) # False
q.put("消息3")
print(q.full()) # True

# 推荐:先判断消息队列是否已满,再写入
if note q.full():
    q.put("msg")
# 推荐:先判断消息队列是否不为空,再读取
if note q.empty():
	q.get()
    
# 不会阻塞的读取写入方法
q.put_nowait("msg")
q.get_nowait()
```

```python
import multiprocessing
# 进程池创建queue
queue = multiprocessing.Manager().Queue()
pool = multiprocessing.Pool(3)

def test(queue):
    pass

for i in range(100):
    pool.apply_async(test, args=(queue,))
```



### 6/进程池Pool

```python
from multiprocessing import Pool

def worker(msg):
    print(msg[0],msg[1])
# 创建进程池对象
po = Pool()
# 向进程池添加进程
for i in range(0,10):
    # 每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(worker,args=("a","b"))

# 关闭进程池,不再接受新的请求
po.close()
# 等待po中所有的子进程执行完成,必须放在close方法之后
# 不调用join方法主进程会向下运行执行完直接挂掉
po.join()
```

### 7/迭代器

- 用处
  - 减少内存空间,实现循环

- 优点
  - 占用内存空间小

```python
# 迭代语句
for temp in xxxx_obj:
	pass
```

- 迭代语句流程:
  - 1.判断xxxx_obj是否可以迭代
    - isinstance(obj,Iterable)
  - 2.在第一步成立的前提下,调用iter函数得到xxxx_obj对象的\__iter__方法的返回值
  - 3.\__iter__方法的返回值是一个迭代器



```python
# 创建迭代对象(分两个对象完成)
from collections import Iterable
from collections import Iterator

class Classmate(object):
    def __init__(self):
        self.names = list()
    
    def add(self,name):
        self.names.append(name)
        
    def __iter__(self):
        return ClassIterator()
    

class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.current_num = 0
    
    def __iter__(self):
        pass
    
    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add("老王")
classmate.add("张三")
classmate.add("李四")

print(isinstance(classmate,Iterable))# True
classmate_iterator = iter(classmate)
print(isinstance(classmate_iterator,Iterator))# True

for name in classmate:
    print(name)
```

```python
# 创建迭代对象
from collections import Iterable
from collections import Iterator

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0
    
    def add(self,name):
        self.names.append(name)
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("张三")
classmate.add("李四")

for name in classmate:
    print(name)
```

- python2的range和xrange区别
  - range直接存储生成列表
    - 返回列表
  - xrange存储生成列表的方法
    - 返回迭代器

```python
# 迭代器实现斐波那契数列
class Fibonacci(object):
    def __init__(self, max_len):
        self.max_len = max_len
        self.a = 0
        self.b = 1
        self.current_num = 0
        self.fibonacci_list = list()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.max_len:
            self.current_num += 1
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            return ret
        else:
            self.current_num = 0
            self.a = 0
            self.b = 1
            raise StopIteration
```

### 8/生成器

- 功能:
  - 可以暂停函数内代码的执行
  - 可以向外生成数据
  - 可以接收外部数据

- generator:是一种特殊的迭代器

- 创建生成器

```python
# 1-元祖推导式
G = (x for x in range(10))
print(G)# <generator object <genexpr> at 0x000001FE9AA5E5C8>
# 2-yield
def g_fibonacci(num):
    a, b = 0, 1
    i = 0
    while i < num: 
        yield a
    	a, b = b, a+b
        i += 1

# 如果函数内有yield,则调用函数时实际上是创建生成器对象
b = g_fibonacci(10)
print(b)# <generator object g_fibonacci at 0x000002242192F648>
for num in b:
      print(num)
```

- 使用send唤醒生成器

```python
# send函数最好不要在第一次迭代时使用,使用的话参数传None
def g_fibonacci(num):
    a, b = 0, 1
    i = 0
    while i < num: 
        ret = yield a
        print("ret>>>",ret)
    	a, b = b, a+b
        i += 1

obj = g_fibonacci(10)
ret = next(obj)
print(ret) # 0

ret = obj.send(None)# ret>>> None
print(ret) # 1
```

### 9/协程

- 调用任务像调函数
- 资源消耗最小

- greenlet

```python
from greenlet import greenlet
import time

def test1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.5)
        
        
def test2():
    while True:
        print("---B---")
        gr1.switch()
        time.sleep(0.5)     

        
gr1 = greenlet(test1)
gr2 = greenlet(test2)
```

- gevent(主要使用)
  - 遇到延时操作会切换执行

```python
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent,i)
        gevent.sleep(0.5)

g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)	
g3 = gevent.spawn(f,5)

g1.join()
g2.join()
g3.join()

# 另一种join写法
gevent.joinall([
    gevent.spawn(f,5),
    gevent.spawn(f,5),
    gevent.spawn(f,5),
])
```

### 10/GIL 全局解释器锁

- 概念
  - CPython解释器的问题
  - 每个线程在执行的过程中都需要先获取GIL,保证同一个时刻只有一个线程可以执行代码
- 不同类型程序的影响
  - 网络程序
    - 网络收发数据,会有大量延时
    - 没啥影响
  - 计算密集型
    - 疯狂计算, 无延时
    - 用线程会降低cpu运算效率
    - 推荐使用多进程
  - IO密集型
    - 存储介质读写
    - 读写速度远远低于cpu计算速度,会有大量延时
    - 可以使用多线程/协程
- 解决方法
  - 换解释器
  - 换编程语言(多线程运行其他的编程语言)



## 五.正则表达式

### 1/示例

```python
import re
result = re.match("itcast","itcast.cn")# 匹配
result.group()# 提取数据
```

### 2/匹配单个字符

| 字符 | 功能                                          |
| ---- | --------------------------------------------- |
| .    | 匹配任意1个字符(除了\n)                       |
| []   | 匹配[]中列举的字符                            |
| \d   | 匹配数字,0-9                                  |
| \D   | 匹配非数字                                    |
| \s   | 匹配空白,即空格,tab键                         |
| \S   | 匹配非空白                                    |
| \w   | 匹配单词字符,a-z,A-Z,0-9,下划线_,任意语言字符 |
| \W   | 匹配非单词字符                                |

```python
import re
re.match(r"[1-36-8]","8")# 匹配部分数字
re.match(r'[a-zA-H]',"A")# 匹配部分字母
```

### 3/匹配多个字符

| 字符  | 功能                                              |
| ----- | ------------------------------------------------- |
| *     | 匹配前一个字符出现0次或者无限次,即可有可无        |
| +     | 匹配前一个字符出现1次或者无限次,即至少1次         |
| ?     | 匹配前一个字符出现1次或者0次,即要么有1次,要么没有 |
| {m}   | 匹配前一个字符出现m次                             |
| {m,n} | 匹配前一个字符出现从m到n次                        |



```python
# {num}
re.match(r"/d{13}","18754134585")# 匹配13位数字
# {min,max}
re.match(r"/d{1,3}","115")# 匹配1-3位数字
# ? 上海电话号码判断
re.match(r"021-?\d{8}","021-12345678")# 成功
re.match(r"021-?\d{8}","02112345678")# 成功
# re.S
str_content = """adfdarf
sadsada
"""
re.match(r".*",str_content).group()# adfdarf
re.match(r".*",str_content,re.S).group()# adfdarf\nsadsada
```



### 4/匹配开头结尾

| 字符 | 功能           |
| ---- | -------------- |
| ^    | 匹配字符串开头 |
| $    | 匹配字符串结尾 |

- 案例

```python
# 判断变量名合法
import re
names = ["name1","_name","2_name","__name__"]
# 开头不为数字,字符/下划线,后面可以有数字
for name in names:
    ret = re.match("[a-zA-Z_]+[a-zA-Z0-9_]*$",name)
    if ret:
        print(name,"is ok")
```

### 5/匹配分组

| 字符        | 功能                             |
| :---------- | -------------------------------- |
| \|          | 匹配左右任意一个表达式           |
| (ab)        | 将括号中字符作为一个分组         |
| \num        | 引用分组num匹配到的字符串        |
| (?P\<name>) | 分组起别名                       |
| (?P=name)   | 引用别名为name分组匹配到的字符串 |

```python
import re
# 判断163邮箱合法
# @前4~20位
email = input("邮箱地址")
ret = re.match(r"([a-zA-Z0-9]{4,20})@(163|126)\.com$","laowang@163.com")# 邮箱中的.需要转义
print(ret.group())# laowang@163.com
print(ret.group(1))# laowang
print(ret.group(2))# 163

# 判断html的h1标签合法
html_h1 = "<h1>waawfeda</h1>"
ret = re.match(r"<(\w*)>.*</\1>",html_h1).group()
print(ret)# 成功

# ?P<name>
html_content = "<body><h1>waawfeda</h1></body>"
ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",html_h1).group()
print(ret)# 成功
ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>",html_h1).group()
print(ret)# 成功
```

### 6/re高级方法

- search
- findall
- sub
- split



```python
import re
#re.search 不从开头匹配 只取第一个
ret = re.search(r"\d+","阅读此书为9999")
ret.group()# 9999
#re.findall 找字符串中所有满足条件的字符串
ret = re.findall(r"\d+","python = 9999, c = 7890, c++ = 12345")
print(ret)# [9999,7890,12345]
#re.sub 替换
ret = re.sub(r"\d+","998","python=997")
print(ret)# python=998
#re.sub 支持函数引用
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret = re.sub(r"\d+",add,"python=997")
print(ret)# python=998
#re.split 切割字符串
ret = re.split(r":| ","name:xiaozhang age:28")
print(ret)# ['name','xiaozhang','age','28']
```

### 7/修饰符

| 修饰符 | 功能                                                         |
| ------ | ------------------------------------------------------------ |
| re.I   | 使匹配对大小写不敏感                                         |
| re.L   | 做本地化识别（locale-aware）匹配                             |
| re.M   | 多行匹配，影响 ^ 和 $                                        |
| re.S   | 使 . 匹配包括换行在内的所有字符                              |
| re.U   | 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.      |
| re.X   | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。 |

## 六.http,web服务器

### 1/http协议

- request
  - request_header
  - request_body

```
GET / HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
```

- response

  - response_header

  ```
  HTTP/1.1 200 OK
  Cache-Control: private
  Connection: keep-alive
  Content-Encoding: gzip
  Content-Type: text/html;charset=utf-8
  Date: Sun, 10 May 2020 09:17:49 GMT
  Expires: Sun, 10 May 2020 09:17:49 GMT
  Server: BWS/1.0
  Vary: Accept-Encoding
  Content-Length: 49
  ```

  - body

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>HTML.BODY</title>
  </head>
  <body>
      <h1>HTML.BODY</h1>
  </body>
  </html>
  ```

- 一个最简单的response

```
HTTP/1.1 200 OK

<h1>HTML_BODY</h1>
```

### 2/关闭连接close()注意点

```python
# 服务器四次挥手/调用close()时立即释放资源
socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
```

### 3/非堵塞

```python
from socket import *
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 非堵塞
tcp_server.setblocking(False)
```

### 4/长连接/短连接

- 短连接
  - 一次HTML请求,并获取数据后,立即断开tcp连接
- 长连接
  - 一次HTML请求,获取数据后,发现还有需要加载的数据,则不立即断开,继续发送HTML请求,全部请求完成之后,断开tcp连接.
- content_length
  - 该response_body的数据长度

### 5/epoll

- 内存映射
  - 将套接字存储内存与系统/应用共享
- 基于事件触发
  - 系统获得了tcp传输的数据后通知应用
  - 比轮询套接字的方式效率提高非常大

### 6/TCP/IP复习

![image-20200512125329135](C:\Users\pyca\AppData\Roaming\Typora\typora-user-images\image-20200512125329135.png)

- arp
  - 存储ip跟mac地址的键值对
  - windows中命令符:arp -a

### 7.http请求的完整过程

- 1.解析域名
- 2.向服务器发送tcp三次握手
- 3.发送http的请求数据以及等待服务器应答
- 4.发送tcp四次挥手



 





















## N.unittest

- 一个unittest例子

```python
# 代码
def add(a,b):
    return a+b

# 创建unittest类
class AddTestCase(unittest.TestCase):
    def setUp(self):
        # 测试初始化调用
        pass

    def tearDown(self):
        # 测试结束调用
        pass

    def test_add(self):
        # 测试函数
        print('add')
        self.assertEqual(3,add(4,5))
        self.assertNotEqual(3, add(4, 2))

if __name__ == "__main__":
    unittest.main()
```



| 断言方法             | 条件          | 说明                                     |
| -------------------- | ------------- | ---------------------------------------- |
| assertEqual(a, b)    | a == b        | 判断 a 和 b 是否相等，相等则通过否则失败 |
| assertNotEqual(a, b) | a != b        | 判断 a 和 b 是否不等，不等则通过相等失败 |
| assertIn(a, b)       | a in b        | b 是否包含 a，包含则通过否则失败         |
| assertNotIn(a, b)    | a not in b    | b 是否不包含 a，包含则失败否则通过       |
| assertTrue(x)        | x is True     | 表达式 x 为 True 则通过，否则失败        |
| assertFalse(x)       | x is False    | 表达式 x 为 False 则通过，否则失败       |
| assertIsNone(x)      | x is None     | x 是否为 None，是则通过，否则失败        |
| assertIsNotNone(x)   | x is not None | x 是否为 None，是则失败，否则通过        |

