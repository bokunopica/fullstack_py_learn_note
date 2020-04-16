# Bootstrap

## 部署

参考官方文档:https://v3.bootcss.com/





# JQuery

文档:https://jquery.com/

中文文档:https://www.jquery123.com/  | https://www.runoob.com/jquery/jquery-tutorial.html



版本区别:

- 1.0 兼容IE8以下
- 2.0 只兼容IE8以上
- 3.0

## 一.入门

### (一)选择元素

#### 1.模拟css-selector选择元素

```javascript
// 标签id
$("#id").css("backgroundColor","red")
// 标签class
$(".class")
// 嵌套 空格分隔
$("ul li")
// 标签name
$("[name=xxx]")
```

#### 2.独有表达式写法

```js
//:表达式
// first
$("li:first")
// last
$("li:last")
// even 下标为偶数 odd 下标为奇数
$("li:even")
// eq()指定下标
$("li:eq(1)")
```

#### 3.多种筛选方式

```js
// eq()指定下标 放在$()外
$("li").eq(2)
// filter()
$("li").filter(".box")
```

### (二)写法

#### 1.方法函数化

```js
// window.onload
$(function(){...})
// 事件绑定
$("h1").click(function(){...})
```

#### 2.链式操作

#### 3.取值赋值合体

```js
// html() 
// 获取innerHTML内容
$("#div1").html()
// 修改innerHTML内容
$("#div1").html("<h1>在修改了</h1>")
// val()
// 获取/修改value值
$("input").val()
$("input").val("new value")
```

## 二.主体

### (一)方法

#### 1.节点操作方法1

- filter()
  - 过滤 对已经获取到的网页元素进行过滤

- not()
  - filter反义词
- has()
  - 拥有,直接判定子节点中是否有符合条件的元素

```js
$("div").filter(".class")
$("div").not(".class")
$("div").has(".class")
```

- prev()
  - 上一个节点
- next()
  - 下一个节点

```js
$("div").prev()
$("div").next()
```

- find()
  - 查找子节点

```js
$("ul").find("li")
```

- eq()
  - 通过下标获取指定的元素节点
- index()
  - 当前节点在兄弟节点中的下标

```js
$("h3").index()
$("li").eq(3)
$("li:eq(4)")
```

- attr()
  - 获取/设置/修改行间属性

```js
// 获取
$("#div").attr("title")
// 修改单个属性
$("#div").attr("title","value")
// 修改多个属性
$("#div").attr({
    "title":"value1",
    "class":"value2",
})
```

- addClass()
  
  - 增加class
- removeClass()
  
  - 移除class
- width()
  
  - 获取width
- innerWidth()
  
  - 获取width+padding
- outerWidth()
  - 获取width+border+padding
  - 参数true
    - 获取width+border+padding+margin
- height()
  
  - 获取height
- innerheight()
  
  - 获取height+padding
- outerheight()
  - 获取height+border+padding
  - 参数true
    - 获取height+border+padding+margin
- insertBefore()
  
  - 指定节点插入到另一个指定节点前面
- insertAfter()
  
  - 指定节点插入到另一个指定节点后面
- appendTo()
  
  - 指定节点插入到另一个指定节点的子节点末尾
- prependTo()
  
  - 指定节点插入到另一个指定节点的子节点首位
- remove()
  
  - 删除节点
- before()
  - 另一个指定节点插入到指定节点前面
  - insertBefore相反
- after()
  - 另一个指定节点插入到指定节点后面
  - insertAfter相反
- append()
  
  - 指定节点的子节点末尾插入到另一个指定节点
- prepend()
  
- 指定节点的子节点首位插入到另一个指定节点
  
- on()

  - 节点添加事件
  - 事件委托
    - 新创建的元素也能够有事件

  

```js
// 给一个事件添加一个函数
$("div").on("click",function{
	alert("hello");
})
// 给多个事件添加一个函数,多个事件中间用空格分隔
$("div").on("click mouseover",function{
	alert("hello");
})
// 给不同时间添加不同的函数
$("div").on({
    "click":function(){
        alert("hello");
    },
    "mouseover":function(){
        alert("world");
    }
})
// 事件委托
/*
	第二个参数是触发对象的选择器
*/
$("ul").on("click","li",function(){
	$(this).css("backgroundColor","red");
})

// 新增节点
$("#btn1").click(function(){
    $('<li>added</li>').appendTo($("ul"));
})
```

