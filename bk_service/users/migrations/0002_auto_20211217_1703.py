# Generated by Django 3.2 on 2021-12-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at'),
        ),
    ]
