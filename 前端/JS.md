# JavaScript

## 一.基础知识

### 编辑器

- pycharm

- 百度网盘有



### (一).javascript组成

- ECMAScript 3,4,5,6,7
- DOM 文档
- BOM 浏览器

### (二).HTML引入JS代码

#### 1.直接HTML中写

type属性指定text/javascript

```HTML
<head>
    <script type="text/javascript">
    	alert("hello world")
    </script>
</head>
```

#### 2.外部导入

使用src属性

```HTML
<head>
    <script src="javascript.js"></script>
</head>
```

### (三).JS的输出方法

#### 1.alert()

- 网页弹小窗

#### 2.document.write()

- 写入html页面

- 如果内容中含有标签会自动解析

- 转义字符:   & and符号

  - ```javascript
    &lt;
    ```

  - ```javascript
    &gt;
    ```

#### 3.console.log()

- 浏览器控制台

### (四)注释与其他注意点

- 单行注释
  - ctrl+/
- 多行注释
  - ctrl+shift+/

- 代码结束必须加分号
- 代码压缩:去掉编写代码的时候,有的所有空格,tab键和换行

### (五)常量

- 基本数据类型
  - 数字
    - number  
      - 100 -20 3.14
  - 布尔值
    - boolean 
      - true false
  - 字符串
    - 单引号,双引号引起来的内容
      - 'hello',"world"
- 复合/引用数据类型
- 特殊数据类型
  - null 空
  - undefined
  - NaN
    - not a number

### (六)变量

- 声明变量
  - 初始化:直接给变量赋值
  - 不初始化:变量值为undefined

```js
var num = 100; //初始化
var num; //num=undefined
var num = null; //初始化为null,速度更快
```

- 标识符/变量名

  - 变量名也是标识符

  - 规则

    - 只能由数字,字母,下划线和美元($)符号组成

    - 不能以数字开头

    - 不能是保留字和关键字

      ![保留字和关键字](..\图片\image-20200307160159439.png)

    - 大小写敏感 age/Age这是两个变量

    - 见名思意(尽量使用英文全称)

    - 单词个数超过两个的

      - 驼峰式命名 userName className
      - 下划线命名 user_name class_name

- 弱引用类型

  - 赋值成什么数据类型就是什么数据类型
    - 不建议改变变量的数据类型,容易引起歧义
  - 关键字 typeof
    - 格式: typeof 常量/变量
    - 功能: 输出当前常量或者变量的数据类型

### (七)进制转换

- 十进制转二进制
  - 模2取余法
    - 同样可适用10转8 10转16
- 十进制转八进制
  - 先转换为二进制
  - 再将二进制数转换为八进制
    - 从右往左数,每三位一组,最后将每一组单独转换为十进制数
- 十进制转十六进制
  - 先转换为二进制
  - 再将二进制数转换为十六进制
    - 从右往左数,每四位一组,最后将每一组单独转换为十进制数

## 二.JS基础

### (一)运算符

#### 1.算数运算符

- +
- -
- *
- /
- % 取余

#### 2.关系运算符

- &gt;
- <

- &gt;=
- <=

- ==

- !=
- ===
- !==

#### 3.逻辑运算符

- &&
- ||
- !

#### 4.一元运算符

- ++
- --

#### 5.赋值运算符

- 基本赋值运算符 =
- 复合赋值运算符 += -= ....

### (二)运算

#### 1.算数运算

不同数据类型数据进行算数运算

- 自动数据类型转换:不同数据类型之间没有办法进行运算,将数据转换成同一数据类型,再进行计算
  - 1.其中有一个操作数必须是字符串,运算符必须是+号,别的数据类型转成字符串,进行字符串拼接
  - 2.任何数据和字符串做+加法意外的操作,那么字符串要先转换成数字再去进行运算
    - 如果字符串是一个纯数字字符串组成的字符串,转成对应的数字
    - 如果字符串中含有除数字意外的别的字符,转换成NaN,NaN和任何数据进行运算都是NaN
  - 3.除字符串以外的数据,在进行运算的时候,先转成数字,再进行运算
    - 布尔值
      - True -> 1
      - False -> 0
    - null ->0
    - undefined -> NaN
    - NaN -> NaN

#### 2.赋值运算

```js
var a = 1;
a += 1; // a = a +1
```

#### 3.一元运算符

```JS
var a = 5;
alert(a++); 
/*
a=5 a++功能:对原有的变量进行+1操作
值:先取a的值作为a++表达式的值,再对a进行+1操作
*/				
alert(++a); 
/*
a=6 ++a 功能:对原有的变量进行+1操作
值:先对a进行+1操作,再取a的值作为a++表达式的值
*/
```

#### 4.关系运算

- 自动数据类型转换
  - 两个操作数都是数值,数值比较
  - 两个都是字符串,则比较字符编码表
  - 一个是数值,则另一个转换为数值进行比较
- 恒等 ===
  - true
    - 数值相同
    - 数据类型相同

#### 5.逻辑运算

- && 与运算
- || 或运算
- !    非运算

### (三)强制类型转换

#### 1.Boolean()

- 转换布尔值
- 数字非0即真

#### 2.Number()

- 转换为数字

#### 3.parseInt()

- 取整
- 可以转换进制

```JS
parseInt("110100",2);
//parseInt(str,str的进制)
```

#### 4.parseFloat()

- 转换为浮点数

### (四)流程控制语句

#### 1.选择语句if

```JS
if(条件1){
   表达式1
}else if(条件2){
   表达式2       
}else{
   表达式3
}
```

#### 2.选择结构switch

```JS
switch(表达式){
	case 常量1:
		.....;
		break;
	case 常量2:
		.....;
		break;
	...
	default:
		当上述所有的case选项都匹配失败,执行这里
		break;
}
```

#### 3.三目运算符

