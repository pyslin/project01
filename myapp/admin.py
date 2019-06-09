from django.contrib import admin

# Register your models here.
#当前目录下models
from myapp.models import Grades, Students

#创建班级的时候同时创建2个学生
class StudentInfo(admin.TabularInline):
    model = Students
    extra = 2
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentInfo,]
    list_display = ('pk', 'gname', 'gdate','ggirlnum','gboynum','isDelete',)
    list_filter = ('gname',)
    search_fields = ('gname',)
    list_per_page = 5
    #添加修改页属性
    fields = ('ggirlnum', 'gboynum', 'gname', 'gdate',)
   #fieldsets = []

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    #列名
    gender.short_description = '性别'
    list_display = ('pk', 'sname', 'sage',gender,'scontend', 'sgrade', 'isDelete',)
    list_per_page = 5
    #actions_on_top = Flase

#admin.site.register(Grades, GradesAdmin)
#admin.site.register(Students,StudentsAdmin)


