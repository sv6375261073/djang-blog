# Generated by Django 2.2.1 on 2021-03-28 19:12

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210328_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(default='default.mp4', upload_to='media/', validators=[blog.validators.file_size]),
        ),
    ]
