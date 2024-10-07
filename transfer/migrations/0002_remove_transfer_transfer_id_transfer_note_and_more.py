# Generated by Django 4.2 on 2024-10-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='transfer_id',
        ),
        migrations.AddField(
            model_name='transfer',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
