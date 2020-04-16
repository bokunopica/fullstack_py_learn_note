

## Django-Learn

### 一.配置环境

#### 1.需求环境:

系统:ubuntu-18.04-LTS

编程语言:Python3.5

Django:1.11.7

编辑器:pycharm



#### 2.Linux配置Virtualenv

##### 创建虚拟环境

```shell
mkvirtualenv GP1 -p /usr/bin/python3.5
```

##### 退出虚拟环境

```shell
deactivate
```

##### 进入虚拟环境

```shell
workon GP1
```

##### pip安装django

```shell
pip install django==1.11.7
```

##### pip更改国内源安装django

```shell
pip install django==1.11.7 -i https://mirrors.aliyun.com/pypi/simple/
```

### 二.创建HelloDjango项目

#### 创建项目

```shell
workon GP1 # 进入GP1虚拟环境
django-admin startproject HelloDjango # 新建项目
python manage.py startapp App # 创建APP
```

#### 运行项目

```shell
python manage.py runserver
```

### 三.简易HelloDjango项目

#### 1.项目时区更改/中英文更改

HelloDjango.settings.py中的LANGUAGE_CODE和TIME_ZONE

#### 2.简易request/response

urls.py中修改urlpatterns

再在views中添加urlpatterns调用的方法

#### 3.套用template模板构造response

先在App文件夹下创建Templates文件夹,将Templates文件夹设置为模板库

将Html模板放在Templates下

urls.py中修改urlpatterns

再在views中添加urlpatterns调用的方法,views中的方法是用render函数

settings中配置installed_apps的list

#### 4.修改templates模板路径

settings.TEMPLATES.DIRS

```python
[os.path.join(BASE_DIR,'templates')]
```

#### 5.创建主templates库

在项目主文件夹下创建文件夹,并标记为Templates库

然后再如上所示.

#### 6.创建子路由

1.创建一个新的APP

2.在APP中创建urls.urlpatterns以及views内的方法.....

3.在项目主文件夹内的urls.py创建APP关联url项



```python
urlpatterns = [
	url(r'^regex',include('APP.urls')),
]
```

#### 7.数据库增删查改操作

Object Relational Mapping - 对象关系映射

##### 7.1.在setting中注册App

##### 7.2.model中建立Object对象

```python
class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)
```

##### 7.3.迁移(将模型映射到数据库的过程)

```shell
python manage.py makemigrations
python manage.py migrate
```

##### 7.4.编写urls,views

```python
objects.all() # 查全部
objects.get(pk=?) # 根据主键查询
save() # 增/改
delete() # 删除
```

##### 7.5.套用templates生成动态查询页面

studentList.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>studentList</title>
</head>
<body>
<ul>
    {% for student in students %}
    <li>{{ student.s_name }}</li>
    {% endfor %}
</ul>
</body>
</html>
```

views.getAll:

```python
def getAll(request):
    try:
        students = Student.objects.all()
        context = {"students":students}
        return render(request, 'studentList.html',context = context)
    except:
        return HttpResponse('GetInfoFailed')
```

##### 7.6.迁移数据至mysql

###### 安装Mysql

```shell
sudo apt install mysql
sudo mysql_secure_installation
```

###### 配置mysql登录设置

###### 安装Pymysql

Terminal中执行

```
pip install pymysql
```

###### 配置Pymysql

```python
BASE_DIR/项目名称/__init__

import pymysql
pymysql.install_as_MySQLdb()
```

settings修改DATABASES设置

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE':'django.db.backends.mysql',
        'NAME':'GP1HelloDjango',
        'HOST':'localhost',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'123456',
    }
}
```

###### 创建数据库

```mysql
create database GP1HelloDjango charset=utf8;
```

###### 添加Mysql Datasource

在Datasource中Add

###### 执行迁移操作

```shell
python manage.py migrate
```

###### render()调用template方法的另一种写法

```python
def index(request):
    template = loader.get_template("index.html")
    result = template.render()
    return HttpResponse(result)
```

#### 8.级联数据

##### 8.1.创建Object-Grade/Student

Object生成外键关联

```python
property = models.ForeignKey(Object)
```

执行数据迁移

```shell
python manage.py makemigrations
python manage.py migrate
```

编写urls以及在views内定义方法

```python
# views内部方法实例

def getGrade(request):
    student = Student.objects.get(pk=1)
    grade = student.s_grade# 根据外键获得数据
    return HttpResponse(student.s_name+":"+grade.g_name)

def getStudents(request):
    grade = Grade.objects.get(pk=1)
    students = grade.student_set.all()
    context = {"grade":grade.g_name,"students":students}
    return render(request,"three_student_list.html",context=context)
```

### 四.Models

#### 1.定义属性

##### 1.1.概述

​	·django根据属性的类型确定以下信息
​		·当前选择的数据库支持字段的类型
​		·渲染管理表单时使用的默认html控件
​		·在管理站点最低限度的验证

​	·django会为表增加自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后，则django不会再生成默认的主键列

​	·属性命名限制
​		·遵循标识符规则
​		·由于django的查询方式，不允许使用连续的下划线



##### 1.2.库

​	·定义属性时，需要字段类型，字段类型被定义在django.db.models.fields目录下，为了方便使用，被导入到django.db.models中

​	·使用方式
​		·导入from django.db import models
​		·通过models.Field创建字段类型的对象，赋值给属性

##### 1.3.逻辑删除

​	·对于重要数据都做逻辑删除，不做物理删除，实现方法是定义isDelete属性，类型为BooleanField，默认值为False

##### 1.4.字段类型

​	·AutoField
​		·一个根据实际ID自动增长的IntegerField，通常不指定如果不指定，一个主键字段将自动添加到模型中

​	·CharField(max_length=字符长度)
​		·字符串，默认的表单样式是 TextInput

