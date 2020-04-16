# Flask

## 一.配置环境

- 虚拟环境
- 安装flask
  - pip install flask
- hello flask

```python
from flask import Flask,abort

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello flask'

if __name__ == __main__:
    app.run(debug=True)
```

- app.run() 参数
  - debug
  - threaded 多线程
  - port
  - host

## 二.插件

### Flask-Script

- 可以添加Flask脚本的扩展库
- 使用命令行参数
  - python xxx.py runserver

### Flask-blueprint

- 路由写法
  - 声明Blueprint对象
    - Blueprint('name',\__name__)
  - 注册到app对象上
    - app.register_blueprint()

### Flask-SQLAlchemy

- ORM

### Flask-Migrate

- 数据库迁移

### Flask-session

- 服务端session

- 支持redis
- RedisSessionInterface
  - save_session
    - 数据进行了pickle序列化

### Flask-Bootstrap

### Flask-debugtoolbar

- debug侧边栏调试工具

### Flask-Caching

- 缓存

### Flask-Mail

- 发邮件

### Flask-Rest-JSONAPI

### Flask-RESTful

### Flask-Restless

## 三.MVC流程

### (一).路由

#### 1.懒加载

函数调用的方式加载

@app.route()

#### 2.蓝图

flask-blueprint

### (二).模板

- flask.render_template()
  - 参数1:模板
  - 参数2~n: key=value (**kwargs)

### (三).数据库CRUD

- 直接写sql
- ORM
  - sqlalchemy
  - flask-SQLAlchemy
- 数据库uri写法
  - 数据库+驱动://用户名:密码@主机:端口/

## 四.Flask相关

### (一)四大内置对象

- Request
  - request
- Session
  - session
- G
  - g
    - global
    - 跨函数传递数据
    - 间接传递数据
- Config
  - 在模板中 config
  - python代码 current_app.config
    - 在项目启动之后才能执行

## 五.views

### 1.路由

- 路由参数获取
- <>
  - 语法<converter : variable_name>
  - converter:
    - string
      - 以/作为结尾的
    - int
    - float
    - path
      - 从path修饰开始,后面的路径都是我们的
      - /没有作用了
    - uuid
    - any

### 2.视图函数

- 默认支持get,options,head
- 手动注册其他请求
  - @blue.route('',methods=['GET','POST'])

### 3.request/response

#### Request

- url
- base_url
- host_url
- path
- method
- remote_addr 
- args
  - 请求参数
  - query_string
  - query_params
  - get请求参数
  - 所有请求都能获取这个参数
  - ImmutableMultiDict
    - 数据类型
    - args和form都是这个类型

#### Response

- 创建Response三种方式
  - 直接返回字符串
  - make_response
  - 构建Response()
- 参数设置
  - 内容
  - 状态码
- render_template
  - 帮助把模板变成html字符串
- 重定向
  - redirect
  - 反向解析 url_for
- 终止处理
  - abort
    - 本质上就是一个exception
  - HttpException
    - 子类指定两个属性即可实现
    - code
    - description
- 异常捕获
  - @app.errorhandler(code_or_exception)

### 4.会话

- cookie

  - 设置cookie
    - response.set_cookie(key,value)
  - 获取cookie
    - request.cookie.get(key)
  - 默认对中文进行了处理

- session

  - 设置session

    - app.config设置SECRET_KEY
    - session[key] = value

  - 获取session

    - session.get(key)

  - flask中session默认特性

    - 存储在cookie中
    - 数据序列化
    - base64编码
    - zlib压缩
    - 还传递了hash
    - 过期时间31天

  - flask-session

    - https://pythonhosted.org/Flask-Session/

    - ```python
      # 设置session类型
      app.config["SESSION_TYPE"] = 'redis'
      # 初始化session
      sess = Session()
      sess.init_app(app)
      ```

### 5.模板

#### 1.模板语言