- off()
  - 取消事件

```js
// 取消全部事件的函数
$("#div1").off();
// 取消某一事件下的函数
$("#div1").off("click");
// 取消某一事件下的指定函数
$("#div1").off("click",show);
```

- scrollTop()
  - 滚动条最高点的高度
- ev
  - 事件
  - 事件操作坐标
    - pageX,pageY (带滚动条距离)
    - clientX,clientY (可视窗口)
  - 事件的详细按键
    - button
    - keydown
    - keypress
- preventDefault
  - ev.preventDefault
  - 阻止默认行为
- stopPropagation
  - ev.stopPropagation
  - 阻止事件冒泡

```js
// 阻止事件冒泡
$(function(){
    $("div").click(function(ev){
        alert(this.id);
        ev.stopPropagation();
    // 阻止默认行为+事件冒泡
    $("a").click(function(ev){
        ev.preventDefault();
        ev.stopPropagation();
    })
    // 阻止默认行为+事件冒泡的简单写法
    $("a").click(function(ev){
        return false;
    })
})
```

- offset
  - 直接获取当前元素,距离最左边/上边的距离,margin不算数
  - left
  - top
- position()
  - 直接获取,当前元素,距离第一个有定位父节点的距离,margin算在内
  - left
  - top
- offsetParent()
  - 查找第一个有定位的父节点,如果父节点没有定位就继续往上去找,最终找到html节点



- val()
  - 获取/设置表单元素的值
  - 取值时只能取到第一个符合条件的元素的值
  - 赋值时会设置所有符合条件的元素的值

```js
$("input").each(function(index,item){
    $(item).val(index);
})
```



- size()
- length

#### 2.特效/动画函数

- hover(funcOver,funcOut)
  - 移入移出特效
- hide()/show()
  - 隐藏:左上角收起;显示:左上角展开
  - 参数1:动画持续的毫秒数
  - 参数2:回调函数,动画结束时执行
- slideDown()/slideUp()
  - 隐藏/显示:卷闸效果
  - 参数1:动画持续的毫秒数
  - 参数2:回调函数,动画结束时执行
- fadeIn()/fadeOut()
  - 淡入/淡出
  - 参数1:动画持续的毫秒数
  - 参数2:回调函数,动画结束时执行

- fadeTo()
  - 透明度变化
  - 参数1:动画持续的毫秒数
  - 参数2:透明度变化的target
  - 参数3:回调函数,动画结束时执行

- animate
  - 参数1:元素的属性变化目标值
  - 参数2:持续时间
  - 参数3:运动形式
    - "swing" 默认 慢快慢
    - "leaner" 匀速
  - 参数4:回调函数
  - 拓展更多animate运动形式
    - 引入jquery-ui
    - https://www.jqueryui.org.cn/demo/5735.html 查找动画特效
    - 引入jquery-ui之后 addClass方法和removeClass方法也可以变成动画
- stop()
  - 停止动画
  - 建议在调用动画前调用stop
  - 参数1:true
    - 停止后续所有动画
  - 参数2:true
    - 停止所有动画,且当前正在进行的动画直接到达目的值
- finish()
  - 停止所有动画,并且所有动画到达目的值
- delay()
  - 动画执行延迟时间

#### 3.节点操作方法2

- remove()
  - 删除元素节点
  - 返回值:删除的节点
  - 不会保留删除的元素上原有的事件和行为
- detach()
  - 删除元素节点
  - 保留删除的元素上原有的事件和行为
- ready() 事件
  - $(document).ready()
    - 事件触发在当前的document加载完成以后执行
    - document加载完毕肯定是在window加载完毕之前
- html()
  - 元素的标签间的内容
  - 修改元素内部文本,读取标签内容
- text()
  - 获取元素的标签间的纯文本
  - 修改元素内部为纯文本

- siblings()
  - 获取除当前节点外,所有的兄弟节点
- nextAll()
  - 获取接下来的所有兄弟节点
- prevAll()
  - 获取上面的所有兄弟节点
