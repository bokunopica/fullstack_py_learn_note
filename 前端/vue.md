# Vue

## 安装

1.cdn引入

2.本地下载

## 基础

### 1.模板语法

#### (1)插值

- a.文本{{}}
- b纯HTML
  - v-html,防止XSS,csrf
    - 前端过滤
    - 后台转义(<> \&lt;  \&gt;)
    - 给cookie加上属性http
- c.表达式
  - 三目
    - {{ 10>20?'True':'False' }}
  - 计算
    - {{ 10+20 }}

#### (2)指令:带有v-前缀的特殊属性

- v-if
  - 布尔值
  - 创建/删除
- v-show
  - 布尔值
  - 显示/隐藏
- v-html
  - html带标签文本
  - 将html标签文本渲染到页面
- v-bind
- v-on:click
- v-for

#### (3)缩写

- v-bind:src => :src
- v-on:click =>@click

### 2.动态绑定class/style

(1)绑定class/style

- 三目
- 对象
- 数组

```html
<body>
    <div id="box">
        <button @click='handleClick()'>click</button>
        <div :class="isActive?'red':'yellow'">动态绑定class-三目写法</div>
        <div :class="classObj">动态绑定class-对象写法</div>
        <div :class="classArr">动态绑定class-数组写法</div>

        <div :style="'background:' + (isActive?'red':'yellow')">动态绑定style-三目写法</div>
        <div :style="styleObj">动态绑定style-对象写法</div>
        <div :style="styleArr">动态绑定style-数组写法</div>
    </div>
    <script>
        var vm = new Vue({
            el: "#box",
            data: {
                isActive: true,
                classObj: {
                    a: true,
                    b: true,
                },
                classArr: ["a", "b"],
                styleObj: {
                    background: 'red',
                },
                styleArr: [{background: "yellow"}],
            },
            methods: {
                handleClick(){
                    this.isActive = !this.isActive;
                }
            }
        })
    </script>
</body>
```

### 3.条件渲染

- v-if
- v-else v-else-if
- template v-if,包装元素template不会被创建
- v-show

### 4.列表渲染

- v-for (特殊 v-for="n in 10")
  - in
  - of

- key:
  - 追踪每个节点的身份,从而重用和重新排序现有元素
  - 理想的key值是每项都有的且唯一的id:data.id
    - data.id是后端传来的json数据的id
- vue对象中的数组更新检测
  - 使用以下方法操作数组,可以检测变动
    - push
    - pop
    - shift
    - unshift
    - splice
    - sort
    - reverse
  - 新数组替换旧数组
    - filter
    - concat
    - slice
    - map
  - 不能检测以下变动的数组
    - vm.items[indexOfItem] = newValue
    - 解决方法
      - Vue.set(example.items,indexOfItem,newValue)
      - splice(start_index,end_index,changeInfo)
- 应用:显示过滤结果

### 5.事件处理

(1) 监听事件-直接触发代码

(2)方法事件处理器-写函数名  handleClick

(3)内联处理器方法-执行函数表达式 handleClick($event)  $event事件对象

(4)事件修饰符 https://cn.vuejs.org/v2/guide/events.html

- ev.stop
  - 阻止冒泡
- ev.prevent
  - 阻止默认行为
- ev.self
  - 只运行绑定自己的事件
- ev.once
  - 触发一次后解除事件绑定

(5)按键修饰符

- @keyup
  - @keyup.enter
  - @keyup.13

### 6.表单控件绑定/双向数据绑定

v-model

(1)基本用法

```html
<div id="box">
    <input type="text" v-model="demo1">
</div>	
<script>
    var vm = new Vue({
        el:"#box",
        data:{
            demo1: "",
        }
    })
</script>
```

(2)修饰符

- lazy
  - 懒加载
- num
  - 数字
- trim
  - 去首尾空格

## 组件

### 1.axios与fetch实现数据请求

(1)fetch

```javascript
fetch("/json/demo.json")
.then(res=>{return res.json()})
.then(res=>{console.log(res.data);})
```

(2)axios

- github地址

```
https://github.com/axios/axios
```

- cdn引入

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

- 实际操作
  - 返回的数据会被包在一个键值对中的data中

```javascript
axios.get("")
axios.post("")
axios.put("")
axios.delete("")

axios({
    url:"/gateway?type=2&k=3553574",
    headers:{
        'X-Client-Info': '{"a":3000,"ch":"1002"}',
        'X-Host': 'mall.cfg.common-banner'
}})
.then(res=>{console.log(res.data);})
```

### 2.计算属性

```html
<div id="box">
    <p>直接写：{{myname.substring(0,1).toUpperCase() + myname.substring(1)}}</p>

    <p>计算属性：{{getMyName}}</p>

    <p>方法：{{getMyNameFunc()}}</p>

</div>
<script>
    var vm = new Vue({
        el:"#box",
        data:{
            myname: "demo",
        },
        computed:{
            getMyName(){
                return this.myname.substring(0,1).toUpperCase() + this.myname.substring(1)
            }
        },
        methods:{
            getMyNameFunc(){
                return this.myname.substring(0,1).toUpperCase() + this.myname.substring(1);
            }
        }
    })
</script>
```

### 5.组件化开发基础

扩展HTML元素，封装可重用的代码

### 6.组件注册方式

a.全局组件

Vue.component

b.局部组件

### 7.组件编写方式与Vue实例的区别

- 自定义组件需要有一个root element
- 父子组件的data是无法共享的
- 组件可以有data,methods,computed....,但是data必须是一个函数

### 8.组件通信

1. 父子组件传值(props down,events up)
2. 属性验证
   - props:{name:Number}
   - Number,String,Boolean,Array,Object,Function,null(不限制类型)
3. 事件机制
   - a.使用$on(eventName)监听事件
   - b.使用$emit(eventName)触发事件