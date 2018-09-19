
from __future__ import unicode_literals
from django.db import models

# Create your models here.
'''
MsgPost 是我们建的表名，这个表有三个字段，content 是文本类型的，用来存储留言的内容，datetime是时间字段，用来存储留言的时间，index 是整型字段，用来存储留言的顺序.Ordering 用来指明表中的数据，按照哪些字段来排序，我们这里写了一个按照时间来排序，‘-datetime’，时间逆序排，‘datetime’，时间正常排序.auto_now_add,的意思就是创建表数据的时候，那个时间，系统自动帮你填，自己呢就不用去写了。

表MsgPost 建好了，我们需要重新编译一下数据库文件，告知django需要为 messageboard 应用建一个模型表MsgPost。
终端里分别先后执行：python manage.py makemigrations messageboard 和 python manage.py migrate
'''
class MsgPost(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField(default=0)
    class Meta:
        ordering = ['-datetime']