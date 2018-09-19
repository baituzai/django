from django.contrib import admin

# Register your models here.
'''
打开 messageboard/admin.py 文件，把刚才建好的表，在这里注册一下。
这些代码的作用就是让那个表在后台 admin 那里可以看到。
'''
from .models import MsgPost
class MsgPostAdmin(admin.ModelAdmin):
    list_display =('pk','content','datetime')
admin.site.register(MsgPost,MsgPostAdmin)