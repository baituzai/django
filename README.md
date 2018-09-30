### Django服务器开发之留言板项目
<p>很多网站使用Django作为框架进行搭建，非常适合内容管理的场景。</p>

#### 1项目目录

#####  1.1. django 项目环境
#####  1.2. 留言板应用
#####  1.3. 模型表Model
#####  1.4. 视图 View

#####  1.1. django 项目环境
本文使用 linux 64位 ubuntu18.04版本 python3.6.6版本
###### 1.1.1 安装python
linux 系统自带python2.7环境，本文使用python3.6.6版本
```bash
python -v
```
###### 1.1.2 安装Django
在python环境下，安装django
打开命令行终端工具，执行 
```bash
pip install django
```
检测是否安装成功，运行python环境 执行
```bash
import django
```
##### 第二节 留言板应用
###### 2.1 创建项目
创建一个名为mysite的工作目录。注意 mysite 后面有个空格和一个英文的 . 符号。
```bash
django-admin startproject mysite . 
```
此时创建好了一个名为 mysite 的文件夹

执行
```bash
python manage.py runserver
```
访问
```bash
http://127.0.0.1:8000/
```
项目建好之后，我们需要编译一下数据库
为 mysite 建一个数据库,makemigrations这个就是编译文件
```bash
python manage.py makemigrations 
```
migrate 就是把刚刚编译的文件起到作用
```bash
python manage.py migrate
```
那现在就在浏览器里面访问http://127.0.0.1:8000/admin 效果
