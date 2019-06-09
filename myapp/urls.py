
from django.conf.urls import url
from myapp.views import index,detail

urlpatterns = [
    #^$字符开始结束，中间没有  就是地址端口/
    url(r'^$', index),
    #^数字开始 /结束 （\d+)至少一个数字
    # 加括号可以取出来做参数给视图
    url(r'^(\d+)/$',detail),
]