# Generated by Django 4.1.5 on 2023-09-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphoto', '0011_alter_author_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='data',
            field=models.CharField(default='01/01/24', max_length=10, null=True, unique=True),
        ),
    ]
