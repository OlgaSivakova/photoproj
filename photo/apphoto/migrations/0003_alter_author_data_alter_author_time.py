# Generated by Django 4.1.5 on 2023-06-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphoto', '0002_remove_post_post_type_author_data_author_post_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='data',
            field=models.CharField(default='01/01/24', max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='time',
            field=models.CharField(default='12:00 - 13:00', max_length=11, null=True),
        ),
    ]
