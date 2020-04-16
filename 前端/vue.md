# Vue

## 安装

1.cdn引入

2.本地下载

## 1.模板语法

### (1)插值

- a.文本{{}}
- b纯HTML
  - v-html,防止XSS,csrf
    - 前端过滤
    - 后台转义(<> \&lt;  \&gt;)
    - 给cookie加上属性http