# GIT

### 1.使用前配置用户名密码

```shell
git config --global user.name "your name"
git config --global user.email "email@example.com"
```

### 2.初始化仓库

```shell
// 初始化工作仓库
git init
// 查看生成的仓库文件
ls -a
```

### 3.文件操作

```shell
# 文件添加/文件修改
# 添加至代码库
git add xxx.py
# 提交到分支
git commit -m 'msg'
# 添加并提交到分支
git commit -a -m 'msg'

# 丢弃工作区文件的修改
git checkout -- xxx.py

# 查看操作日志
git log
git log --oneline

# 回退版本
git reset version_hash
git reset --hard version_hash
# 回退到上一个版本
git reset HEAD

# 删除工作区文件
rm xxx.py
# 删除暂存区中的文件
git rm xxx.py
```

### 4.分支操作

```shell
# 创建分支
git branch 分支名
# 查看分支
git branch
# 切换分支
git checkout 分支名
# 创建+切换分支
git checkout -b 分支名
# 合并某分支到当前分支 版本号相差>=2需要处理
git merge 分支名
# 删除某分支
git branch -d 分支名
```

### 5.配置SSH keys

```shell
# 创建SSH key
# Git Bash
ssh-keygen -t rsa -C "youremail@example.com"
# 用户主目录里找到.ssh目录,id_rsa和id_rsa.pub两个文件(密钥对)
# 用户主目录 C:\Users\Administartor
# GitHub-Account_settings-SSH_keys页面
# Add_SSH_Key:填入id_rsa.pub文件的内容
```

### 6.远程库

```shell
# 关联远程库
git remote add origin git@github.com:bokunopica/git_test.git
# 更新本地库 pull
git pull --rebase origin master
git status
git add xxx.py
git commit -m 'msg'
# 本地库上传至远程库 push
git push -u origin master
```