​	·TextField
​		·大文本字段，一般超过4000使用，默认的表单控件是Textarea

​	·IntegerField
​		·整数

​	·DecimalField(max_digits=None, decimal_places=None)
​		·使用python的Decimal实例表示的十进制浮点数
​		·参数说明
​			·DecimalField.max_digits
​				·位数总数
​			·DecimalField.decimal_places
​				·小数点后的数字位数

​	·FloatField
​		·用Python的float实例来表示的浮点数

​	·BooleanField
​		·true/false 字段，此字段的默认表单控制是CheckboxInput

​	·NullBooleanField
​		·支持null、true、false三种值

​	·DateField([auto_now=False, auto_now_add=False])
​		·使用Python的datetime.date实例表示的日期
​		·参数说明
​			·DateField.auto_now
​				·每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false
​			·DateField.auto_now_add
​				·当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false
​		·说明
​			·该字段默认对应的表单控件是一个TextInput. 在管理员站点添加了一个JavaScript写的日历控件，和一个“Today"的快捷按钮，包含了一个额外的invalid_date错误消息键
​		·注意
​			·auto_now_add, auto_now, and default 这些设置是相互排斥的，他们之间的任何组合将会发生错误的结果

​	·TimeField
​		·使用Python的datetime.time实例表示的时间，参数同DateField

​	·DateTimeField
​		·使用Python的datetime.datetime实例表示的日期和时间，参数同DateField

​	·FileField
​		·一个上传文件的字段

​	·ImageField
​		·继承了FileField的所有属性和方法，但对上传的对象进行校验，确保它是个有效的image

##### 1.5.字段选项

​	·概述
​		·通过字段选项，可以实现对字段的约束
​		·在字段对象时通过关键字参数指定

​	·null
​		·如果为True，Django 将空值以NULL 存储到数据库中，默认值是 False

​	·blank
​		·如果为True，则该字段允许为空白，默认值是 False

​	·注意
​		·null是数据库范畴的概念，blank是表单验证证范畴的

​	·db_column
​		·字段的名称，如果未指定，则使用属性的名称

​	·db_index
​		·若值为 True, 则在表中会为此字段创建索引

​	·default
​		·默认值

​	·primary_key
​		·若为 True, 则该字段会成为模型的主键字段

​	·unique
​		·如果为 True, 这个字段在表中必须有唯一值

##### 1.6.关系

​	·分类
​		·ForeignKey：一对多，将字段定义在多的端中
​		·ManyToManyField：多对多，将字段定义在两端中
​		·OneToOneField：一对一，将字段定义在任意一端中

​	·用一访问多
​		·格式
​			·对象.模型类小写_set
​		·示例
​			grade.students_set

​	·用一访问一
​		·格式
​			·对象.模型类小写
​		·示例
​			·grade.students

​	·访问id
​		·格式
​			·对象.属性_id
​		·示例
​			·student.sgrade_id



#### 2.查询集和过滤器

- all() 返回所有数据
- filter() 返回符合条件的数据
- exclude() 过滤掉符合条件的数据
- order_by() 排序
- values() 将数据转换为字典,返回列表

#### 3.返回单个数据

- get() 返回一个满足条件的对象

  如果没有找到符合条件的对象 会引发 模型类.DoesNotExist异常

  如果找到多个,会引发 模型类.MultiObjectsReturned异常

- first() 查询集第一个对象

- last() 查询集最后一个对象

- count() 查询集对象个数

- exists() 判断查询集中是否有数据 返回布尔值

#### 4.切片

- .[n:m] 返回第n到第m个对象 n:offset m:limit n.m不能为负数

#### 5.查询条件

- 属性__运算符=值
- lt 小于
- gt 大于
- gte 大于等于
- lte 小于等于
- in 在某一集合中
- contains 类似于 模糊查询 like
- startswith 以xx开始 类似like
- endswith 以xx结束 类似like
- exact 精确 ==
- isnull,isnotnull 是否为空
- year,month,day,week_day,hour,minute,second 时间筛选 (Timezone关联)
- 前面同时添加i,ignore 忽略大小写
  - iexact
  - icontains
  - istartswith
  - iendswith
- 聚合函数aggregate()
  - Avg
  - Count
  - Max
  - Min
  - Sum
- 查询快捷 filter(columns=xx)
- 跨关系查询 filter(Object__o_name = XXXX)
- F对象 F()  例filter(object_columns_gt = F(object_coulumn2))
  - 与自身属性做对比
  - 支持算数运算
- Q对象 Q()  例 Q(object_columns_gt = xxx) & Q(object_columns_gt = xxx)
  - 可以对条件进行封装
  - 封装之后,可以支持逻辑运算
    - 与 &
    - 或 |
    - 非 ~

#### 6.模型成员

- 显性属性
  - 开发者手动书写的属性
- 隐性属性
  - 开发者没有书写,ORM自动生成的
  - 如果你把隐性属性手动声明了,系统不会为您产生隐性属性了
  - 如果需要修改 则要重写Manager的方法

#### 7.locals()

- locals
  - 内置函数
  - 将局部变量,使用字典的方式进行打包
  - key是变量名,value是变量中存储的数据

#### 附.状态码

- 2XX
  - 请求成功
- 3XX
  - 转发或重定向
- 4XX
  - 客户端错误
- 5XX
  - 服务器错了
  - 后端最不想看到的



### 五.Templates

#### 1.模板动态插入代码段

##### 1.1模板中的变量

```
{{var}}
```

##### 1.2模板中的点语法

```
grades grade
字典查询
属性或者方法	grade.name
索引 grade.0.gname
```

##### 1.3模板中的标签

```
{{% tag %}}
```

作用

- 1.加载外部传入的变量
- 2.在输出中创建文本
- 3.控制循环或逻辑



###### 1.3.1 if

