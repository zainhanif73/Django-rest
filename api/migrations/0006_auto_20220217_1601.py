# Generated by Django 3.0.14 on 2022-02-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220216_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AlterField(
            model_name='reciptionist',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
    ]
