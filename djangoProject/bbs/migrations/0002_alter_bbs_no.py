# Generated by Django 3.2.13 on 2022-05-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='no',
            field=models.IntegerField(max_length=100),
        ),
    ]