```
-------if-------------
{% if  表达式 %}
语句
{% endif  %}
-------if-else--------------
{%  if 表达式 %}
语句
{% else  %}
语句
{% endif %}
--------if-elif---------------
{% if 表达式 %}
语句	
{% elif 表达式 %}
语句
{% endif %}

```

###### 1.3.2 for

```
----for-empty-end---------
{% for 变量 in 列表 %}
语句1 
{% empty %}
语句2
{% endfor %}
-----------------------------------
当列表为空或不存在时,执行empty之后的语句
{{ forloop.counter }} 表示当前是第几次循环，从1数数
{{ forloop.counter0}}表示当前是第几次循环，从0数数
{{ forloop.revcounter}}表示当前是第几次循环，倒着数数，到1停
{{ forloop.revcounter0}}表示当前第几次循环，倒着数，到0停
{{ forloop.first }} 是否是第一个  布尔值
{{ forloop.last }} 是否是最后一个 布尔值
```

###### 1.3.3 注释

```
------单行注释--------
{#  被注释掉的内容  #}


------多行注释--------
{% comment %}
内容
{% endcomment %}

------html渲染注释------
<!--> 内容   <-->
```

###### 1.3.4 乘除

```
{% widthratio 数  分母  分子  %}
```

###### 1.3.5 整除

```
{% if num|divisibleby:2 %}
```

###### 1.3.6 相等

```
-----ifequal # 如果相等-----
{%  ifequal  value1 value2 %}
语句
{% endifequal %}

-----ifnotequal 如果不相等-----
{%  ifnotequal  value1 value2 %}
语句
{% endifnotequal %}
```

###### 1.3.7 过滤器

过滤器:	{{ var|过滤器 }}
作用：在变量显示前修改

###### 1.3.8 加减

```
-----加法-----
{{ p.page | add : 5 }}
-----减法----没有减法过滤器，但是加法里可以加负数----
{{ p.page | add : -5}}
```

###### 1.3.9 大小写

```
----lower----
{{ p.pname|lower }}
----upper----
{{ p.pname|upper }}
```

###### 1.3.10 html渲染

```
---将字符串渲染为html元素---谨慎使用---
html:{{ code|safe}}
-------------------------------------
{% autoescape off%}
code
{% endautoescape %}

不想渲染
{% autoescape on%}
code
{% endautoescape %}

```

###### 1.3.11 继承

```
模板也可以继承

关键字block:挖坑
	{% block XXX%}
		code
	{% endblock %}

extends 继承，写在开头位置
	{% extends  '父模板路径' %}

include:    加载模板进行渲染
	格式{% include '模板文件' %}

```

##### 1.4结构标签

- block
  - 块
  - 用来规划我们的布局(挖坑)
  - 首次出现,代表规划
  - 第二次出现,代表填充以前的规划
  - 第三次出现,代表填充以前的规划,默认动作是覆盖
    - 如果不想覆盖,可以添加{{block.super}}
    - 这样就实现了增量式操作
- extends
  - 继承
  - 可以获取父模板中的所有结构

- block + extends 
  - 化整为零

- include
  - 包含
  - 可以将页面作为一部分,嵌入到其他页面中
- block + include
  - 由零聚一
- 三个标签可以混合使用
- 能用block + extends搞定的 就尽量不要使用include

##### 1.5 静态资源

- 动静分离
- 创建静态文件夹
- 在settings中注册STATICFILES_DIR=[]
- 在模板中使用
  - 先加载静态资源{%load static%}
  - 使用{%static 'xxx'%} xxx相对路径
- 坑点
  - 仅在debug模式可以使用
  - 以后需要自己单独处理

##### 

### 六.view

#### 1.urls

- 路由器

  - 按照列表的书写顺序进行匹配的
  - 从上倒下匹配,没有最优匹配的概念

- 路由规则编写

  - 我们通常直接指定以^开头
  - 在结尾处直接添加反斜线

- 路由路径中的参数使用()进行获取

  - 一个圆括号对应试图函数中的一个参数

    ```python
    url(r'^user_list/(?P<v1>\d+)/(?P<v2>\d+)$',views.user_list)
    ```

  - 参数

    - 路径参数
      - 位置参数
        - 按照书写顺序进行匹配
      - 关键字参数
        - 按照参数名称匹配,和顺序就无关了
    - 参数个数必须和视图函数中参数个数一直(除默认的request以外)

- 反向解析

  - 根据跟路由中注册的namespace和在子路由中注册name,这两个参数来动态获取我们的路径

  - 在模板中使用

    ```html
    {% url 'namespace:name'%}
    ```

  - 如果带有参数

    ```
    {% url 'namespace:name' value1 value2[valueN...]%}
    ```

  - 如果带有关键字参数

    ```
    {% url 'namespace:name' key1=value1 key2=value2[keyN=valueN...]%}
    ```

#### 2.错误页面定制

- 在模板中重写对应错误状态码的页面
- 关闭Debug
- 实现原则
  - 就近原则



#### 3.Request

- 内置属性
  - method
  - path
  - GET
    - 类字典结构
    - 一个key允许对应多个值
    - get
    - getlist
  - POST
  - META
    - 各种客户端元信息
    - REMOTE_ADDR远端访问IP

#### 4.Response

- HttpResponseRedirect
  - 重定向,暂时
  - 302
  - 简写redirect
- JsonResponse
  - 返回Json格式数据
  - 重写了\__init__,序列化json数据,指定content_type为application/json
- HttpResponsePermanentRedirect
  - 重定向,永久性
  - 301
- HttpResponseBadRequest
  - 400
- HttpResponseNotFound
  - 404
- HttpResponseForbidden
  - 403

- Response.MIME
  - 作用:指定传输数据使用哪种形式打开
  - 格式:大类型/小类型
    - image/png
    - image/jpg

### 七.会话技术

#### 1.出现场景