- parentsUntil()
  - 获取从目前节点到指定的父节点之间所有的节点
- nextUntil()
  - 获取从目前节点到下面的指定节点之间所有的节点
- prevUntil()
  - 获取从目前节点到上面的指定节点之间所有的节点
- parent()
  - 获取父节点
- parents()
  - 获取所有父节点
  - 加css选择器参数进行筛选
- closest()
  - 必须传递参数,css选择器
  - 只获取父节点中第一个符合条件的元素

- wrap()
  - 每一个获取到的元素节点单独包装

```js
$("span").wrap("<p class='box' title='hello';></p>")
```

- wrapAll()
  - 获取到的元素节点整体包装
- wrapInner()
  - 内部包装
  - 往节点里面塞东西
- unwrap()
  - 删除包装
  - 删除上面一层包装,不包括body节点
- clone()
  - 克隆节点本身,不带事件和行为
  - 参数true
    - 完全克隆
- add()
  - 将多个选择器拼接在一次
- slice(start,end)
  - [start,end)
  - 获取指定范围内获取到的元素节点
- serialize()
  - 将表单中的数据拼接成querystring(查询字符串)
- serializeArray()
  - 将表单数据拼接成数组
- trigger()
  - 主动触发事件
  - 可以触发官方定义的事件以外,还可以触发自定义的事件
- ev.data
  - 事件参数对象

```js
$("button").on("click",{username:"name",age:"age"},function(ev){
    alert(ev.data); //拿到传入参数
})
```



- ev.target
  - 事件触发对象
- ev.type
  - 输出事件类型

#### 4.工具方法

调用方法:$.func()

- type()
  - 输出当前数据类型
- trim()
  - 去除字符串首尾空格
- inArray()
  - 查找对象在数组中的位置
  - 参数1:查找的对象
  - 参数2:数组
- proxy()
  - 改变上下文语境
  - this
- noConflict()
  - 给$函数起别名,用别名调用jq函数
- parseJSON()
  - 解析JSON
- makeArray()
  - 伪数组转数组

#### 5.插件方法

调用方法:$.func()

- extend()
  - 拓展工具方法
  - $.xxx()
- fn.extend()
  - 拓展JQ方法
  - 要实现链式操作的话要return回原先操作的节点

```js
// 添加工具方法
$.extend({
    aaa:function(){
        alert("工具方法");
    },
})
// 添加方法
$.fn.extend({
    aaa:function(){
        alert("工具方法");
    },
})
// 调用
$.aaa();
$("div").aaa();
```

#### 6.cookie/ajax

cookie需要引入jquery.cookie.js

- $.cookie()
  - $.cookie(name) 通过name取值
  - $.cookie(name,value) 设置name和value
  - $.cookie(name,value{可选项})
    - expires 数值 过期时间
    - raw 布尔值 value是否不进行编码
  - $.cookie(name,null) 删除cookie

```js
$.cookie("key","value",{
    expires:7
})
```



- $.ajax()

```js
// 一般请求
$.ajax({
	type:"get",
    url:"1.txt",
    data:{
        
    },
    success:function(data,statusText,xhr){
        alert(data+","+statusText);
    },
    error:function(msg){
        alert(msg);
    }
})

// 跨域请求 指定dataType字段
$.ajax({
	type:"get",
    url:"https://api.asilu.com/weather/",
    data:{
        city:"青岛"
    },
    dataType:"jsonp",
    success:function(data,statusText){
        console.log(data);
    },
    error:function(msg){
        alert(msg);
    }
})

```

- load()
  - $("div").load("url")
    - 将url传入以后,将下载到的数据直接填充到被选中元素的innerHTML中
  - $("div").load("url",function(data,status,xhr){ .... })
    - 回调函数
    - data:下载到的数据
    - statusText 下载的状态 success error
    - xhr ajax对象
      - xhr.status  网络状态码

- get()
  - get请求
- post()
  - post请求

```js
// load()
$("div").load("url",function(data,status,xhr){
    alert(data)
})
// get()
$.get("url",function(data,statusText,xhr){
    alert(data);
})
// post()
$.get("url",{
    username:'bbb',
    age:19,
    password:"123456",
},function(data,statusText,xhr){
    alert(data);
})
```
