from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from myapp.models import Students
def index(request):
    student = Students.objects.get(pk=1)
    return render(request,'myapp/index.html',{'stu':student,'num':10})

def detail(request,num):
    return HttpResponse('detail-%s'%num)

from  myapp.models import Grades
def grades(request):
    #model里面取数据
    gradesList = Grades.objects.all()
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/grades.html', {'grades': gradesList})


def students(request):
    #model里面取数据
    studentsList = Students.objects.all()
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/students.html', {'students': studentsList,'num':10, 'str': ' good man','list':['sunck','good']})

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

def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    print()
    return HttpResponse('attibels')

def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a+' '+b+' '+c)
#http://127.0.0.1:8000/get1/?a=1&b=2&c=3

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    return HttpResponse(a1+' '+a2)
#http://127.0.0.1:8000/get2/?a=1&a=2

def showregister(request):
    return render(request,'myapp/register.html')

#from myapp.models import Person
def register(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    #person = Person()
    #person.name = name
    #person,age = age
    #person.save()
    return HttpResponse('register done')

def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

def cookietest(request):
    res = HttpResponse()
    #cookie = res.set_cookie('sunk','good man')
    cookie = request.COOKIES
    res.write('<h1>'+cookie['sunk']+'</h1>')
    return res

#from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(request):
    #return HttpResponseRedirect('/redirect2')
    return redirect('/redirect2')
def redirect2(request):
    return HttpResponse('我是重定向后对象')

def main(request):
    #session的id是存在cookies里面 得到后再去redis取
    #request.COOKIES('sessionid')
    #取session，后值是取不到时默认
    username = request.session.get('name','游客')
    print(username)
    return render(request,'myapp/main.html',{'username':username})

def login(request):
    return render(request,'myapp/login.html')

def showmain(request):
    #login点击后  存session
    username = request.POST.get('username')
    #默认2个星期过期，可设置数字秒 0为关闭浏览器过期，None 永不过期
    request.session.set_expiry(5000)
    request.session['name'] = username
    return redirect('/main')

from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)
    #request.session.clear()
    #request.session.flush()
    return redirect('/main')