- 服务器如何识别客户端
- Http在Web开发中基本都是短连接

- 请求生命周期
  - 从Request开始
  - 到Response结束

#### 2.种类

##### 2.1 Cookie

- 客户端会话技术
  - 数据存储在客户端
- 键值对存储
- 支持过期时间
- 默认Cookie会自动携带,本网站所有Cookie
- Cookie不能跨域名,跨网站
- 通过HttpResponse
  - set_cookie
  - delete_cookie
- Cookie默认不支持中文
- 可以加盐
  - set_signed_cookie
  - 加密
  - delete_signed_cookie
  - 获取的时候需要解密

##### 2.2 Session

- 服务端会话技术
- 数据存储在服务器中
- 默认Session存储在内存中
- Django中默认会把Session持久化到数据库中
- Django中Session的默认过期时间是14天
- 主键是字符串
- 数据是使用了数据安全
  - 使用的base64
  - 在前部添加了一个混淆串
- session依赖于cookie
- 常用操作
  - get(key,default=none) #根据键获取回话的值
  - clear() #清除所有会话
  - flush() #删除当前的会话数据并删除会话的cookie
  - delete request['session_id'] #删除会话
  - session.session_key #获取session的key
  - request.session['user'] = username #设置数据

##### 2.3 Token

- 服务端会话技术
- 自定义的Session
- 如果Web页面开发中,使用起来和Session基本一致
- 如果使用在移动端或客户端开发中,通常以Json形式传输,需要移动端自己存储Token,需要获取Token关联数据的时候,主动传递Token

##### 2.4 Cookie和Session,Token对比

- Cookie使用更简洁,服务器压力更小,数据不是很安全
- Session服务器要维护Session,相对安全
- Token拥有Session的所有优点,自己维护略微麻烦,支持更多的终端

#### 3.CSRF

- 防跨站攻击
- 防止恶意注册,确保客户端是我们自己的客户端
- 使用了cookie中csrftoken进行验证,传输
- 服务器发送给客户端,客户端将cookie获取过来,还要进行编码转换(数据安全)
- 如何实现的
  - 在我们 存在csrf_token 标签的页面中,响应会自动设置一个cookie,csrftoken
  - 当我们提交的时候,会自动验证csrftoken
  - 验证通过,正常执行以后流程,验证不通过,直接403



### 八.模型关系

#### 1. 1:1

- 应用场景
  - 用于复杂表的拆分
  - 扩展新功能
- Django中的OneToOneField
  - 使用的时候,关系声明还是有细微差别的
- 实现
  - 使用外键实现的
  - 对外键添加了唯一约束
- 数据删除
  - 级联表
    - 主表
    - 从表
    - 谁声明关系谁就是从表
    - 在开发中如何确认主从
      - 当系统遭遇不可避免毁灭时,只能保留一张表,这个表就是你的主表
  - 默认特性(CASCADE)
    - 从表数据删除,主表不受影响
    - 主表数据删除,从表数据直接删除
  - PROTECT 受保护(on_delete=models.PROTECT)
    - 开发中为了防止误操作,我们通常会设置为此模式
    - 主表如果存在级联数据,删除动作受保护,不能成功
    - 主表不存在级联数据,可以删除成功
  - SET(on_delete=models.SET)
    - SET_NULL
      - 允许为null
    - SET_DEFAULT
      - 存在默认值
    - SET()
      - 指定值
  - 级联数据获取
    - 主获取从 隐性属性 级联模型的名字
    - 从获取主 显性属性 属性的名字

#### 2.   1:M

- ForeignKey
- 主从获取
  - 主获取从 隐性属性 级联模型_set
    - student_set Manager的子类
      - all
      - filter
      - exclude
      - Manager上能使用的函数都能使用
    - 从获取主
      - 显性属性



#### 3. M:N

- 实际上最复杂
- 开发中很少直接使用多对多属性,而是自己维护多对多的关系
- 产生表的时候会产生单独的关系表
  - 关系表中存储关联表的主键,通过多个外键实现的
  - 多个外键值不能同时相等
- 级联数据获取
  - 从获取主
    - 使用属性,属性是一个Manager子类
  - 主获取从
    - 隐性属性
      - 也是Manager子类,操作和从操作主完全一样
- 级联数据
  - add
  - remove
  - clear
  - set



#### 4. 模型继承

- Django中模型支持继承
- 默认继承是会将通用字段放到父表中,特定字段放在自己的表中,中间使用外键链接
  - 关系型数据库关系越复杂,效率越低,查询越慢
  - 父类表中也会存储过多的数据
- 使用元信息来解决这个问题(class Meta:)
  - 使模型抽象化
  - 抽象的模型就不会在数据库中产生映射了
  - 子模型映射出来的表直接包含父模型的字段

#### 5.企业开发 sql->model

- django可以根据表生成模型

  - ```shell
    python manage.py inspectdb > App.models.py
    ```

  - 元信息中包含一个属性 manage=False

- 如果自己的模型不象被迁移系统管理,也可以使用manage=False进行声明

### 九.静态文件

#### 1.setting设置

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR,'static/img')
```

#### 2.实现文件上传

##### 2.1 models

```python
class image(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to="img")
```

##### 2.2 templates

###### upload.html

```html
<form action="{% url "three:upload" %}" method = 'post' enctype="multipart/form-data">
    {% csrf_token %}
    <span>image_name</span><input type="text" placeholder="name" name="name" width="80px">
    <br>
    <span>image</span><input type="file" name="image">
    <button>submit</button>
    <br>
</form>
```

show.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3>{{ imagename }}</h3>
<img src="{{ url }}" alt="{{ imagename }}">
</body>
</html>
```



##### 2.3 views

