# Generated by Django 5.0 on 2024-07-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayapp', '0017_alter_contact_message_alter_contact_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
    ]