```JS
表达式1 ? 表达式2 : 表达式3;
```

- 先判断表达式1是否为真
- 1为真,执行2
- 1为假,执行3

#### 4.while循环

```JS
while(循环条件){
    循环语句;
}
```

#### 5.do...while循环

```js
do{
	语句1;
}while(循环条件);
```

#### 6.for循环

```js
var num=10
for(var i=0,i<=num,i++){
    语句;
    if(i==5){
        continue;//跳过这次循环
    }
    if(i==9){
        break;//跳出整个循环
    }
}
```

- break
  - 跳出循环
- continue
  - 跳过这一次循环

### (五)函数

#### 1.函数声明

```JS
function 函数名(参数){
	函数体;
    return 返回值;
}
```

#### 2.arguments

- arguments是用来存储实际传入的参数
- arguments.length
  - 参数个数
- arguments[下标]
  - 访问下标次序的数据

### (六)递归

#### 1.满足以下三个特点就是递归:

- 函数自己调用自己
- 一般情况有参数
- 一般情况下有return

#### 2.如何写递归?

- 首先去找临界值,即无需计算,获得的值
- 找这一次和上一次的关系
- 假设当前函数已经可以使用,调用自身计算上一次

#### 3.递归存在的问题

- 内存占用
- 内存瞬间占用和内存瞬间释放

### (七)数组

#### 1.创建数组

- 通过new创建数组对象

```JS
var arr = new Array(100,true,"hello")
```

- 省略new直接创建数组对象

```JS
var arr =Array(100,true,"hello")
```

- 数组常量进行赋值,用"[]"包裹

```JS
var arr = [100,true,"hello"]
```

#### 2.数组属性

- 数组.length
  - 返回值为数组中元素的个数

#### 3.访问数组

- 数组[i]

#### 4.数组的方法

##### 栈结构:

- push
  - 功能:在数组末尾依次加入元素
  - 返回值:push之后数组的长度
- pop
  - 功能:在数组末尾取出一个元素
  - 返回值:数组末尾的这个元素

##### 队列结构:

- push
  - 功能:在数组末尾依次加入元素
  - 返回值:push之后数组的长度
- shift
  - 功能:从数组的头部取下一个元素
  - 返回值:取下的元素
- unshift
  - 功能:从数组的头部插入元素
  - 返回值:插完元素以后数组的长度

##### 其他:

- concat

  - 功能:
    - 1.拷贝原数组,生成新数组
    - 2.合并数组
  - 返回值:合并成的新数组,原数组不会改变

- slice

  - 功能:提取元素,切片
  - 返回值:切片生成的新数组

- splice

  - 格式: arr.splice(start,end,data1,data2...);
    - start:插入/开始截取的位置
    - end:截取的长度
    - data1~datan:插入的元素
  - 功能:增删改
  - 返回值:新生成的数组

- join

  - 功能:将数组中的元素,用传入的拼接符,拼接成一个字符串(替换逗号拼接符)
  - 返回值:拼接好的字符串

- reverse

  - 功能:逆序

- sort

  - 功能:排序,默认按照字符串大小排序

  - 参数: 重写比较函数

  - ```JS
    arr.sort(function(value1,value2){
        return value2 - value1
    })
    ```

#### 5.数组的排序

##### 冒泡:

逐轮逐次左右两数对比进行换位操作

##### 选择:

对数进行比较并换位

#### 6.遍历数组

- 写for,while循环
- for....in快速遍历
- forEach方法

### (八)声明提升

- 在当前作用域,声明变量和函数,会直接提升在整个代码的最前面运行
  - 当前作用域
  - 变量
  - 函数

### (九)严格模式

```js
"use strict";
```

#### 1.作用域

写在哪个作用域下,在哪个作用域下生效

(尽量注意不要严格模式写在全局)

#### 2.变化

- 全局变量声明时,必须加var
- this无法指向全局对象
- 函数内重名属性会报错
- arguments对象不允许被动态改变
- 新增保留字:implements,interface,let,package,private,protected,public,static,yield

#### 3.新增数组方法

- indexOf()

  - 格式:数组.indexOf(item,start)
  - 参数
    - item 任意数据
    - start 下标,默认为0
  - 在数组中查找第一次出现item元素下表,从start开始去查找

- forEach()

  - 格式: arr.forEach(function(item,index,arr){....})

  - 功能:遍历数组

- map()

  - 格式:arr.map(function(item,index,arr){return ....;})
  - 功能:遍历数组

- filter()

  - 格式:arr.filter(function(item,index,arr){return ....;})
  - 功能:过滤

- some()

  - 格式:arr.some(function(item,index,arr){return ....;})
  - 功能:查找数组中是否有符合条件的数

- every()

  - 格式:arr.every(function(item,index,arr){return ....;})
  - 功能:查找数组中是否有不符合条件的数

- reduce()

  - 格式:arr.every(function(prev,next,index,arr){return ....;})
  - 参数
    - prev 上一次遍历return的值 
    - next 当前的遍历值
    - arr数组本身
    - index 索引值
  - 功能:归并计算

### (十)字符串

#### 1.概念

- 所有带单引号或者双引号的都叫做字符串
- 字符串是只读的,声明之后无法被修改

#### 2.声明字符串

- 1.通过new运算符去声明字符串
  - new String(str);
- 2.省略new声明字符串
  - String(str);
- 3.字符串常量赋值
  - var variable = "str";

#### 3.方法

- str.length
  - 访问字符串中字符的个数
- str.charAt(index)
  - 访问字符串中单个字符
  - index 下标
- document.write()中
  - big() 更大号字体
  - blink() 闪烁
  - bold() 粗体
  - fixed() 打字机文本
  - strike() 删除线
  - fontcolor() 颜色
  - fontsize() 尺寸
  - link() 链接
  - sub() 下标
  - sup() 上标
