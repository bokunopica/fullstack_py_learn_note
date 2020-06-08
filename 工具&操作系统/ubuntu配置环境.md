#### 配置xshell链接

sudo apt-get install openssh-server

1. service ssh start
2. /etc/init.d/ssh start

### APT配置

sudo apt update

#### 配置mysql

安装 sudo apt install mysql-server

配置文件 sudo mysql_secure_installation

![img](..\图片\ubuntu00.jpg)

设置远程访问

```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
注释掉
# bind-address      = 127.0.0.1
```

设置所有人都可连接

```
mysql -uroot -p
mysql>grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
# 表示允许任何主机远程连接，连接的密码是123456
exit
```

重启服务

```
service mysql restart
```

用户登录拒绝问题

```
解决步骤：

1、打开MySQL目录下的配置文件(我的目录是/etc/mysql/mysql.conf.d/mysqld.cnf, 可能有的系统是my.ini)，在文件的最后添加一行“skip-grant-tables”，保存并关闭文件。

2、重启MySQL服务(我用命令 service mysql restart)。

3、在命令行中输入“mysql -uroot -p”(不输入密码)，回车即可进入数据库。

4、执行，“use mysql;”使用mysql数据库。

5、执行，“update user set authentication_string=PASSWORD("rootadmin") where user='root';”（修改root的密码, 有的mysql表列名可能是password, 需要是命令:"update user set password=PASSWORD("rootadmin") where user='root';"）
```



#### 配置python3.7优先级

- 调整Python3的优先级，使得3.7优先级较高
  - sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
  - sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2

- 更改默认值，python默认为Python2，现在修改为Python3
  - sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
  - sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150

- easy_install
  - sudo apt-get install python-setuptools python-dev build-essential

#### No module named 'apt_pkg'

1.先将原来的Python apt模块进行删除：

sudo apt-get remove --purge python-apt

2.再将它删除：

sudo apt-get install -f -y python-apt

3.进入文件层：

cd /usr/lib/python3/dist-packages/

4.将它改变：

sudo cp apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.cpython-37m-x86_64-linux-gnu.so


#### 配置pip源

首先在当前用户目录下建立文件夹.pip，然后在文件夹中创建pip.conf文件，再将源地址加进去即可。

mkdir ~/.pip
vim ~/.pip/pip.conf
\# 然后将下面这两行复制进去就好了
[global]
index-url = https://mirrors.aliyun.com/pypi/simple

#### virtualenv配置

安装virtualenv 和 virtualenvwrapper

创建目录

```
mkdir $HOME/.virtualenvs
```

修改bashrc文件

```
export WORKON_HOME=~/.virtualenvs

source ~/.local/bin/virtualenvwrapper.sh
source ~/.bashrc
```

创建虚拟环境

```
mkvirtualenv env
```

删除虚拟环境

```
rmvirtualenv env
```



#### pycharm配置

project interpreter ->配置文件存储位子和环境位置

















#### nginx

 详见:http://nginx.org/en/linux_packages.html

控制nginx

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

nginx配置文件

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

启动nginx服务

```
sudo nginx -c /home/bool/DjangoLearnProject/HelloNginx/config/nginx.conf
```