```python
from django.http import HttpResponse
from django.shortcuts import render
from Three.models import image


def index(request):
    return render(request,"three/index.html")


def upload(request):
    if request.method == 'GET':
        return render(request,"three/upload.html")
    elif request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('image')
        item = image()
        item.name = name
        item.image = img
        item.save()
        return HttpResponse('success')

    
def show(request):
    imagename = request.GET.get('name')
    img = image.objects.filter(name=imagename).last()
    url = '/static/upload/'+img.image.url
    return render(request,"three/show.html",context={"url":url,"imagename":imagename})

```

##### 2.4 urls

```python
from django.conf.urls import url

from Three import views

urlpatterns=[
    url(r'^index/',views.index,name='index'),
    url(r'^upload/',views.upload,name='upload'),
    url(r'^show/',views.show,name='show'),
]
```

### 十.缓存

#### 1.创建缓存表

```shell
python manage.py createcachetable[table_name]
```

#### 2.缓存配置

```python
CACHES = {
	'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'my_cache_table',
        'TIMEOUT':'60',
        'OPTIONS':{
            'MAX_ENTRIES':'300',
        },
        'KEY_PREFIX':'rock',
        'VERSION':'1',
	}
}
```

#### 3.缓存使用

- 在视图中使用(使用最多的场景)

- @cache_page()

  - time秒60*5缓存5分钟
  - cache缓存配置,默认为default
  - key_prefix 前置字符串

- ```python
  from django.core.cache import cache
  cache.get(key)#读缓存
  cache.set(key,value)#存入缓存
  ```

  

#### 4.Redis安装配置

参考文章:https://blog.csdn.net/hzlarm/article/details/99432240

直接输入命令 `sudo apt-get install redis-server`
安装完成后，Redis服务器会自动启动。
使用`ps -aux|grep redis`命令可以看到服务器系统进程默认端口6379

`tcp 0 0 127.0.0.1:6379 0.0.0.0:* LISTEN`
使用`sudo /etc/init.d/redis-server status`命令可以看到Redis服务器状态

Redis服务器基本配置
配置文件为/etc/redis/redis.conf(在线安装推荐)或者 /usr/local/redis/redis.conf(手动安装)

首先sudo vi /etc/redis/redis.conf
添加Redis的访问账号
Redis服务器默认是不需要密码的，假设设置密码为hzlarm。
去掉requirepass 前面的注释#，在后面添加密码
requirepass hzlarm

开启Redis的远程连接
注释掉绑定地址#bind 127.0.0.1

修改Redis的默认端口
port 6379

Redis以守护进程运行
如果以守护进程运行，则不会在命令行阻塞，类似于服务
如果以非守护进程运行，则当前终端被阻塞，无法使用
推荐改为yes，以守护进程运行
daemonize no|yes
Redis的数据文件
dbfilename dump.rdb

数据文件存储路径
dir /var/lib/redis

配置完成后重新启动服务器
sudo /etc/init.d/redis-server restart or
sudo service redis-server restart or
sudo redis-server /etc/redis/redis.conf

Redis安装 配置服务器 启动客户端 数据操作 发布订阅 主从配置 卸载Redis

启动客户端
安装Redis服务器，会自动地一起安装Redis命令行客户端程序。命令行输入 redis-cli 如果设置了密码 hzlarmredis-cli -a hzlarm
常用命令： Redis命令不区分大小写
ping 返回PONG表示畅通
help 命令行的帮助
quit  或者Ctrl+d或者Ctrl+c退出
键的命令

- 查找键，参数支持正则KEYS pattern例如keys *查看所有的key列表
- 判断键是否存在，如果存在返回1，不存在返回0EXISTS key [key ...]
- 查看键对应的value的类型TYPE key
- 删除键及对应的值DEL key [key ...]
- 设置过期时间，以秒为单位
- 创建时没有设置过期时间则一直存在，直到使用使用DEL移除EXPIRE key seconds
- 查看有效时间，以秒为单位TTL key
- 修改 key 的名称RENAME key newkey



#### 5.Django-Redis配置

先安装dJango-redis包

```shell
pip install django-redis
```

setting.py

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        },
     'TIMEOUT': 60*60*8
    }
}
```

#### 6.设置多个缓存

##### 1.settings.py修改

在settings.py中的CACHES字典中添加多个缓存 例如:

```python
CACHES = {
	'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'my_cache_table',
        'TIMEOUT':'60',
        'OPTIONS':{
            'MAX_ENTRIES':'300',
        },
        'KEY_PREFIX':'rock',
        'VERSION':'1',
	}
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
    },
}
```

##### 2.注解cache_page

修改cache参数

```python
@cache_page(time,cache='redis')
```

##### 3.直接设置缓存

```python
from django.core.cache import cache
cache.set(key,value)
# example
token = uuid.uuid4().hex
cache.set(token,user.id)
```

##### 4.直接获取缓存

```python
from django.core.cache import cache
cache.get(key)
```

### 十一.AOP中间件

#### 1.调用顺序

- 中间件注册的时候是一个列表
- 如果我们没有在切点处直接进行返回,后续中间件就不再执行了
- 如果我们直接进行了返回,后续中间件就不再执行了

#### 2.切点

- process_request
- process_view
- process_template_response
- process_response
- process_exception

#### 3.切面

#### 4.创建定制中间件

##### 1.创建middleware文件

directory:middlewares

在其下创建py文件

创建中间件类文件

例如:

```python
from django.utils.deprecation import MiddlewareMixin

class HelloMiddle(MiddlewareMixin):
	pass