- charCodeAt(index)
  - 功能:访问字符串中对应下标字符的ASCII码值
- String.fromCharCode()
  - 功能:将传入的ASCII码值转成对应的字符
  - 返回值:组成的字符串
- indexOf(subStr,start)
  - 功能:查找字符串
  - 参数
    - subStr 查找的字符串
    - start 起始下标值
  - 返回值 -1 则表示没查找到
- lastIndexOf()
  - 反向查找
- search(subStr)
  - 参数:subStr(字符串/正则表达式)
  - 功能:在字符串中查找subStr第一次出现的位置
  - 正则修饰符 i 忽略大小写 g 全局匹配
- substring(start,end)
  - 功能:提取[start,end]这一段的字符,生成新字符串
  - 返回值:新字符串
- substr(start,length)
  - 提取字符串
  - 返回值:新字符串
- slice(start,end)
  - 功能:切割字符串
  - 返回值:新字符串
- replace(oldStr,newStr)
  - 用newStr将oldStr替换掉,生成新字符串
  - 参数
    - 第一个参数传入的是字符串只能替换一次
    - 第一个参数 正则表达式+g(全局匹配)则能全部替换
      - /str/g
  - 返回值:替换成的新字符串
- split(分隔符,length)
  - 参数
    - 分隔符
    - 控制返回的数组中包含子串的个数
  - 分割字符串,返回数组
- toLowerCase()
  - 转成全小写
- toUpperCase()
  - 转成全大写
- concat()
  - 拼接字符串

### (十一)对象

#### 1.声明对象

- new运算符

  - ```
    var obj1 = new Object();
    ```

    

- 省略new声明

  - ```
    var obj2 = Object();
    ```

    

- 对象常量赋值

  - ```
    var obj3 = {};
    ```

    

#### 2.新增属性

- ```js
  obj.attribute = value;
  ```

- ```
  obj['attributeName'] = value;
  ```

- ```JS
  var obj = {
  	attribute:value,
  };
  ```

  

#### 3.新增方法

- ```JS
  obj.fuc = function(){
  	.........;
  }
  ```

- ```JS
  obj['fuctionname'] = function(){
  	.........;
  }
  ```

- ```JS
  var obj = {
  	func:function(){
  		......;
  	},
  };
  ```

#### 4.调用属性/方法

```js
obj.attr;
obj['attr'];
obj.func();
obj['func']();
```

#### 5.删除属性/方法

```js
delete obj.attr;
delete obj.func;
```

#### 6.遍历

```js
var person ={
	uname:"name",
    sex:"female",
};
for(var i in person){
	person[i];        
}
```



### (十二)一些常用对象和函数

#### 1.Math

- 数学计算
- random 0-1之间随机数
- max(num,num1.....)
- min(...)
- abs()
- ceil() 向上取整
- floor() 向下取整
- pow(x,y)    x^y
- sqrt()
- sin(弧度)
- cos(弧度)
- PI   180弧度

#### 2.Date 日期对象

- 声明

  ```js
  //没有传入参数 默认当前系统时间
  var date = new Date();
  //传入参数
  var date = new Date("2000/01/01")
  var date = new Date(2000,1,1,)
  //传入时间戳
var date = new Date(1000)
  ```

- 格式化方法

  - toDateString()
  - toTimeString()
  - toLocaleDateString()
  - toLocaleTimeString()
  - toUTCString()

  - set/getFullYear() 年
  - set/getMonth() 月
  - set/getDate() 日
  - getDay() 周几
  - set/getHours() 
  - set/getMinutes()
  - set/getSeconds

- 其他方法

  - Date.parse() 转换时间戳
  - get/setTime() 获得/修改时间戳

#### 3.setInterval 定时器

- 每隔对应的毫秒数,执行一次传入的函数

- ```js
  var timer = setInterval(function,time)
  ```

- 返回值:启动定时器的,系统分配的编号

- clearInterval(timer) 取消定时器

### (十三)this关键字

- 每一个函数中都有一个内置的变量this,this指向当前函数的主人,函数的主人要根据上下文关系进行判断

#### 1.常见this

- 全局函数
  - 函数的主人
  - object Window
- 对象中的函数
  - 函数的主人
  - object 对象
- 对象.方法名 = 函数
  - 函数的主人
  - object 对象

#### 2.强制数据类型转换

- call
  - 格式:函数名.call();
  - 参数
    - 第一个参数:传入该函数this指向的对象
    - 第二个参数开始:将原函数的参数往后顺延一位
- apply
  - 格式:函数名.apply()
  - 参数
    - 第一个参数:传入该函数this指向的对象
    - 第二个参数:数组 数组,放入我们原有所有的参数
- bind
  - 预设this指向
  - 参数:传入该函数this指向的对象

## 三.BOM 浏览器对象模型

![image-20200315144653699](..\图片\image-20200315144653699.png)



### (一)window

(一般情况下window可以省略)

- onload
  - 把常量/变量/函数....等放到最后加载

- alert() 系统对话框1
- confirm() 系统对话框2
  - 确定或取消提示框
  - 返回 布尔值
- prompt() 带输入的提示框 系统对话框3
  - 参数1 面板上显示的内容
  - 参数2 输入框默认值
  - 返回值 取消=null,确定=输入内容

- open() 打开新窗口
  - 参数1 跳转url
  - 参数2 字符串 新窗口的名字(窗口对象的名字)
  - 参数3 一串特殊含义的字符串
    - 规定了装载到窗口的 URL 是在窗口的浏览历史中创建一个新条目，还是替换浏览历史中的当前条目

### (二)history

window.history

当前窗口的历史记录

- 属性
  - length
- 方法
  - back() 回溯到上一个url
  - forward() 前进到下一个url
  - go()
    - 参数: 0 刷新当前页面
    - 参数: 正/负整数 前进/后退n条记录

