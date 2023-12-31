# Generated by Django 4.1.5 on 2023-06-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphoto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.AddField(
            model_name='author',
            name='data',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='author',
            name='post_type',
            field=models.CharField(choices=[('O', 'Одиночная фотосессия'), ('G', 'Групповая фотосессия')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='time',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
