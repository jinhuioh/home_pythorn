# Generated by Django 3.2.13 on 2022-05-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name=100)),
                ('title', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=500)),
            ],
        ),
    ]
