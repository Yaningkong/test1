# Generated by Django 2.2.2 on 2021-03-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 't_text',
            },
        ),
        migrations.DeleteModel(
            name='Stu',
        ),
    ]