- 模板中的变量 {{  var }}
- 模板中的标签 {% tag %}
  - block
    - 块操作
    - {% block xxx %}
    - {{ super() }}  继承后保留块中的内容
    - {% endblock %}
  - extends
    - {% extends ‘xxx’ %}
  - include
    - 包含，将其他html包含进来
    - {% include ’xxx’ %}
  - marco
    - 宏定义，可以在模板中定义函数
    - {% marco hello(name) %}
    -  {{ name }}
    -  {% endmarco %}
    - {% from ‘xxx’ import xxx %} 导入宏定义函数
  - for
    - 循环
    -  {% for item in cols %}
    -  {% else %}
    -  {% endfor %}
    - 循环信息loop
      - first
      - last
      - index
      - revindex
  - if
    - 判断
    - {% if a==b %}
    - {% endif %}
  - 过滤器
    - {{变量|过滤器|过滤器....}}
    - capitalize
    - lower
    - upper
    - title
    - trim
    - reverse
    - format
    - striptags

#### 2.模板中使用反向解析

- url_for
  - {{url_for('static',filename='xxx')}}

### 6.蓝图/路由创建参数

- template_folder
- url_prefix
- static_folder

### 7.中间件/钩子

- 中间件属性
  - before_first_request
  - before_request
  - after_request
  - teardown_request
- 写法
  - 注解写法
  - @app(or Blueprint).property

## 六.models

### 1.SQLAlchemy-orm

Model

- 文档
  - flask-sqlalchemy
  - sqlalchemy

- 设置字段
  - \__tablename__ 表名
  - \__abstract__  抽象(继承模型用)

- 基本字段
  - Integer
  - SmallInteger
  - BigInteger
  - Float
  - Numeric
  - String
  - Text
  - Unicode
  - Unicode Text
  - Boolean
  - Date
  - Time
  - DateTime
  - Interval
  - LargeBinary
- 常用约束
  - primary_key
  - autoincrement
  - unique
  - index
  - nullable
  - default
  - ForeignKey()
- 建库
  - db.create_all()
  - db.drop_all()
- 数据操作
  - 数据插入(增)
    - db.session.add(object)
    - db.session.add(list[object])
  - 数据删除(删)
    - db.session.delete(object)
  - 数据更新(改)
    - 获取已有的数据后修改并再次插入数据
  - 完成操作
    - db.session.commit()
  - 简单查询数据(查)
    - model.query.xxxx
      - Basequery类
    - model.query
      - get(id) 根据id查询
      - all() 查询全部
- flask-sqlalchemy参数
  - SQLALCHEMY_POOL_SIZE
    - 连接池中链接最大个数
  - SQLALCHEMY_POOL_TIMEOUT
  - SQLALCHEMY_POOL_RECYCLE
    - 链接回收时间

### 2.查询数据-1

- model.query

- 获取单个对象

  - first
  - get
  - get_or_404

- 获取结果集

  - all
    - 特殊,特例
    - 列表
  - filter
    - BaseQuery对象
    - filter(类名.属性.运算符('xxx'))
      - \__eq__
      - \__gt__
      - \__ge__
      - \__lt__
      - \__le__
      - contains
      - startswith
      - endswith
      - in_
      - like
    - 可以带逻辑运算符
      - filter(逻辑运算符(条件,条件))
      - and_
      - or_
      - not_

  - offset()
    - offset和limit在一块不区分顺序,offset在前执行
  - limit()
    - offset和limit在一块不区分顺序,offset在前执行
  - order_by()
    - db.text("-id")
    - 根据传入的字段排序
    - 不能放在offset或者limit后调用
  - get()
  - first()
  - paginate()
    - 分页器
    - page
    - per_page
    - error_out
    - max_per_page
  - filter_by()
    - 用在级联数据上
    - 条件语法精准
    - 字段 = 值
  - 级联数据
    - 获取
      - 手动实现获取
      - 使用关系 relationship进行级联查询
        - 反向引用
        - db.relationship('Class',backref='model',lazy=True)
    - 关系
      - 1:1
        - ForeignKey + Unique
      - 1:M
        - ForeignKey
      - M:N
        - 额外关系表
          - ForeignKey
          - Foreign

