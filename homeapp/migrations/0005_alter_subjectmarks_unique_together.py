# Generated by Django 4.2.6 on 2023-10-22 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_alter_department_options_remove_student_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subjectmarks',
            unique_together={('student_id', 'subject')},
        ),
    ]
