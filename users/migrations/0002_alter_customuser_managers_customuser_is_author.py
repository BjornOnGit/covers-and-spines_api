# Generated by Django 5.0.2 on 2024-03-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
    ]
