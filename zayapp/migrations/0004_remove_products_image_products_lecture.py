# Generated by Django 5.0 on 2024-06-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayapp', '0003_rename_product_image_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='lecture',
            field=models.FileField(blank=True, null=True, upload_to='static/videos/'),
        ),
    ]