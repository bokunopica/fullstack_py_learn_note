# Python基础+

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

### 4.继承

```python
# 对父类方法进行扩展
# 调用父类方法
# 1.使用super类
# super()就是使用super类创建出来的对象
class Base:
    def test(self):
        print("a")
class Child(Base):
    def test(self):
        print("b")
        super().test()
print(Child().test)# 先打印b再打印a
# 2.使用父类名(不推荐)
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

### 5.新式类/旧式(经典)类

- 新式类
  - 以object为基类的类
  - py3.+定义的类都是新式类
- 经典类
  - 不以object为基类的类
  - py2定义时不指定object作为基类,则默认定义经典类
- 方法搜索顺序两者不同!

### 6.多态

- 继承父类
- 重写父类的方法



