from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('is good man')

def detail(request,num):
    return HttpResponse('detail-%s'%num)

from  .models import Grades
def grades(request):
    #model里面取数据
    gradesList = Grades.objects.all()
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/grades.html', {'grades': gradesList})

from .models import Students
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
1
    #有了数据,模板  然后渲染，传回页面
    return render(request, 'myapp/students.html', {'students': studentsList})
