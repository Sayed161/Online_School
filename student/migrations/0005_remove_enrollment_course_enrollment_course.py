# Generated by Django 4.2.7 on 2024-01-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_lesson_course'),
        ('student', '0004_alter_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='course',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ManyToManyField(default=None, to='course.course'),
        ),
    ]