```

##### 2.在settings.py中注册创建的middleware

```python
MIDDLEWARE = [
    'middleware.helloMiddleware.HelloMiddle',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

##### 3.根据需求编写切点函数

例如:

```python
from django.utils.deprecation import MiddlewareMixin

class HelloMiddle(MiddlewareMixin):
    def process_request(self,request):
        print('test')
```

### 十二.练习:分页器

#### 1.Paginator包简介

- 存在于django.core中
- 对象创建:Paginator(数据集,每一页数据数)
- 属性:
  - object_list 当前页面所有的数据对象
  - number 当前页码值
  - paginator 当前page关联的Paginator对象
- 方法:
  - has_next() 是否有下一页
  - has_previous() 是否有上一页
  - has_other_pages() 是否有上一页或下一页
  - next_page_number() 返回下一页的页码
  - previous_page_number() 返回上一页的页码
  - len() 返回当前页的数据的个数

#### 2.例:

##### 1.创建urls中url

```python
url(r'getstudents', views.get_students, name='get_students'),
```



##### 2.创建views中方法

```python
def get_students(request):
    page = request.GET.get('page')

    per_page = request.GET.get('per_page')

    if not page:
        page = 1

    if not per_page:
        per_page = 10


    students = Student.objects.get_queryset().order_by('id')

    paginator = Paginator(object_list=students,per_page=per_page)

    students = paginator.page(page)

    data = {
        "students":students,
        "pages":paginator.page_range,
    }

    return render(request,"students.html",context=data)
```



##### 3.创建templates中模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <link href="https://cdn.bootcss.com/twitter-bootstrap/3.3.7/css/bootstrap.css" rel="stylesheet">

    <script type="text/javascript" src="https://cdn.bootcss.com/twitter-bootstrap/3.3.7/js/bootstrap.js"></script>

    <script type="text/javascript" src="https://cdn.bootcss.com/jquery/1.11.1/jquery.js"></script>

</head>
<body>
<ul>

    {% for student in students %}
        <li>{{ student.s_name }}</li>
    {% endfor %}
</ul>





<nav aria-label="Page navigation">
  <ul class="pagination">
    <li>
      <a href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    {% for page in pages %}
        <li><a href="{% url "app:get_students" %}?page={{ page }}">{{ page }}</a></li>
    {% endfor %}
    <li>
      <a href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>


</body>
</html>
```

### 十三.部署

nginx:http://www.nginx.cn/doc/index.html

- django中自带开发者服务器
  - runserver
    - 路由处理功能,动态资源处理
    - 如果是debug的话,静态资源处理功能
  - 功能健壮,性能是比较低的,仅适用于开发
- 部署不会使用单一服务器
  - Apache
  - Nginx
    - HTTP服务器
      - 处理静态资源
    - 反向代理
      - uWSGI HTTP服务器
      - gunicorn HTTP服务器
    - 邮件服务器
    - 流媒体服务器

#### 1.安装nginx

 详见:http://nginx.org/en/linux_packages.html

#### 2.控制nginx

```
# 启nginx
sudo nginx
# 查看nginx运行状态
ps -ef|grep nginx
# 杀nginx
sudo kill 进程id
# 信息查看
nginx -v
nginx -V
# 控制nginx
nginx -s signal
		stop 关闭
		quit 关闭
		reload 重新加载配置
		
# 通过系统管理 不建议使用
systemctl status nginx # 查看nginx状态
systemctl start nginx # 启动nginx服务
systemctl stop nginx # 关闭nginx服务
systemctl enable nginx # 设置开机自启
systemctl disable nginx # 禁止开机自启
```

#### 

#### 3.配置nginx配置文件

nginx.conf

```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    server {
    listen       80;
    server_name  localhost;

    # project repository
    root   /home/bool/DjangoLearnProject/HelloNginx;

    location /static {

        alias /home/bool/DjangoLearnProject/HelloNginx/static;
        }

    location / {
        include /etc/nginx/uwsgi_params;
        uwsgi_pass 127.0.0.1:8888;
        }


    }

}

```

#### 4.启动nginx服务

conf路径得是绝对路径

```
sudo nginx -c /home/bool/DjangoLearnProject/HelloNginx/config/nginx.conf
```

#### 5.安装uwsgi

```
# 需要安装python-dev包
apt-get install libpython3.5-dev

# 安装uwsgi
pip install uwsgi
```



#### 6.配置uwsgi配置文件

uwsgi.ini

```
[uwsgi]
# 使用nginx连接时 使用
socket=0.0.0.0:8888
# 直接作为web服务器使用
# http=0.0.0.0:8888
# 配置工程目录
chdir=/home/bool/DjangoLearnProject/HelloNginx
# 配置项目的wsgi目录,相对于工程目录
wsgi-file=HelloNginx/wsgi.py

