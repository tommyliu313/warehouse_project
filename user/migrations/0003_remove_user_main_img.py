# Generated by Django 4.2 on 2024-09-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='main_img',
        ),
    ]
