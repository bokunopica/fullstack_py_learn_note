# HTML+CSS+JS

## 一.HTML5

### 元素:

![html元素](图片\QQ图片20200304133430.png)

```
<html>文档中html部分的开始
```

### 语义元素:

#### 1.a 超链接

```html
<a href="url" target="_blank">Text<a>
```

- href
  - 指定超链接url
- target
  - _self 在本标签页中打开url
  - _blank 新建标签页打开url
  - 默认值为_self

#### 2.b 粗体

```HTML
<b>Text</b>
```

#### 3.em 斜体

```HTML
<em>Text</em>
```

#### 4.u 下划线 (不推荐)

```html
<u>Text</u>
```

#### 5.删除线

```html
<s>Text</s>
```



### 表格:

#### 6.table tr td 表格

```html
<table border="1px">
    <thead>
    <tr>
        <th>ColumnName</th>
        <th>ColumnName</th>
    </tr>
    <thead>
    <tbody>
	<tr>
        <td>Text</td>
        <td>Text</td>
    </tr>
    <tr>
        <td>Text</td>
        <td>Text</td>
    </tr>
    </tbody>
    <tfoot>
    <tr>
        <td>ColumnName</td>
        <td>ColumnName</td>
    </tr>
    <tfoot>
</table>
```



- table
  
  - border
    - 表格边界粗细
  
  - <thead>
    - 表头
  - <tbody>
    - 表内容
  
  - <tfoot>
    - 表脚
  - td
    - colspan
      - 合并行单元格
      - default=1
    - rowspan
      - 合并列单元格
      - default=1

#### 7.br 换一行

```html
<br>
```

#### 8.ol 有序列表

```html
<ol type="A">
    <li>text</li>
        <ol type="a">
            <li>text</li>
            <li>text</li>
            <li>text</li>
   		</ol>
    <li>text</li>
    <li>text</li>
</ol>
<ol reversed>
    <li>text</li>
    <li>text</li>
    <li>text</li>
</ol>
```

- reversed
  - 降序
  - 无需赋值
- type
  - 序号类型
  - default="1"



#### 9.ul 无序列表

```HTML
<ul>
    <li>text</li>
    <li>text</li>
    <li>text</li>
</ul>
```



#### 10.li 表示列表中的项

### 表单元素:

#### 1.form

```html
<form></form>
```

#### 2.input

```HTML
<form>
    <input type="text"><!--单行文本框-->
    <br><br>
    <input type="text" value="Text">
    <br><br>
    <input type="text" placeholder="Hint" maxlength="8">
    <br><br>
    <input type="text" placeholder="Hint" size="50">
    <br><br>
    <input type="text" value="Text" readonly>
    <br><br>
    <input type="text" placeholder="Hint" maxlength="8">
</form>
```



- type

  - 表单输入格式

  - 参数值

    - text 文本

    - password 密码

    - button 按钮

      -  与js合作作为绑定事件
      - type
        - onclick

    - submit 提交表单

    - range 滑条

    - number 数值

    - checkbox 方勾选框

    - radio  圆勾选框

    - list 选择的数据列表

    - email 邮件

    - tel 电话

    - url 链接

    - date 日期

    - color RGB颜色

    - search 搜索

    - hidden 隐藏数据项

    - image 图片按钮

    - file 文件

      



type=="text":

- value
  - 填充默认值
  - 占位符
- placeholder
  - 输入提示
- maxlength
  - 最大长度
- size
  - 文本框可见的字符数目
- readonly
  - 不需要赋值
  - 不能修改文本
  - 只读

- method
  - 请求类型
  - 参数值
    - get
    - post
    - put
    - .....

- action
  - 接口操作



type==range,number:

- min
  - 最小值
  - 数值
  - default=0
- max
  - 最大值
  - 数值
  - default=100
- step
  - 滑动单位
- value
  - 起始值
  - 数值
  - default=0

type==radio

```HTML
<input type="radio" value="text" name="a">
<input type="radio" value="text" name="a">
<input type="radio" value="text" name="a">
```

- name
  - 单选 选择分支
- checked
  - 默认选择项

type==image

```HTML
<input type="image" src="imageDir" width="20px">
```



- src
  - 图片路径
- width
  - 宽度

type==file

- Multiple
  - 一次允许上传多个文件
- Required
  - 必须上传一个文件
- enctype
  - multipart/form-data
  - 必须有这个属性

#### 3.textarea 多行表单

```html
<form>
    <textarea rows="20">longtext</textarea>
</form>
```

- rows
  - 行长度

- cols
  - 列长度

#### 4.button 按钮



#### 5.select 选项

```HTML
<select>
	<option>text</option>
    <option>text</option>
    <option>text</option>
</select>
```

