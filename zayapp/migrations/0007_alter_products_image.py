# Generated by Django 5.0 on 2024-06-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayapp', '0006_rename_lecture_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/image/'),
        ),
    ]