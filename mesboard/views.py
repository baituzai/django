from django.shortcuts import render

from .models import MsgPost

# Create your views here.
'''
这个代码表示的是浏览器访问一个地址，这个地址指向该方法，这个方法返回的就是刚才的 html页面。
需要注意的是这里的 messageboard 的是应用 messageboard 下的 templates 模板下的文件夹名称。
------
from .models import MsgPost，意思是从 messageboard/models.py 文件中导入以前建好的表 MsgPost
MsgPost.objects.all(),取出后台数据库中表 MsgPost中的所有的数据。
For循环里面是，遍历得到的所有数据，针对每一条数据，进行编号，并且对每条数据的时间进行格式化，类似2017-02-02 12:00这种
Context 是一个字典，render 方法，会把这个字典数据传给 messageboard/index.html 这个页面，当在浏览器访问地址发起请求的时候。
'''
def index(request):
    msg_list = MsgPost.objects.all()
    for i in range(len(msg_list)):
        msg = msg_list[i]
        msg.datetime = msg.datetime.strftime('%Y-%m-%dT %H:%M:%S')
        msg.index = len(msg_list)- i
    context = {'msg_list':msg_list}
    return render(request, 'mesboard/index.html', context)

'''
msgCreate 就是一个存数据的方法，request.POST[‘content’],是取出 post 请求的 content数据，MsgPost(content=content)，就是创建了一条数据，msg.save()，是保存这个数据到数据库。
return就是把刚刚提交的数据可以实时的在前端页面看到。
面打开 messageboard/urls.py 文件，让我们定义一个前端提交数据到后台的接口地址。
'''
def msgCreate(request):
    content = request.POST['content']
    msg = MsgPost(content=content)
    msg.save()
    return index(request)