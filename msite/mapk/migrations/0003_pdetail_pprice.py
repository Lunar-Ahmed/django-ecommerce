# Generated by Django 5.1.2 on 2024-10-10 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapk', '0002_remove_pdetail_pimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdetail',
            name='pprice',
            field=models.TextField(max_length=10, null=True),
        ),
    ]
