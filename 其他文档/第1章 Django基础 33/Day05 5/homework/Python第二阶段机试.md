# 机试
## 要求
- 所有同学收起手机
- 关闭所有聊天通讯工具（飞秋，QQ，微信）
- 最后交代码压缩包  zip, gz
- 和已完成功能的文件 


# 项目需求
- 数据库统一使用默认数据库SQLite
- 实现所有页面展示
- 实现主页面轮播，电影列表显示，电影详情信息
- 实现注册，登录
- 实现用户信息修改
- 实现收藏，与取消收藏

### 加分项
- 前后端分离实现
- 在注册前实现用户名预校验，其它字段的合法验证，以及数据安全



# 轮播图连接
>* https://www.vmovier.com/apiv3/index/getBanner

# 电影列表链接
>* https://www.vmovier.com/apiv3/post/getPostInCate?cateid=0&p=1

# 数据
-	postid		唯一标识
  - title		标题
    - image	图片
    - duration时长	
  - app_fu_title简要信息


# 电影详情{{postid}} 是替换值
>* https://www.vmovier.com/{{postid}}?qingapp=app_new


