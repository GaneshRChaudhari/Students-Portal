# Generated by Django 4.2.6 on 2023-10-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['department']},
        ),
        migrations.RemoveField(
            model_name='student',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
