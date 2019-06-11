
from django.conf.urls import url
from myapp.views import index, detail, grades, students, gradeStudents
from myapp.views import addstudent, stupage,studentsearch,gradesFilter,attribles,get1,get2,showregister,register
urlpatterns = [
    #^$字符开始结束，中间没有  就是地址端口/
    url(r'^$', index),
    #^数字开始 /结束 （\d+)至少一个数字
    # 加括号可以取出来做参数给视图
    url(r'^(\d+)/$', detail),
    url(r'^grades/$', grades),
    url(r'^students/$', students),
    url(r'^grades/(\d+)$', gradeStudents),
    url(r'^addstudent/$', addstudent),
    url(r'^stu/(\d+)/$', stupage),
    url(r'^studentsearch/$',studentsearch),
    url(r'^gradesFilter/$', gradesFilter),
    url(r'^attribles/$',attribles),
    url(r'^get1/$',get1),
    url(r'^get2/$',get2),
    url(r'^showregister/$',showregister),
    url(r'^showregister/register$',register),
]