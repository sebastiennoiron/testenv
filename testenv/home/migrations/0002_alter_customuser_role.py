# Generated by Django 3.2.13 on 2022-06-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('FM', 'base farmer'), ('SM', 'salesman'), ('TSP', 'tech support'), ('RMG', 'regional manager'), ('PMG', 'project manager')], max_length=25),
        ),
    ]