# Generated by Django 2.2.1 on 2021-03-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210330_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(default='default.mp4', upload_to='video/% Y/% m/% d/'),
        ),
    ]