# 配置进程,线程信息
process=4
threads=10
enable-threads=True
master=True
pidfile=uwsgi.pid
daemonize=uwsgi.log
```

#### 7.关闭服务并重启

```
sudo nginx -s quit # 关闭nginx
uwsgi --stop uwsgi.pid # 关闭uwsgi
sudo nginx -c xxxxxxxxxx# 启动nginx 以xxxxx配置文件启动
sudo nginx -s reload # 重启
uwsgi --ini inipath # 以ini配置文件的配置启动uwsgi
```

#### 8.云端部署

- 安装云服务器系统
  - Ubuntu
  - centos
- 安装一套开发环境
  - Python
    - 2.x
    - 3.x
  - pip
    - 注意版本兼容
  - virtualenv
    - 版本不兼容
    - workon_home
    - source xxx
  - mysql
    - apt直接安装
  - redis
    - 源码安装
    - make % make test
    - utils/install_server.sh
  - nginx
    -  详见:http://nginx.org/en/linux_packages.html
  - 准备进行部署
    - 安装项目所需依赖
      - 导出项目依赖 pip freeze > requirements.txt
      - pip install -r xxx.txt
    - 修改配置文件到指令路径
    - 从静态文件开始部署
    - 动态资源
      - 处理好数据
      - 创建库,创建表   
  - 坑点
    - 邮件发送
      - 25端口是非安全端口,阿里不允许使用
      - 使用安全SSL端口465



#### 9.nginx对接runserver

在nginx配置文件中对接uwsgi的ip:port修改成runserver的ip:port

```
location /{
	proxy_pass http://127.0.0.1:8000
}
```

#### 10.负载均衡

```
upstream my_server{
	server 127.0.0.1:8000 weight=1;
	server 127.0.0.1:8001 weight=1;
}
server{
	location / {
		proxy_pass http://my_server;
	}
}
```

### 十四.Rest_framework

#### 1.安装

#### 2.HelloREST

- 禁用Rest_framework的模板界面

  settings.py

  ```
  REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': (
          'rest_framework.renderers.JSONRenderer',
      )
  }
  ```

- 序列化器

- 视图函数

  - viewsets.ModelViewSet
  - CBV
  - 视图集合

- 路由

  - routers.DefaultRouter

- 记得在INSTALLED_APPS添加rest_framework

- nginx部署时 需要将rest_framework的静态资源也部署上

- ```
      location /static/rest_framework/ {
          alias /home/bool/.virtualenvs/GP1/lib/python3.5/site-packages/rest_framework/static/rest_framework/;
          }
  ```

  



- runserver
  - 所有Api变成可视化
  - 超链接
    - HyperLinkedModelSerializer
  - 对数据集合实现了
    - 路由 /users/,/groups/
    - get
    - post
  - 对单个数据实现了
    - 路由 /users/id/,/groups/id/
    - get
    - post
    - put
    - delete
    - patch
  - viewsets做了视图函数的实现
  - router做了路由的注册 

#### 3.模型序列化

- 模型序列化
  - 正向序列化
    - 将模型转换成JSON
  - 反向序列化
    - 将JSON转换成模型
- serialization
  - 在模块serializers
    - HyperLinkedModelSerializer
      - 序列化模型,并添加超链接
    - Serializer
      - 手动序列化
    - ModelSerializer

#### 4.Request/Response/APIView

- Request
  - rest_framework.request
  - 将Django中的Request作为了自己的一个属性_request
  - 属性和方法
    - content_type
    - stream
    - query_params
    - data
      - 同时兼容 POST,PUT,PATCH
    - user
      - 可以直接在请求上获取用户
      - 相当于在请求上添加一个属性,用户对象
    - auth
      - 认证
      - 相当于请求上添加了一个属性,属性值是token
    - successful_authenticator
      - 认证成功
- Response
  - 依然是HttpResponse的子类
  - 自己封装的
    - data 直接接受字典转换成JSON
    - status 状态码
  - 属性和方法
    - rendered_content 渲染内容
    - status_text 状态码转换成文字
- APIView
  - renderer_classes
    - 渲染的类
  - parser_classes
    - 解析转换的类
  - authentication_classes
    - 认证的类
  - throttle_classes
    - 节流的类
    - 控制请求频率的类
  - permission_classes
    - 权限的类
  - content_negotiation_class
    - 内容过滤类
  - metadata_class
    - 元信息的类
  - versioning_class
    - 版本控制的类
  - as_view()
    - 调用父类中的as_view -> dispatch
      - dispatch被重写
      - initialize_request
        - 使用django的request构建了一个REST中的Request
      - initial
        - perform_authentication
          - 执行用户认证
          - 遍历我们的认证器
            - 如果认证成功会返回一个元祖
            - 元祖中的第一个元素就是 user
            - 第二个元素就是auth,token
        - check_permissions
          - 检查权限
          - 遍历我们的权限检测器
            - 只要有一个权限检测没通过
            - 就直接显示权限被拒绝
            - 所有权限都满足,才算是拥有权限
        - check_throttles
          - 检测频率
          - 遍历频率限制器
            - 如果验证不通过,就需要等待
      - csrf_exempt
        - 所有APIView的子类都是csrf豁免的
- 错误码
  - 封装status模块中
  - 实际上就是一个常量类
- 针对视图函数的包装
  - CBV
    - APIView
  - FBV
    - 添加@api_view装饰器
    - 必须手动指定允许的请求方法

#### 5.CBV 类视图

APIView

- 子类
  - generic包中
  - GenericAPIView
    - 增加的模型的获取操作
    - get_queryset
    - get_object
      - lookup_field 默认pk
    - get_serializer 获取序列器
    - get_serializer_class 指定序列器
    - get_serializer_context 序列器上下文内容
    - filter_queryset 过滤器
    - paginator 分页器
    - paginate_queryset 分页后的数据
    - get_paginated_response 获取分页后的response
  - CreateAPIView
    - 创建的类视图
    - 继承自GenericAPIView
    - 继承自CreateModelMixin
    - 实现了post进行创建
  - ListAPIView
    - 列表的类视图
    - 继承自GenericAPIView
    - 继承自mixins.ListModelMixin
  - 实现了get
  - RetrieveAPIView
    - 查询单个数据的类视图
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 实现了get
  - DestoryAPIView
    - 销毁数据的类视图,删除数据的类视图
    - 继承自GenericAPIView
    - 继承自DestoryModelMixin
    - 实现了delete
  - UpdateAPIView
    - 更新数据的类视图
    - 继承自GenericAPIView
    - 继承自UpdateModelMixin
    - 实现了put,patch
  - ListCreateAPIView
    - 获取列表数据,创建数据的类视图
    - 继承自GenericAPIView
    - 继承自ListModelMixin
    - 继承自CreateModelMixin
    - 实现了get,post
  - RetrieveUpdateAPIView
    - 获取单个数据,更新单个数据的类视图
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 继承自UpdateModelMixin
    - 实现了get,put,patch
  - RetrieveDestoryAPIView
    - 获取单个数据,删除单个数据
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 继承自DestoryModelMixin
    - 实现了 get,delete
  - RetrieveUpdateDestroyAPIView
    - 获取单个数据,更新单个数据,删除单个数据的类视图
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 继承自UpdateModelMixin
    - 继承自DestoryModelMixin
    - 实现了 get,put,patch,delete
- mixins
  - CreateModelMixin
    - create
    - perform_create
    - get_success_headers
  - ListModelMixin
    - list
      - 查询结果集,添加分页,帮你序列化
  - RetrieveModelMixin
    - retrieve
      - 获取单个对象并进行序列化
  - DestoryModelMixin
    - destory
      - 获取单个对象
      - 调用perform_destory
      - 返回Response 状态码204
    - perform_destory
      - 默认是模型delete
      - 如果说数据的逻辑删除
        - 重写进行保存
  - UpdateModelMixin
    - update
      - 获取对象,合法验证
      - 执行更新(perform_update)
    - perform_update
      - 更新
    - partial_update
      - 差量更新,对应的就是patch

- viewsets
  - ViewSetMixin
    - 重写as_view
  - GenericViewSet
    - 继承自GenericAPIView
    - 继承自ViewSetMixin
  - ViewSet
    - 继承自APIView
    - 继承自ViewSetMixin
    - 默认啥都不支持,需要自己手动实现
  - ReadOnlyModelViewSet
    - 只读的模型视图集合
    - 继承自RetrieveModelMixin
    - 继承自ListModelMixin
    - 继承自GenericViewSet
  - ModelViewSet
    - 直接封装对象的所有操作
    - 继承自GenericViewSet
    - 继承自CreateModelMixin
    - 继承自RetrieveModelMixin
    - 继承自UpdateModelMixin
    - 继承自DestoryModelMixin
    - 继承自ListModelMixin

#### 6.权限控制

1.用户登录,获得用户token,缓存token

2.操作api时需要新的params:token,根据token获取用户并判断is_admin字段



基本权限编写

```
# 继承BaseAuthentication编写,实现抽象函数authenticate
class UserAuth(BaseAuthentication):
	def authenticate(self,request):
		token = request.query_param.get('token')
		u_id = cache.get(token)
		user = UserModel.objects.get(pk=u_id)
		return user,token