### (三)location

window.location = window.document.location

这两个是一个东西

- url:统一资源定位符
  - 协议://域名:端口/路径/?参数#锚点
  - protocol://hostname:port/pathname/?search#hash
- 属性
  - protocol 协议
  - hostname 域名/IP
  - port 端口
    - 浏览器 8080 http 80 https 443
  - pathname 路径
  - search 传递的参数
  - hash 锚点
  - href 完整url
- 方法
  - assign(url) 当前窗口跳转url
    - 产生历史记录
  - replace(url) 当前窗口url替换成新的url
    - 不产生历史记录
  - reload() 刷新当前窗口
    - 参数 true 不经过浏览器缓存强制从服务器重载

### (四).DOM document模型

![image-20200315161153950](..\图片\image-20200315161153950.png)

#### 1.节点类型

```HTML
<div id = 'div1'>div文本</div>
```



- 元素节点  <div></div>
  - nodeType:1
  - nodeName:标签名
  - nodeValue:null
- 属性节点 id = 'div1'
  - nodeType:2
  - nodeName:属性名
  - nodeValue:属性值
- 文本节点 div文本



#### 	2.获取元素节点的方法

- document.getElementById(id)

  - 通过id获取符合条件的元素

  - 返回值:符合条件的一个节点

  - ```js
    var attr = document.getElementById(id);
    attr.attrName; //根据该元素的属性获取值
    ```

- node.getElementsByTagName(TagName);

  - 可以通过节点嵌套查找

- node.getElementsByClassName(className);

  - 可以通过节点嵌套查找
  - IE8以下不兼容

- document.getElementsByName(name属性);

  - 一般使用在表单元素上
  - 不能获取下一节点的元素

- document.querySelector()
  - 参数:字符串 CSS选择器格式字符串
    - #idName id属性
    - tagName 标签名
    - .className class属性
    - [name = "hello"] 指定属性=xx
  - 返回值:一个元素节点,找到符合条件的第一个元素节点
  - IE8以下不兼容
- document.querySelectorAll()
  - 参数:字符串 CSS选择器格式字符串
    - #idName  id属性
    - tagName 标签名
    - .className class属性
    - [name = "hello"] 指定属性=xx
  - 返回值:类数组
  - IE8以下不兼容

#### 3.访问外部样式

- node.currentStyle['attrName']
  - IE
  - 获取样式
- getComputedStyle(node)["attrName"]
  - 火狐/谷歌
  - 获取样式

#### 4.行间属性增删改查

- 访问行间属性(getAttribute)
  - node.getAttribute("attrName");
- 修改行间属性
  - node.setAttribute("attrName");
- 删除行间属性
  - node.deleteAttribute("attrName");

#### 5.节点属性

- innerHTML 
  - 获取标签间内容 会解析标签
- innerText
  - 获取标签间纯文本 会省略标签 不解析标签
- outerHTML
  - 从外标签开始到外标签结束

#### 6.子节点方法

- childNodes
  - 所有子节点
  - 包含文本节点
- firstChild
  - 第一个子节点
  - 包含文本节点
- lastChild
  - 最后一个子节点
  - 包含文本节点
- nextSibling
  - 访问当前兄弟节点中的下一个节点
  - 包含文本节点
- previousSibling
  - 访问当前节点兄弟节点中的上一个节点
  - 包含文本节点
- 以下节点IE8以下不兼容,但是忽略文本
- children
- firstElementChild
- lastElementChild
- nextElementSibling
- previousElementSibling

--------------------------------------------------

- attributes
  - 获取当前元素节点上的所有的属性节点
  - getNamedItem("attrName")
  - ["attrName"] 效果同上
    - nodeName
    - nodeType
    - nodeValue

#### 7.节点操作方法

- document.write()
  - 覆盖原页面有的内容并写入新内容
- document.createElement()
  - 参数:标签名
  - 返回值:创建好的这个节点
- node.appendChild(node1)
  - 插入节点
- document.createTextNode()
  - 创建文本节点

- node.parentNode.insertBefore(newNode,node)
  - 将newnode插在node节点前

- node.parentNode.replaceChild(newNode,node)
  - newNode替换node
- node.cloneNode()
  - 拷贝节点
  - 参数: 如果是ture 则返回所有子孙节点
  - 返回值:一样的节点
- node.parentNode.removeChild(node)
  - 移除节点

#### 8.offset方法

- node.offsetwidth
- node.offsetheight
- node.offsetleft
- node.offsetright

#### 9.文档碎片

文档插入比在内存中节点插入耗费的计算时间长

## 四.事件

### (一)事件基础

#### 1.绑定事件

- 1.内联模式
  - 事件驱动指定的函数写在html元素行中
  - 函数的实现写在script中
- 2.外联模式/脚本模式(推荐)
  - 在script中指定html元素的事件驱动函数的实现

#### 2.绑定事件格式

元素节点.on + 事件类型 = 匿名函数

- 例如:
  - click 事件类型
  - onclick 事件处理的函数

### (二)事件类型

#### 1.鼠标事件

- click 单击
- dblclick 双击
- mouseover 鼠标移入
  - 经过子节点也会触发
- mouseout 鼠标移除
  - 经过子节点也会触发
- mousemove 鼠标移动(会不停的触发)
- mounsedown 按下
- mounseup 抬起
- mouseenter 鼠标移入
  - 经过子节点不会触发
  - 不支持IE8以下
- mouseleave 鼠标移出
  - 经过子节点不会触发
  - 不支持IE8以下

#### 2.键盘事件(表单元素,全局window)

- keydown 键盘按下
  - 按下不放手会一直触发
- keyup 键盘抬起
- keypress 键盘按下
  - 只支持字符键

#### 3.HTML事件

##### I.window事件:

- load
  - 页面加载完成以后触发
