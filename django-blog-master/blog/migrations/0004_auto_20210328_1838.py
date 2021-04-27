# Generated by Django 2.2.1 on 2021-03-28 18:38

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(upload_to='./video/', validators=[blog.validators.file_size]),
        ),
    ]