#### 6.datalist 数据列表

```HTML
<input type="text" list="datalist">
<datalist id="datalist">
	<option>text</option>
    <option>text</option>
    <option>text</option>
</datalist>
```

- id
  - datalist_id

### 图片:

#### 1.img 创建图片

```HTML
<img src="xxx.png" width="128px" height="128px" alt="text">
```

- src
  - url 图片地址
- width
  - 图片宽度
- height
  - 图片高度
- alt
  - 备用内容(图片加载失败时显示)
- usemap
  - 分区响应图
  - 需要指定map名称,名称前加#



#### 2.map 分区响应图

- name
  - map名称

#### 3.area 分区响应图区域

```HTML
<map name="map1">
	<area href="url1" shape="Rect" coords="左边缘,上边缘.右边缘,下边缘" target="_blank">
	<area href="url2" shape="" coords="">
    <area href="url3" shape="" coords="">
    <area href="url4" shape="" coords="">
    <area href="url5" shape="" coords="">
</map>
```

- href
  - url
- alt
  - 备用内容
- shape
  - Rect 矩形区域
    - coords指定数值"x,y,z,a"
    - x = 图像左边缘
    - y = 图像上边缘
    - z = 图像右边缘
    - a = 图像下边缘
  - Circle 圆形区域
    - coords指定三个值"x,x,x"
    - x = 图像左边缘到圆心的距离
    - y = 图像右边缘到圆心的距离
    - z = 圆的半径
  - Poly 多边形
    - coords指定数值"x1,y1,x2,y2,x3,y3,..."
    - n组坐标xn,yn
  - Default 默认图片区域

- coords
  - 确定分区区域

### 视频/音频:

#### 1.video

```HTML
<video src="url" autoplay></video>
```

- src
- height
- width
- autoplay
  - 不需要指定值
  - 自动播放
- preload
  - 预先载入视频
  - default = Auto
  - Auto
    - 请求下载整个视频
  - None
    - 不会载入
  - Metadata
    - 只载入第一帧
- controls
  - 控制栏
  - 不需要指定值
- loop
  - 视频循环播放
- poster
  - 视频载入时显示图片
- muted
  - 视频静音

#### 2.source 视频/音频分类

```HTML
<video>
	<source src="xxx.mp4" type="video/mp4">
</video>
```

在<video></video>

或者<audio></audio>元素中插入元素source

- src

- type
  - video/mp4
  - video/ogg
  - audio/mpeg
  - audio/ogg

#### 3.audio 音频2

```HTML
<audio src="url" autoplay></audio>
```

- src
- autoplay
- controls
  - 控制栏

## 二.CSS

### 1.最基础的CSS元素及属性

- sytle元素

  - font-size 设置文本大小的属性
  - color 设置文本颜色的属性

  ```HTML
  <a style="font-size:40px;color:#ffad2a">Text</a>
  ```

  

### 2.制作一个初级CSS设计

#### 1.使用元素内嵌样式表

- ```HTML
  <a style="font-size:40px;color:#ffad2a">Text</a>
  ```

#### 2.使用文档内嵌样式表

- 在head标签中写样式表

- ```HTML
  <head>
      <style type="text/css">
          a{
              font-size:40px;
              color:#345cff;
          }
      </style>
  </head>
  ```

  a标签样式表

- a -> * 所有元素

#### 3.使用外部样式表

- 在head标签中导入样式

- ```HTML
  <link rel="stylesheet" type="text/css" href="{指定url}">
  ```

#### 4.优先级

- 1 元素内嵌
- 2 文档内嵌
- 3 外部

### 3.使用CSS选择器

- 选择所有元素

```HTML
<head>
    <style type="text/css">
        *{
            font-size:40px;
            color:#345cff;
        }
    </style>
</head>
```

- 根据类型选择元素

```HTML
<head>
    <style type="text/css">
        a{
            font-size:40px;
            color:#345cff;
        }
    </style>
</head>
```

- 根据类选择元素

```HTML
<head>
    <style type="text/css">
        .className{
            font-size:40px;
            color:#345cff;
        }
    </style>
</head>
<body>
    <a class="className">Text</a>
</body>
```

- 根据id选择元素
  - id是唯一身份标志 
  - 不推荐一个id给多个标签使用

```HTML
<head>
    <style type="text/css">
        #idName{
            font-size:40px;
            color:#345cff;
        }
    </style>
</head>
<body>
    <a id="idName">Text</a>
</body>
```

- 根据属性选择元素

```HTML
<head>
    <style type="text/css">
        [href]{
            font-size:40px;
            color:#345cff;
        }
    </style>
</head>
<body>
    <a href="url">Text</a>
</body>
```

