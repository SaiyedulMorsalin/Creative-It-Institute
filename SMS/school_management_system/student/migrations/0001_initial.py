# Generated by Django 5.1.1 on 2024-09-09 02:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('course', '0001_initial'),
        ('department', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=11, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('student_type', models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Irregular', 'Irregular')], max_length=15, null=True)),
                ('registration_id', models.PositiveIntegerField(blank=True, null=True)),
                ('secret_key', models.CharField(blank=True, max_length=6, null=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('admission_at', models.DateTimeField(auto_now_add=True)),
                ('courses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_courses', to='course.course')),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_department', to='department.department')),
                ('permanent_address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_permanent_address', to='address.permanentaddress')),
                ('present_address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_present_address', to='address.presentaddress')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
