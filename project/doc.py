"""

pip uninstall name
pip install django
from package import pyname
from pyname import class

#get version
python
import django
djiango get_version()

#start project & app
django-admin startproject project
python manage.py startapp myapp


#mysql
mysql -u root -p
show databases;
use databasename;
show tables;
drop database databasename;
create datebase databasename;

#migrate model
python manage.py makemigrations
python manage.py migrate


@@@@当前虚拟环境内venv\lib\site-pack\django\db\backends\mysql\base.py"
if version < (1, 3, 13):
    pass
#   raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
operations.py
        if query is not None:
            query = query.encode(errors='replace')
            #query = query.decode(errors='replace')

python manage.py shell
from myapp.models import Grades,Students
from myapp.models import timezone
from myapp.models import *
Grades.objects.all()
grade1 = Grades()
grade1.name = 'python04'
grade1.save()
model类名.objects.all()
model类名.objects.get()
对象.model类名_set.all()

database: select * from myapp_grades

c
python manage.py runserver (ip)(:port)
python manage.py createsuperuser
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE =  'Asia/Shanghai'



git clone /path/to/repository（克隆到本地仓库）
git clone username@host:/path/to/repository（克隆到网上仓库）
share project on github   project  pyslin

git update添加(暂时）和提交commit

git push origin maste （更新push到网上仓库）


把网上的拉下来：
git pull

分支是用来将特性开发（新功能）绝缘开来的。在你创建仓库的时候，master 是“默认的”分支。
在其他分支上进行开发，完成后再将它们合并到主分支上。
创建一个叫做“develop”的分支，并切换过去：
git checkout -b develop

切换回主分支：
git checkout master



TextField
DecimalField(max_digits,decimal_places) 小数（总位数，点后位数）
FloatField
NullBooleanField

DataField(auto_now=Ture,auto_now_add=)
可以保存修改时间  或第一创建时间
TimeField
DateTimeField

FileField
上传文件的字段
ImageField
图片（会校验是否图片）

null
是否保存null
 blanke
 db_column
 可以指定列名
 unique=True

ForeignKey
一对多，在多端
访问：.对象。模型类小写_set
grade.students_set
访问id  student.sgrade_id
 ManyToManyField
在两端都要

insert into students(sname,sgender,scontend,isDelete,sgrade_id,sage) values('','',..)('',''..)
select where like  .. from
stud = Students.objects.get(pk=1)
stu.sage= 20

400客户端出错
404找不到网页无匹配视图
500服务器端出错

path method encoding GET POST FILES COKKIES session
get() getlist()

# 向图书馆增加数据GET或POST方法方法
def addbooktodatabase(request):
    # 获取参数book_name,author,author_age
    if request.method == "GET":
        book_name = request.GET["book_name"]
        author_name = request.GET["author"]
        author_age = request.GET["author_age"]
    else:
        book_name = request.POST["book_name"]
        author_name = request.POST["author"]
        author_age = request.POST["author_age"]

    ## 先增加作者信息
    from polls.models import Person
    person = Person()
    person.name = author_name
    person.age = author_age
    person.save()
    ## 增加图书信息
    from polls.models import Book
    bookadded = Book(name=book_name)
    # 保存修改
    bookadded.person_id = person.id
    bookadded.save()
    # 重定向到添加成功页面
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/addok/')


安装redis
pip install django-redis-sessions 配置setting 用redis作为缓存

pip install list
验证码
"""