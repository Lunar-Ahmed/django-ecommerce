# Generated by Django 5.0.9 on 2024-10-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapk', '0012_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default='sneaker1.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default='sneaker1.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, default='sneaker1.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, default='sneaker1.jpg', upload_to=''),
        ),
    ]
