# Generated by Django 3.2.4 on 2021-06-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='no_picture.png', upload_to='posts/%y'),
        ),
    ]
