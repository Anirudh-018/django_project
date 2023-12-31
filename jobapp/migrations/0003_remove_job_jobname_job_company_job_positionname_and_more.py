# Generated by Django 4.1.12 on 2023-10-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_rename_loaction_job_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='jobName',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default='no name', max_length=50),
        ),
        migrations.AddField(
            model_name='job',
            name='positionName',
            field=models.CharField(default='no name', max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.CharField(default='no name', max_length=250),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(default='no name', max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(default='no name', max_length=60),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(default='no name', max_length=60),
        ),
    ]
