# Generated by Django 4.0.5 on 2022-06-29 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answermodel',
            name='updated_on',
        ),
    ]