- unload
  - 页面解构的时候触发(刷新页面,关闭当前页面)
  - 兼容IE
- scroll
  - 页面滚动
- resize
  - 窗口大小发生变化的时候触发
- contextmenu
  - 右击菜单

##### II.表单事件:

- blur
  - 失去焦点
- focus
  - 获取焦点
- select
  - 在输入框中选中文本的时候触发
- change
  - 当我们对输入框的文本进行修改并且失去焦点的时候
- submit
  - 必须在form元素上
  - 点击submit上的按钮才能触发
- reset
  - 必须在form元素上
  - 点击reset上的按钮才能触发

### (三)事件对象和事件对象属性

#### 1.事件对象

- 概念
  - 事件绑定一旦完成的时候,生成一个事件对象
  - 触发事件的时候,系统会自动调用事件绑定的函数.将事件对象当作第一个参数传入. 

- 获取事件对象
  - argument 函数形参
  - window.event

![image-20200316173633853](..\图片\image-20200316173633853.png)

#### 2.事件对象属性

- button
  - 0 鼠标左键
  - 1 鼠标中键
  - 2 鼠标右键
- clientX,clientY
  - 获取鼠标位置
  - 原点:可视窗口的左上角
- pageX,pageY
  - 获取鼠标位置
  - 原点:页面的左上角
- screenX,screenY
  - 获取鼠标位置
  - 原点:屏幕的左上角
- shiftKey
  - 按下shift键为true,默认为false
- altKey
  - alt
- ctrlKey
  - ctrl
- metaKey
  - win/command键
- keyCode
  - 只在keydown下支持
  - 键码
  - 返回值:大写字母的ASCII码
  - which
    - var which = e.which || e.keyCode;
- charCode
  - 只在keypress下支持
  - 字符码
  - 返回值:字符码 区分大小写,当前按下对应字符的ASCII码
  - which
    - var which = e.which || e.charCode;
- target
  - 目标对象/出发对象
  - IE8以下不兼容 window.event.srcElement
- evt.cancelBubble
  - 取消事件冒泡
  - 默认值为false 若要取消则赋值true
- evt.stopPropagation();
  - 取消事件冒泡
- evt.preventDefault();window.event.returnValue=false;
  - 阻止默认行为
- document.documentElement.clientWidth/document.body.clientWidth
  - 当前窗口的宽
- document.documentElement.clientHeight/document.body.clientHeight
  - 当前窗口的高

#### 3.事件对象方法

- node.addEventListener()
  - node.attachEvent("on",evType,funcName)
    - 低版本IE兼容方法
  - 添加事件监听器
  - 参数
    - 1.事件类型
    - 2.绑定函数
    - 3.布尔值 true 事件捕获 false 事件冒泡 默认
- node.removeEventListener()
  - node.detachEvent("on"+evType,funcName)
    - 低版本IE兼容方法
  - 删除事件监听器
  - 参数
    - 1.事件类型
    - 2.要删除的函数

## 五.正则

### (一)声明对象

- 1.通过new去声明正则表达式
  - var box = new RegExp("hello","ig");
  - 参数1 正则主体 字符串
  - 参数2 修饰符
    - i 忽略大小写
    - g 全局匹配(不只匹配第一个)
    - m 换行匹配
      - 遇到换行符则重新开始计算行首
- 2.省略new声明
  - var box = RegExp("hello","ig");
- 3.常量赋值
  - var box = /hello/gi;

### (二)方法

#### 1.test

- 格式: 正则.test(字符串)
- 功能:在字符串中匹配这个正则是否存在
- 返回值:布尔值 存在=true 不存在=false

#### 2.exec

- 格式: 正则.exec(字符串)
- 功能:在字符串中匹配这个正则是否存在
- 返回值: 
  - 匹配成功:返回匹配到的字符串组成的数组
  - 匹配失败:null

### (三)字符串中可以使用正则的方法

#### 1.match

- 格式: 字符串.match(正则)
- 功能:在字符串中匹配是否有符合正则表达式的字符
- 返回值:
  - 匹配成功:返回匹配到的字符串组成的数组
  - 匹配失败:null

#### 2.replace

- 格式: 字符串.match(oldStr/正则,newStr)
- 功能:用newStr替换oldStr
- 返回值:替换后的字符串

#### 3.split

- 格式:字符串.split(分隔符/正则)
- 功能:分割字符串
- 分割剩下的子串的数组

#### 4.search

- 格式:字符串.search(子串/正则)
- 功能:找到符合条件的子串第一次出现的位置
- 返回值:
  - 找到:下标
  - 没找到:-1

### (四)元字符

#### 1.单个数字和字符

- .     匹配单个的任一字符
- [范围]    匹配单个范围内的字符
  - [0-9]  单个0-9的数字
  - [a-zA-Z0-9_] 匹配单个的数字,字母,下划线
  - \w  匹配单个的数字,字母,下划线
  - \W  匹配单个非数字,字母,下划线
  - \d  匹配单个数字 等价于[0-9]
  - \D  匹配单个非数字 等价于[ ^0-9 ]
- [^范围] 匹配单个范围内非括号内内容的字符

#### 2.重复字符 

x(任意的单个字符)

- x? 匹配0个或者1个x
- x+ 匹配之上一个x字符
- x* 匹配任意个x字符
- x{m,n} 匹配至少m个,最多n个x字符,包括n
- x{n} 必须匹配n个x字符
- (xtz)+ 小括号括起来的部门是当作单个字符处理

#### 3.空白字符

- \0 匹配null字符
- \b 匹配空格字符
- \f 匹配换页符
- \n 匹配换行符
- \r 匹配回车字符
- \t 匹配制表符
- \s 匹配任一单个的空白字符
- \S 匹配任意单个非空白字符

#### 4.锚字符

- ^ 行首匹配  必须以这个正则开头
- $ 行尾匹配  必须以这个正则结尾

