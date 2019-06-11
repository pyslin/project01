from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    #返回属性
    def __str__(self):
        return self.gname

class StudentsManager(models.Manager):
    #继承manager类，重写方法，过滤返回的集合
    def get_queryset(self):
        #父类，方法 加一个过滤条件，
        # exclude是满足条件以外的 oberby排序
        #values 返回多个对象的列表
        #get无符合或多个会引发异常 count查询集个数 first last exists
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

class Students(models.Model):
    #自定义模型管理器，取代原来objects
    #顺便改个名stuOBJ= models.manager()
    objects = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    scontend = models.CharField(max_length=20)
    sage = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    lasttime = models.DateTimeField(auto_now=True)
    #关联外键
    sgrade = models.ForeignKey('Grades',on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
    class Meta:
        #定义数据表名
        db_table = 'students'
        #对象默认排序字段 id降序,会增加开销
        ordering = ['-id']

    #新建类方法用于创建对象
    @classmethod
    def createStudent(cls,name,age,gender,contend,grade):
        stu = cls(
            sname=name,
            sage=age,
            sgender=gender,
            scontend=contend,
            sgrade=grade,
        )
        return stu

