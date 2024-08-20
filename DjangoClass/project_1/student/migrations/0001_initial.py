# Generated by Django 5.1 on 2024-08-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=50)),
                ('student_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