- 根据属性与属性值选择元素

```HTML
<head>
    <style type="text/css">
        [href="url"]{
            font-size:40px;
            color:#345cff;
        }
    </style>
</head>
<body>
    <a href="url">Text</a>
</body>
```

- 选择器动作-鼠标扫过(hover)

```HTML
<head>
    <style type="text/css">
        a{
            font-size:40px;
            color:#345cff;
        }
        a:hover{
            font-size:60px;
            color:#345cff;
        }
    </style>
</head>
<body>
    <a href="url">Text</a>
</body>
```

### 4.控制边框和背景

#### 1.定义简单边框

```HTML
<head>
    <style type="text/css">
        .class1{
            border-width: 8px;
            border-color: #345cff;
            border-style: solid;
        }
    </style>
</head>
<body>
<p class="class1">text</p>
</body>
```

- border-width
- border-style
  - solid 实线
  - dashed 破折线
  - dotted 点线
- border-color
- border-top-color
- border-bottom-style
- ..............
- border-dimension(哪一块)-property(属性)
- border-radius: xxpx /xxpx
  - 框体圆角

#### 2.Border简写属性

```HTML
<head>
    <style type="text/css">
        .class1{
            border-top: 8px solid red;
            border-bottom: 10px dashed yellow;
        }
    </style>
</head>
<body>
<p class="class1">text</p>
</body>
```

#### 3.定义简单背景

文本框背景

```HTML
<head>
    <style type="text/css">
        .class1{
            width: 800px;
            height: 600px;
            border-top: 8px solid red;
            border-bottom: 10px dashed yellow;
            background-image: url(url);
        }
    </style>
</head>
<body>
<p class="class1">text</p>
</body>
```

body背景

```HTML
<head>
    <style type="text/css">
        .class1{
            background-repeat: no-repeat;
            background-image: url(url);
        }
    </style>
</head>
<body class="class1">
    
</body>
```



- background-color
- background-image
- background-repeat

  - 控制背景是否重复
- background-attachment

  - 背景展示方式
  - default=local
  - fixed
  - local 不跟滑条动
- background-size
- 背景图片的尺寸
  - auto
  - contain 平铺
  - cover

#### 4.background简写属性

### 5.CSS设置文本样式

#### 1.对齐文本

```HTML
<head>
	<style type="text/css">
        .class1{
            text-align:center;
        }
    </style>
</head>
<body>
	<p class="class1">Text</p>
</body>
```

- text-align

  - center
  - right
  - left

- align

  - ```HTML
    <p align="center">Text</p>
    ```

#### 2.文本方向

```HTML
<head>
	<style type="text/css">
        .class1{
            direction:rtl;
        }
    </style>
</head>
```



- directon
  - ltr
  - rtl
  - 仅限英文

#### 3.指定字母间距,单词间距,行间距

```HTML
<head>
	<style type="text/css">
        .class1{
            letter-spacing:10px;
            word-spacing:10px;
            line-height:10px;
        }
    </style>
</head>
```

- letter-spacing
  - 文本间距/每个字母间距
- word-spacing
  - 单词间距
- line-height
  - 行间距

#### 4.缩进

```HTML
<head>
	<style type="text/css">
        .class1{
            text-indent:10px;
        }
    </style>
</head>
```

- text-indent
  - 首行缩进

#### 5.文本装饰

```HTML
<head>
	<style type="text/css">
        .class1{
            text-decoration:underline;
        }
    </style>
</head>
```

- text-decoration
  - underline 下划线
  - overline 上划线
  - line-through 删除线

#### 6.文本大小写转换

- text-transform
  - 中文无效
  - capitalize  单词首字母大写
  - upercase 全部大写
  - lowercase 全部小写

#### 7.字体名称

- font-family
  - 电脑中安装的字体

#### 8.字体大小

- font-size

#### 9.字体样式

- font-style
  - italic 斜体
  - inherit 
  - normal 默认
  - oblique 字体倾斜

#### 10.指定字母是否以小型大写字母显示

- font-variant
  - normal
  - small-caps

#### 11.设置字体粗细

- font-weight
  - bold 粗体
  - bolder 更加粗的粗体
  - normal 默认
  - 100-900数字 粗细

#### 12.创建文本阴影

```HTML
<head>
	<style type="text/css">
        .class1{
            text-shadow:10px 10px 1px red;
        }
    </style>
</head>
```

- text-shadow 需要设置四个值
  - 1竖直偏移
  - 2水平偏移
  - 3模糊程度
  - 4阴影颜色

#### 13.透明度

- opacity
  - 0~1

### 6.CSS使用过渡/动画

