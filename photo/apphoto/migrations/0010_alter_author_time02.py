# Generated by Django 4.1.5 on 2023-07-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphoto', '0009_author_time02'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='time02',
            field=models.CharField(max_length=11, null=True),
        ),
    ]