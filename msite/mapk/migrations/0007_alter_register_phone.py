# Generated by Django 5.1.1 on 2024-10-13 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapk', '0006_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
