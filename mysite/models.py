from django.db import models

# Create your models here.
class Text(models.Model):#数据 manage.py migrate  去admin注册
    id = models.IntegerField(primary_key=True,auto_created=True)
    content = models.CharField(max_length=500)
    # class Meta:
    #     db_table='t_text'