# Generated by Django 4.0.4 on 2022-05-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201118_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='users/profile_pics/default_image.png', upload_to='users/profile_pics/'),
        ),
    ]