```

#### 7.节流控制

settings.py

```
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
    	# 需要自己编写throttle替换该设置
        'rest_framework.throttling.UserRateThrottle',
    ),
    "DEFAULT_THROTTLE_RATES":{
    	"user":"5/m"
    	"address":"5/m"
    }
}
```

throttle实现类

```
class UserThrottle(SimpleRateThrottle):
	
	scope = 'user'
	
	def get_cache_key(self,request,view):
		ident = request.auth
	else:
		ident = self.get_ident(request)
		
	return self.cache_format % {
		'scope':self.scope
		'ident':ident
	}
	
class AddressThrottle(SimpleRateThrottle):
	
	scope = 'address'
	
	def get_cache_key(self,request,view):
		ident = request.auth
	else:
		ident = self.get_ident(request)
		
	return self.cache_format % {
		'scope':self.scope
		'ident':ident
	}
```

CBV中添加

```
throttle_classes = (UserThrottle,)
```

#### 8.级联查询

现在有A,B两个model,关系为A 一对多 B

serializers.py

```python
class BModelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = B
		fields = {.......}
        
class AModelSerializer(serializers.HyperlinkedModelSerializer):
	B_set = BModelSerializer(many=True,read_only=True)
	class Meta:
		model = A
		fields = {.......,'B_set'}
```

修改集合B_set的叫法为NewName

*指定参数 related_name='NewName'

models.py

```python
class A(models.Model):
	.........


class B(models.Model):
	xxxxxxxxx
	B_A = models.ForeignKey(A,related_name='NewName')
```



### 十五.异步任务/后台管理

#### 1.异步任务 celery安装

```
pip install celery
pip install django-celery-results
```

#### 2.简单任务编写

```
from celery import Celery
app = Celery("tasks",broker='redis://localhost:6379/1')

@app.task
def add(a,b):
	return a+b
	
if __name__ == '__main__':
	print(add.delay(4,6)) # app.delay异步实现
```



#### 3.celery部署

settings.py

```
CELERY_BROKER_URL = 'redis://localhost:6379/1'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'
```

执行migrations

编写任务实现

启动

```
celery -A ProjectName worker --loglevel=info
```



#### 4.异步任务实现email发送

settings.py

```
EMAIL_HOST_USER="xxxxxxxxx@xxx.com"
EMAIL_HOST_PASSWORD="XXX"
EMAIL_HOST="smtp.XXX.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True

```



```
@shared_task
def send_email(receive):
	subject = "你要发送的邮件标题"
	message = "内容"
	from_email = "xxxxxxxxx@xxx.com"
	recipient_list = (receive,)
	send_mail(subject,message,from_email,recipient_list)
```



#### 5.后台管理代码参考

在admins.py中编写

```python
class StudentAdmin(admin.ModelAdmin):
    # 字段显示处理
	def sex(self):
		if self.s_sex:
			return '女'
		else:
			return '男'
       	# 设置显示的标题
        sex.short_description = '性别'
        # 显示字段
        list_display = ('s_name' , 's_age', sex)
        # 过滤字段
        list_filter = ()
        # 搜索字段
        search_fields = ()
        # 分页,每页多少个数据
        list_per_page = xx
        # 排序规则
        orderding = ()
        # 分组显示
        fieldsets = (
        	('基本信息',{'fields':('s_name','s_age','s_sex')}),
            ('可选信息',{'fields':('s_height','s_weight')}),
        )
        
			
# 后台注册模型
admin.site.register(student,StudentAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('g_name' , 'g_position')
    # 创建grade时附带创建student
    inlines = [StudentInfo]
   
class StudentInfo(admin.TabularInline):
    extra = 3
    model = Student
```



admin.site修改为自己的site

```python
class MyAdminSite(admin.AdminSite):
	
    site_title = 'test'
    site_header = 'test'
	
site = MyAdminSite()
site.register(xxxxx)
```