# Generated by Django 4.1.5 on 2023-06-10 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apphoto', '0003_alter_author_data_alter_author_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
