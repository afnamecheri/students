# Generated by Django 3.2 on 2024-04-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_delete_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]
