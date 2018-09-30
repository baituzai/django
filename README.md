### Django服务器开发
<p>很多网站使用Django作为框架进行搭建，非常适合内容管理的场景。</p>

#### 项目目录

#####  1. django 项目环境
#####  2. 留言板应用
#####  3. 模型表Model
#####  4. 视图 View

##### 第一节 安装环境
###### 1.1 安装python
windows 下Python 安装及pip 安装，环境变量配置，按照 https://pypi.python.org/pypi/pip#downloads 这个文档步骤来就行了。
检测python是否安装成功（本文使用python3.6版）
```bash
python -v
```
###### 1.2 安装Django
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
