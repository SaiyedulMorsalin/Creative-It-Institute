# Generated by Django 5.1 on 2024-08-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudent',
            name='student_img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