#### 5.替代字符

- | 或

#### 6.转义字符

- \ .
- \ *

## 六.本地存储技术

### (一)简介

- localStorage
  - 永久存储
  - 最大可以存储5M    客户端的一个微型数据库
  - 只能存储string
  - IE8以下不兼容
- cookie
  - 可以设置过期时间
  - 最大可以存4kb
  - 每一个域名下面最多可以存储50条数据
- sessionStorage
  - talk值

### (二)对象的属性和方法

#### 1.localStorage

- setItem(key,value);
  - 存储键值对
  - 同样的方法:
    - localStorage.key= value
    - localStorage["key"] = value
- getItem(key);
  - 获取键对应的值
- removeItem(key);
  - 删除键值对

#### 2.cookie

- cookie字符串大致格式
  - "key1=value1;key2=value2......;keyn=valuen"

- 设置cookie
  - document.cookie = "key=value"
  - 中文处理
    - encodeURIComponent
      - 编码
    - decodeURIComponent
      - 解码
- 获取cookie
  - alert(document.cookie)
- 设置过期时间
  - expires 过期时间
  - document.cookie="key=value;expires=(date对象)"
- 可选项
  - path 限制访问路径
    - 默认当前html的路径
  - domain 限制访问域名
    - 默认当前html的服务器域名/IP
  - secure 安全
    - 设置了这个字段之后,只能通过https协议加载cookie

### (三)封装

#### 1.cookie

```js
//设置cookie
function setCookie(key,value,{expires,path,domain,secure}){
    var cookieStr = encodeURIComponent(key) + "=" +encodeURIComponent(value);
    if(expires){
        cookieStr += ";expires=" + afterOfDate(expires);
    }
    if(path){
        cookieStr += ";path=" + path;
    }
    if(domain){
        cookieStr += ";path=" + domain;
    }
    if(secure){
        cookieStr += ";secure";
    }
    document.cookie = cookieStr;
}
//获取cookie
function getCookie(name){
    var cookieStr = decodeURIComponent(document.cookie);
    var start = cookieStr.indexOf(name+"=");
    if(start==-1){
        return null;
    }else{
        var end = cookieStr.indexOf(";",start);
        if(end==-1){
            end=cookieStr.length;
        }
        var str = cookieStr.substring(start,end);
        var arr = str.split("=")
        return arr[1]
    }
}
//删除cookie
function removeCookie(name){
    document.cookie = encodeURIComponent(name)+"=;expires="+new Date(0);
}
```



## 七.ECMA6相关

### (一)变量

#### 1.声明变量

- let
  - 遇到大括号就形成作用域
  - 块级作用域
- constant
  - 变量值只能在声明的时候确定,后续是没有办法修改的
  - 声明常量

### (二)箭头函数

#### 1.概念

- 新潮的函数写法
- 例:var add = x => x+10
- 适当省略函数中的function和return关键字

#### 2.写法

```JS
//无参无返回值
var show = () => {
    alert("hello world");
}
//有参无返回值
var xxx = num =>{
    alert(num);
}
//有参有返回值
var add = x => {
    return x+10;
}

//多个参数,有返回值
var show = (x,y) =>{
    alert(x+y);
}
```

#### 3.实用场景

```JS
//数组条件过滤
var newArr = arr.filter(item => item>20);
//数组各数字变大
var newArr = arr.map(item => item*1.3);
```

#### 4.注意

- 箭头函数,不能用new
- 如果返回值是一个对象,一定要加();
- this指向上一层函数的主人

### (三)解构

#### 1.格式

- 中括号解构

```js
var [a,[b,c],d] = [1,[2,3],4];
```

- 大括号解构

```js
var {a,b,c} = {
	a:1;
    b:[2,3];
	c:"4";
}
```

#### 2.优点

```JS
//1.交换两个数
var [x,y] = [10,20];
[x,y] = [y,x];
//2.函数可以返回多个值
function show(){
    return ["a","b","c"];
}
var [a,b,c] = show();
//3.函数定义参数,和传入参数的顺序改变(参数可以有默认值)
function show({p1=0,p2=0,p3=0}){
    alert(p1+p2+p3);
}
show({
    p1:1;
    p2:2;
    p3:3;
});
//4.快速取出数组中的某一个元素
var arr = [10,20,30,40,50];
var {0:first,4:last} = arr;
// first = arr[0];last = arr[4]
```

### (四)字符串

#### 1.传统字符串

- 单引号
- 双引号

#### 2.ECMA6-反引号

- 换行,代码缩进都能在字符串中体现出来
- 格式化字符串
  - ${变量/表达式/函数调用}

```js
function showSelf({name,age,sex="男"}){
    alert(`我叫${name},今年${Math.max(age,20,30)}岁`);
}
```

### (五)数组和合并对象

#### 1.方法

- Array.from()

  - 伪数组转化真数组

- find()

  - 数组中查找符合条件的元素

  - ```JS
    //一般方法
    var res = arr.find(function(item,index,arr){
    	return item>20;
    });
    //箭头
    var res = arr.find(item => item>20);
    ```

- findIndex()

  - 找到元素的下标

  - ```JS
    var res = arr.findIndex(item => item>20);
    ```

- copyWithin

  - ```JS
    var arr = [1,2,3,4,5,6,7,8,9];
    arr.copyWithin(3,7,9);
    alert(arr);// result:1,2,3,8,9,6,7,8,9
    ```

  - 参数

    - 参数1:从哪个个下标开始
    - 参数2/3:范围[start,end]

  - 功能:将数组中指定index的对象换成数组[m:n]的对象

- Object.assign
  - 合并对象
  - 格式:Object.assign(obj1,obj2,obj3)
  - 将后面的对象全部合并到第一个对象中
  - 拷贝方式:浅拷贝
    - 数组等较为复杂的属性会直接拷贝内存地址
    - 数组属性更新后,合并的数组也会更新,但常量不会变

