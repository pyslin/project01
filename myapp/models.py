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


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    scontend = models.CharField(max_length=20)
    sage = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey('Grades',on_delete=models.CASCADE)
    def __str__(self):
        return self.sname

