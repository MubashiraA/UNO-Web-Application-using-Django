# Generated by Django 4.0.5 on 2022-06-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_answermodel_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answermodel',
            name='answer',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='qn',
            field=models.TextField(max_length=1000),
        ),
    ]
