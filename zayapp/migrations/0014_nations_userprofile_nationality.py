# Generated by Django 5.0 on 2024-07-03 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayapp', '0013_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='nations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('code', models.CharField(default='', max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nationality',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='zayapp.nations'),
        ),
    ]
