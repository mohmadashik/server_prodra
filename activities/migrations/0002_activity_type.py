# Generated by Django 4.2.17 on 2024-12-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.CharField(default='run', max_length=32),
        ),
    ]