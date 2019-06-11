from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('is good man')

def detail(request,num):
    return HttpResponse('detail-%s'%num)

from  myapp.models import Grades
def grades(request):
    #model里面取数据
    gradesList = Grades.objects.all()
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/grades.html', {'grades': gradesList})

from myapp.models import Students
def students(request):
    #model里面取数据
    studentsList = Students.objects.all()
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/students.html', {'students': studentsList})

def gradeStudents(request,num):
    #model里面对应班级
    grade = Grades.objects.get(pk=num)
    #班级对象.小写学生类名_set。all（）
    studentsList = grade.students_set.all()
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/students.html', {'students': studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent('刘德华', 34, True, '我叫刘德华', grade)
    stu.save()
    return HttpResponse('have created one student')

#分页取数据
def stupage(request,page):
    #model里面取数据
    page = int(page)
    studentsList = Students.objects.all()[(page-1)*5:page*5]
    #studentsList = Students.objects.all()[0:3]这里下标不能负数
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/students.html', {'students': studentsList})
    #数据集会放缓存的，方便下次查询

from django.db.models import  Q
from django.db.models import Max,Min,Avg,Count
def studentsearch(request):
    # 格式sage__双下划线   外键sgrade_
    # in exact contains startswith endswith  前面加i 表示不区分大小写
    #isnull isnotnull
    #gt gtq lt ltq
    #year month day hour minute second
    #studentsList = Students.objects.filter(sname__contains='刘')
    #studentsList = Students.objects.filter(sname__startswith='胡')
    #studentsList = Students.objects.filter(sgrade=1)
    #studentsList = Students.objects.filter(sname__isnull=False)
    #studentsList = Students.objects.filter(sname__contains='刘')
    #studentsList = Students.objects.filter(pk__in=[14,15])
    #studentsList = Students.objects.filter(lasttime__year=2019)
    #studentsList = Students.objects.filter(sage__gt=20)
    #满足逻辑或的需求 Q
    #studentsList = Students.objects.filter(~Q(pk__lte=2) ) #加波浪形取反
    studentsList = Students.objects.filter(Q(pk__lte=2)|Q(sage__gt=10))
    #是最大age的值，不是student
    MaxAge = Students.objects.aggregate(Max('sage'))
    print(MaxAge)
    #studentsList = Students.objects.get(sage=MaxAge)
        #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/students.html', {'students': studentsList})

from django.db.models import  F
def gradesFilter(request):
    #同一对象筛选  不同属性比较
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+10)
    print(g)
    return HttpResponse('****')