#### 2.遍历

- for循环
- for...in
- foreach
- for...of
  - for(var item of arr){}
  - item是当前遍历到的元素

### (六)集合set/map

集合:不重复/无序

#### 1.set

- 声明方法
  - new Set()
- 添加元素
  - add()
- 遍历
  - for(let item of imgs.keys()){...};
  - for(let item of imgs.values()){...};
  - for(let item of imgs.entries()){...};
  - for...of
- 数组变集合
  - var set = new Set([10,20,30,40,50,40]);
- 集合变数组
  - var arr = [...set];

#### 2.map

- 声明map

  - new Map();

- 添加数组

  - map.set(key,value)

- 取值

  - map.get(key)

- 遍历

  - ```js
    for(let [key,value] of map){
        console.log(key,value);
    }
    ```

  - for....of

### (七)对象

#### 1.构造函数

- 通过new调用函数
  - this.property
  - this.function
  - 省略声明对象
  - 省略return值语句

#### 2.原型对象(封装)

- 每一个函数上,都有一个原型对象prototype

- prototype用在构造函数上,可以给构造函数的原型prototype,添加方法

- 例:

  ```js
  object.prototype.function = function(){
      ......;
  }
  ```

  

#### 3.继承

- 原型链继承

```JS
function Dog({name,type,age}){
    this.name = name;
    this.type = type;
    this.age = age;
}
Dog.prototype = {
    run: function(){
      alert(this.name);  
    },
    showSelf: function(){
        alert(1);
    }
}

function Teddy({name,type,age,color}){
    Dog.call(this,{
        name:name,
        type:type,
        age:age,
    })
    this.color = color
}

for(var funcName in Dog.prototype){
    Teddy.prototype[funcName] = Dog.prototype[funcName;]
}

Teddy.prototype.showcolor = function(){
    alert("color");
}
```

#### 4.多态(重写)

```JS
//继上面的代码块
Teddy.prototype.shoSelf = function(){
    alert(2);
}
```

### (八)原型详解

#### 1.\__proto__

和object.prototype作用相同

#### 2.instanceof

- 判断某一个对象是否是这个构造函数构造的
- 格式: obj1 instanceof Obj;
- 返回布尔值

### (九)class

```JS
//构造一个类
class FatherObject{
    //构造器
    constructor(parameter1,parameter2){
        this.attr1 = parameter1;
        this.attr2 = parameter2;
    }
    //类函数
    testFunc(){
        .....;
    }
}
//类继承 extends
class SonObject extends FatherObject{
    //重写构造器
    constructor(parameter1,parameter2,parameter3){
        super(parameter1,parameter2);
        this.attr3 = parameter3;
    }
}
```

### (十)回调函数

```js
function funcName(){
    ....;
}
//回调函数
function funcName2(funcName){
    funcName();
}
```



## 八.动画

### (一)运动框架

- 1.每次启动定时器之前,先将上一次定时器关闭

- 2.if....else 将运动和停止分开

- getStyle 浏览器兼容 获取对象有效样式

  - ```JS
    function getStyle(node,cssStr){
        return node.currentStyle ? node.currentStyle[cssStr] : getComputedStyle(node)[cssStr];
    }
    ```

    

### (二)部分运动

#### 1.匀速运动

- 1.每次启动定时器之前,先将上一次定时器关闭
- 2.if....else 将运动和停止分开

#### 2.分享到菜单 淡入淡出

- CSS透明度设置
  - opacity:0.3; filter:alpha{opacity=30};

#### 3.缓冲运动

- var speed = (iTarget - iCur) / 8;
  - 除8比较好
- 元素的样式识别不了小数位数,故需要向上/向下取整

#### 4.缓冲菜单(页面居中)



```JS
//获取居中top值
var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;//当前窗口的top值
var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;//当前窗口的高
```

- window.onscroll;
- window.onresize;

#### 5.多物体运动;

- 不能共用同一个timer
- 不能共用同一属性

#### 6.链式运动

- 一个动作完成后再执行另一个动作
- 运用回调函数来进行封装

## 九.后端交互

### (一)ajax

#### 1.概念

- 异步的javascript和xml(数据传输)
- ajax是前后端数据交互的搬运工
- xml
  - 优点
    - 种类丰富
    - 传输量非常大
  - 缺点
    - 解析麻烦
    - 不适合轻量级数据
- json
  - 优点
    - 轻量级
    - 解析比较轻松
      - JSON.parse()
      - JSON.stringify()
  - 缺点
    - 数据种类比较少
    - 数据量比较小

#### 2.ajax基础操作

```JS
/*
	XMLHttpRequest IE8以下不兼容
	IE8以下声明ajax对象:
		ActiveXObject("Microsoft.XMLHTTP");
*/
//1.创建ajax对象
var xhr = null;
if(windows.XMLHttpRequest){
    xhr = new XMLHttpRequest();
}else{
    xhr = new ActiveXObject("Microsoft.XMLHTTP");
}
//1.1创建ajax对象另一种写法
var xhr = null;
try{
    xhr = new XMLHttpRequest();
}catch(error){
    xhr = new ActiveXObject("Microsoft.XMLHTTP");
}

//2.调用open
/*
	参数1: 请求方式 get post....
	参数2: url
	参数3: 是否异步 true是 false否
*/
xhr.open("get","1.txt",true);
//3.调用send
xhr.send();
//4.等待数据响应
xhr.onreadystatechange = function(){
    if(xhr.readyState == 4){
        alert(xhr.responseText);
    }
}
```

#### 3.异常捕捉

```js
try{
    ......;
    throw new error("string");
}catch(error){
    ......;
}
```

#### 4.readystatechange

