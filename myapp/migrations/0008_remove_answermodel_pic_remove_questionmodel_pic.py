# Generated by Django 4.0.5 on 2022-06-06 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_answermodel_pic_questionmodel_pic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answermodel',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='pic',
        ),
    ]