### 3.orm其他

#### 1.高并发问题

- 加锁
  - 悲观锁(数据操作加锁)
    - db.session.Query(Model).with_lockmode("update")
  - 乐观锁
    - 操作前和操作后对数据进行比对
    - 如果满足预期则成功

#### 2.数据库事务

- 默认orm开启事务
- begin
- commit
- rollback 回滚
  - db.session.rollback()
  - 多个操作才有意义



### 4.查询数据-2

- 直接查询
  - db.session.query(Model).get()
- 连接
  - db.session.query(Model).join(Movie.反向引用字段)
- 聚合
  - db.session.query(Model).group_by(Movie.字段)
- 条件
  - db.session.query(Model).having(Movie.字段==xx)
- 计算函数
  - fuc.函数名(字段)
- 排序
  - db.session.query(Model).order_by(字段)
  - 字段前加负为逆序

## 七.restful

### flask-restuful

### 1.JSON格式

```python
# 单个对象
{
    "status":200,
    "msg":"ok",
    "data":{
        "property":"value",
        "property":"value",
        "property":"value"
    }
}

# 多个对象,列表对象
{
    "status":200,
    "msg":"ok",
    "data":[
        {
            "property":"value",
            "property":"value",
            "property":"value"
        },
        {
            "property":"value",
            "property":"value",
            "property":"value"
        },
        {
            "property":"value",
            "property":"value",
            "property":"value"
        },
    ]
}
```

### 2.序列化

#### 1.配置fields

- 非嵌套数据

```python
xxx_fields = {
	"property_other":fields.String(attribute=property),
	"property1":fields.Float
}
```

- 嵌套数据

```python
nest_xxx_fields = {
	"property_other":fields.String(attribute=property),
	"property1":fields.Float,
	"nest_data":fields.Nested(xxx_fields)
}
```

- 手动指定映射到原始属性名称
  - attribute="property_name"
- 属性指定默认值
  - default = "value"

#### 2.利用fields序列化数据

- 函数marshal()
  - marshal(data,data_fields)

- 类装饰器@marshal_with



#### 3.fields

- Raw
  - format
  - output
  - 调用
    - 将数据传递进格式化工具的时候,现货取值output
    - 再对值进行格式化
- String
  - 继承Raw
  - 将value进行格式化
  - 转换成兼容格式的text
- Integer
  - 继承Raw
  - 重写了初始化,default=0
  - 重写格式化,直接将value转换成int
- Boolean
  - 继承Raw
  - 重写格式化,直接将value转换成bool
- Nested
  - 继承自Raw
  - 重写output
  - 进行marshal
- List
  - 继承自Raw
  - 重写output
    - 判断你的类型
    - 对不同的类型进行不同的处理
      - dict 直接进行处理
      - list 迭代处理
  - 重写format
    - 进行格式化

#### 4.输入管理

```python
# RequestParser对象
parser = reqparse.RequestParser()
# add_argument()
parser.add_argument("name",type=str,help="xxxx")
```

- add_argument参数
  - type
    - 数据类型
  - required
    - 是否必须
  - help
    - 错误提示
  - action
    - append 追加 同一个key可以有多个value,转换成列表
  - dest
    - 别名 调args时可以用这个名称
  - location
    - 获取位置,可以是单个值,也可以是列表
    - "form"
    - "args"
    - "cookies"
    - 不同位置获得的参数可以拼接到一块

## 八.日志

### Logging

#### 1.四大组成

- Logger
  - 和代码直接对接的对象
- Handler
  - 处理者
  - 日志处理策略
- Filter
  - 过滤器
- Formatter
  - 格式化

#### 2.日志级别

### 日志处理流程

- 通过Logger对象进行输出
- 交给Handler处理者进行处理
  - 处理者可以对输出样式进行格式化
  - 也可以对数据进行过滤