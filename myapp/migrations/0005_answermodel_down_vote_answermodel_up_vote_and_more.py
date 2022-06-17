# Generated by Django 4.0.5 on 2022-06-04 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_questionmodel_answermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='answermodel',
            name='down_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answermodel',
            name='up_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='qn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.questionmodel'),
        ),
    ]
