from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Text)#用 createsuperuser创建一个超级管理员进入admin页面操作