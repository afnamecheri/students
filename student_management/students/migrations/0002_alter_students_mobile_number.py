# Generated by Django 5.0.4 on 2024-04-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
