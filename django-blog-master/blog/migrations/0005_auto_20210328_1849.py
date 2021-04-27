# Generated by Django 2.2.1 on 2021-03-28 18:49

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210328_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(upload_to='media/', validators=[blog.validators.file_size]),
        ),
    ]
