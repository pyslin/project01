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
对象.model类名_set.all()

database: select * from myapp_grades

c
python manage.py runserver (ip)(:port)
python manage.py createsuperuser
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE =  'Asia/Shanghai'


"""