```HTML
<head>
	<style type="text/css">
        p{
            width:100px;
            height:100px;
            background-color:antiquewhite;
        }
        p:hover{
            width:200px;
            height:200px;
            background-color:#ffad2a;
            transition-delay: 150ms;
            transition-duration: 500ms;
        }
        
    </style>
</head>
```



#### 1.过渡指令

- hover

#### 2.过渡指令的属性

- transition-delay 操作到开始过渡的延迟
- transition-duration 过渡的时间
- transition-property 设置需要过渡的元素
- transition-timing-function 过渡方式
  - linear 线性 默认
  - ease 贝塞尔曲线式1
  - ease-in 贝塞尔曲线式2
  - ease-out  贝塞尔曲线式3
  - ease-in-out 贝塞尔曲线式4
- 浏览器头
  - -webkit-
    - chrome
    - safari
  - -o-
    - opera
  - -moz-
    - mozilla
  - -ms
    - ie

#### 3.动画

```HTML
<head>
	<style type="text/css">
        p{		
        	width:100px;
        	height:100px;
        	background-color:antiquewhite;

        }
        p:hover{
            animation-delay: 150ms;
            animation-duration: 500ms;
            animation-name: animateName;
            animation-ititeration-count:infinite;
            animation-direction:alternate;
        }
        @keyframes animateName{
            from{
                width:100px;
            	height:100px;
            	background-color:antiquewhite;
            }
            to{
                width:200px;
            	height:200px;
                background-color:#ffad2a;
            }
        }
        
    </style>
</head>
```

- animation-delay
- animation-duration
- animation-name
  - 指定动画名称,并用@keyframes实现
  - @keyframes
    - from{}指定动画初始状态
    - 50%{}指定动画50%时的状态
    - 75%{}指定动画75%时的状态
    - to{}指定动画结束状态
- animation-ititeration-count
  - 动画重复次数
  - infinite
  - 次数

- animation-direction
  - 动画过渡是否平滑初始和结束
  - normal
  - alternate
- animation-fill-mode
  - forwards 停止在最后一帧

#### 4.变换

```HTML
<head>
	<style type="text/css">
        p{
            width:100px;
            height:100px;
            background-color:antiquewhite;
        }
        p:hover{
            width:200px;
            height:200px;
			background-color:antiquewhite;
            transform:rotate(45deg);
        }
        
    </style>
</head>
```

- transform
  - rotate(xxdeg)
    - 旋转xx degree
  - scale(xx)
    - 放大xx倍
  - scalex() 放大x轴
  - scaley() 放大y轴
- transfrom-origin 旋转中心点
  - top right 顶部最右侧
  - bottom right 底部最右侧
  - 20px 40px 距离左侧20px 距顶部40px

### 7.CSS盒子模型

![盒子模型](图片\image-20200306201736795.png)



```HTML
<head>
	<style type="text/css">
        .class1{
            border:1px solid black;
            background-color:antiquewhite;
            padding-top:100px;
            padding-left:100px;
            padding-right:100px;
            background-clip: content-box
        }
    </style>
</head>

<body>
<div class="class1">Text</div>
</body>
```

- background-clip 背景渲染范围
  - content-box
  - border-box
  - padding-box

盒子模型的属性:

- content
- padding
- border
- margin

盒子模型属性的方向:

- top
- bottom
- left
- right

## 三.JavaScript

### 1.嵌入JS

#### 头部书写JS

```HTML
<head>
    <script type="text/javascript">
    	alert("hello world")
    </script>
</head>
```

#### 外部导入JS

```HTML
<head>
    <script src="javascript.js"></script>
</head>
```

### 2.创建变量

```HTML
<script type="text/javascript">
    var text = "Text";
    alert(kaopu);
</script>
```

- var varName = value

### 3.变量使用

```HTML
<script type="text/javascript">
    var number = 100;
    number = number + 200;
    document.write("<h1>"+number+"</h1>");
</script>
```

###  4.条件判断

- if...else if...else

```HTML
<script type="text/javascript">
    var number = 100;
    if(number==100){
        document.write("True");
    }else if(number==200){
        document.write("Double");
    }else{
        document.write("False");
    }
</script>
```

### 5.while循环

```HTML
<script type="text/javascript">
    var number = 100;
    if(number == 100){
        while(number !== 100){
            document.write("False");
        }
        document.write("True");
    }
</script>
```

### 6.for循环

```HTML
<script type="text/javascript">
    for(var i=1;i<=10;i++){
        document.write(i+"<br>");
    }
</script>
```

### 7.数组

```HTML
<script type="text/javascript">
	var numList = Array();
    for(var i=1;i<=10;i++){
        numList[i]=i;
    }
    document.write(numList)
</script>
```