- onreadystatechange 事件
  - readyState属性: 请求状态
    - 0 初始化 还没有调用open
    - 1 载入 已调用send() 正在发送请求
    - 2 载入完成 send()方法完成,已收到全部响应内容
    - 3 解析 正在解析响应内容
    - 4 完成 解析完成,可以在客户端调用了
  - status属性:状态码
    - 2XX
    - 3XX
    - 4XX
    - 5XX

#### 5.ajax_GET;ajax_POST

- form表单
  - action 点击submit以后跳转的url
  - method 表单的提交数据的方式
    - get
    - post
  - enctype
    - post需求的参数
    - "application/x-www-form-urlencoded"

- ajax
  - get
    - xhr.open("get","url",true);
    - url和参数写在xhr.open()的第二个参数中
  - post
    - xhr.open("post","url",true);
    - 在send方法前 设置请求的格式
      - xhr.setRequestHeader("content-type","application/x-www-form-urlencoded")
    - xhr.send("params=....&....")
    - url写在xhr.open;参数写在xhr.send

#### 6.ajax函数封装

```js
/*
	method
	url
	data
*/
function $ajax({method="get",url,data,success,error}){
    //1.创建ajax对象
    var xhr = null;
    try{
        xhr = new XMLHttpRequest();
    }catch(error){
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    //data转化成参数字符串
    if(data){
        data = queryString(data);
    }
    
    //2.open
    if(method == "get" && data){
        url += "?" + data;
    }
    xhr.open(method,url,true);
    
    //3.send
    if(method == "post"){
        xhr.setRequestHeader("content-type","application/x-www-form-urlencoded")
        xhr.send(data);
    }else{
        xhr.send();
    }
}
	//4.等待数据响应
	xhr.onreadystatechange = function(){
        if(xhr.readyState == 4){
            //这里还需要判定一下状态码 xhr.status
            if(xhr.status==200){
                if(success){
                    success(xhr.responseText);//处理数据,回调函数;
                }
            }else{
                if(error){
                    error("Error:"+xhr.status);
                }
                
            }
            
        }
	}
```

#### 7.将对象转成查询字符串

```js
function queryString(obj){
    var str = "";
    for(var attr in obj){
        str += attr+"="+obj[attr]+"&";
    }
    return str.substring(0,str.length - 1);
}

//调用例子
var str = queryString({
    name1:"value1";
    name2:"value2";
});
```

### (二)JSON对象

#### 1.概念

字符串的一种格式

#### 2.转换方法

- JSON.stringify()
  - 数据结构 => 字符串;数据转换为json
- JSON.parse()
  - 字符串 => 数据结构;解析json为数据

#### 3.前后端交互的流程:

- 1.通过ajax下载数据
- 2.分析数据,转成对应数据结构
- 3.处理数据

### (三)JSONP跨域

ajax只能下载同源的数据,跨源数据禁止下载

#### 1.同源策略

- 1.同协议
- 2.同域名/同IP
- 3.同端口号

#### 2.跨源的方式

- 1.修改ajax同源协议(不建议)
- 2.委托php(后端服务器)进行跨源
- 3.JSONP()
  - 利用函数的形参获得数据

#### 3.简单的JSONP用法

现在外部写一个js文件,如下:test.js

```JS
//函数名(实际数据)
download("I am a string")
```

在HTML中引入该js文件,并将函数补完:

```HTML
<script>
    function download(data){
        alert(data);
    }
</script>
<script src="test.js"></script>
```

#### 4.JSONP跨域主要问题

- 1.在需要的时候加载数据
  - 自行生成元素并给元素添加src属性
  - 绑定到事件上
- 2.能否引入除.js文件以外的其他路径
  - 能

#### 5.使用流程

- 1.先去生命一个函数,这个函数有一个形参,这个形参会拿到我们想要的下载数据,使用这个参数做后续数据的处理
- 2.在需要下载数据的时候,动态创建script标签,将标签src属性设置成,下载数据的连接
- 3.当script插入到页面上的时候,就会,调用已经封装好的函数,将我们需要的数据传过来

## 十.其他

### (一)网络传输协议

- ISO 7层网络分层
- 通用 5层网络分层
  - 应用层
  - 传输层
    - Port
    - 协议:TCP/UDP
  - 网络层
    - IP
  - 数据链路层
  - 物理层

![image-20200323174029256](..\图片\image-20200323174029256.png)

#### 1.TCP协议

- 面向链接协议
- 传输数据:
  - 1.建立连接  三次握手
  - 2.传输数据
  - 3.断开连接  四次挥手
- 优点:
  - 安全
  - 准确度高
- 缺点:
  - 传输效率低
  - 耗资源

![image-20200323174109278](..\图片\三次握手.png)

![image-20200323174251940](..\图片\四次挥手.png)

#### 2.UDP协议

- 传输数据
  - 直接传,根本不管是否收到数据
- 缺点
  - 不安全
  - 准确度非常低
  - 经常丢包
- 优点
  - 及时性非常高
  - 消耗资源低

### (二).闭包

#### 1.概念

- 满足以下特点的叫闭包:
  - 函数嵌套函数
  - 内部函数使用外部函数的形参和变量
  - 被引用的形参和变量就不会被垃圾回收机制所回收

- 好处
  - 希望一个变量常驻在内存当中
  - 避免全局变量污染  避免声明全局变量
  - 可以声明私有成员
- 缺点
  - 内存泄露

#### 2.简单例子

```js
//局部变量a可以被累加
function aaa(){
    var a=2;
    function bbb(){
        a++;
        alert(a)
    }
    return bbb;
}
```

#### 3.立即执行函数例子

```js
//立即执行函数
(function(){
    alert("hello world");
})();

//闭包+立即执行函数
var ccc = (function(){
    var a=2;
    return function(){
        a++;
        alert(a);
    }
})();

ccc();
ccc();
```

