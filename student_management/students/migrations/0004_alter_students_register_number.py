# Generated by Django 5.0.4 on 2024-04-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_students_register_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='register_number',
            field=models.PositiveIntegerField(),
        ),
    ]