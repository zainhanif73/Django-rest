# Generated by Django 3.0.14 on 2022-02-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city_id', models.IntegerField()),
                ('location', models.CharField(max_length=300)),
                ('contact', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='AdminModel',
            new_name='Admin',
        ),
    ]